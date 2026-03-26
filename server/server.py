import asyncio
import websockets
import json
import uuid
from datetime import datetime, timezone

from core.satellite import Satellite
from simulation.event_engine import event_engine

# clients
connected_clients = set()
client_log_levels = {}

def generate_id():
    return str(uuid.uuid4())

# satellites
system_satellites = [
    Satellite(generate_id(), "TestSatellite1", "Sputnik"),
    Satellite(generate_id(), "TestSatellite2", "Sputnik"),
]

TRANSITION_DELAY = 1.5  # delay (in seconds)

async def broadcast(msg):
    # no clients
    if not connected_clients:
        return

    msg_as_json = json.dumps(msg)

    if msg.get("type") == "LOG":
        log_level = msg.get("level")
        tasks = []
        for client in connected_clients:
            client_level = client_log_levels.get(client, "ALL")
            if client_level == "ALL" or client_level == log_level:
                tasks.append(client.send(msg_as_json))
        if tasks:
            await asyncio.gather(*tasks)
    else:
        await asyncio.gather(*[client.send(msg_as_json) for client in connected_clients])

async def complete_transition_after_delay(sat, satellite_id, satellite_name):
    await asyncio.sleep(TRANSITION_DELAY)
    if sat.complete_transition():
        timestamp = datetime.now(timezone.utc).strftime("%H:%M:%S")
        final_state = sat.state()

        await broadcast({
            "type": "SATELLITE_STATE_UPDATE",
            "satellite_id": satellite_id,
            "satellite_name": satellite_name,
            "new_state": final_state,
            "last_message": sat.last_message,
            "timestamp": timestamp
        })

        await broadcast({
            "type": "LOG",
            "sender": "System",
            "level": "STATUS",
            "message": f"New state: {final_state.upper()}",
            "timestamp": timestamp
        })
        print(f"Transition completed: {satellite_name} -> {final_state}")

async def handler(websocket):
    print("New client connected!")
    connected_clients.add(websocket)
    client_log_levels[websocket] = "ALL"

    client_id = f"CLIENT-{id(websocket)}"
    await websocket.send(json.dumps({
        "type": "sync",
        "client_id": client_id,
        "satellites": [sat.to_dict() for sat in system_satellites]
    }))

    try:
        async for message in websocket:
            try:
                # convert to json format
                data = json.loads(message)

            except json.JSONDecodeError:
                await websocket.send(json.dumps({"error": "Invalid JSON format!"}))
                continue

            message_type = data.get("type")

            if message_type == "CHANGE_STATE":
                satellite_id = data.get("satellite_id")
                satellite_name = data.get("satellite_name")
                new_state = data.get("new_state")

                # shutdown is handled separately — removes satellite from list
                if new_state == "SHUTDOWN":
                    sat_ref = None
                    for sat in system_satellites:
                        if sat.id == satellite_id:
                            sat_ref = sat
                            break

                    if sat_ref and sat_ref.state() in ["new", "init", "safe", "error"]:
                        satellite_name = sat_ref.name
                        system_satellites.remove(sat_ref)
                        timestamp = datetime.now(timezone.utc).strftime("%H:%M:%S")

                        await broadcast({
                            "type": "SATELLITE_REMOVED",
                            "satellite_id": satellite_id
                        })

                        await broadcast({
                            "type": "LOG",
                            "sender": satellite_name,
                            "level": "STATUS",
                            "message": "Shutting down satellite",
                            "timestamp": timestamp
                        })
                        print(f"Satellite removed: {satellite_name}")
                    else:
                        await websocket.send(json.dumps({"error": "Cannot shutdown satellite in current state"}))

                else:
                    success = False
                    sat_ref = None

                    for sat in system_satellites:
                        if sat.id == satellite_id: # find correct satellite
                            satellite_name = sat.name
                            success = sat.process_cmd(new_state) # process through fsm
                            sat_ref = sat
                            break

                    timestamp = datetime.now(timezone.utc).strftime("%H:%M:%S")

                    if success and sat_ref:
                        current_state = sat_ref.state()

                        await broadcast({
                            "type": "SATELLITE_STATE_UPDATE",
                            "satellite_id": satellite_id,
                            "satellite_name": satellite_name,
                            "new_state": current_state,
                            "last_message": sat_ref.last_message,
                            "timestamp": timestamp
                        })

                        if sat_ref.is_transitioning():
                            await broadcast({
                                "type": "LOG",
                                "sender": satellite_name,
                                "level": "INFO",
                                "message": f"Reacting to transition {new_state.lower()}",
                                "timestamp": timestamp
                            })
                            asyncio.create_task(
                                complete_transition_after_delay(sat_ref, satellite_id, satellite_name)
                            )

                        else:
                            await broadcast({
                                "type": "LOG",
                                "sender": satellite_name,
                                "level": "STATUS",
                                "message": f"New state: {current_state.upper()}",
                                "timestamp": timestamp
                            })
                        print(f"State changed: {satellite_name} -> {current_state}")

                    elif sat_ref:
                        # transition rejected — broadcast updated last_message + log
                        await broadcast({
                            "type": "SATELLITE_STATE_UPDATE",
                            "satellite_id": satellite_id,
                            "satellite_name": satellite_name,
                            "new_state": sat_ref.state(),
                            "last_message": sat_ref.last_message,
                            "timestamp": timestamp
                        })

                        await broadcast({
                            "type": "LOG",
                            "sender": "System",
                            "level": "WARNING",
                            "message": f"{satellite_name}: {sat_ref.last_message}",
                            "timestamp": timestamp
                        })
                        print(f"Rejected: {satellite_name} -> {sat_ref.last_message}")

            elif message_type == "OPERATOR_LOG":
                level = data.get("level")
                log_message = data.get("message")

                await broadcast({
                    "type": "LOG",
                    "sender": f"OP",
                    "level": level,
                    "message": log_message,
                    "timestamp": datetime.now(timezone.utc).strftime("%H:%M:%S")

                })

            elif message_type == "CHANGE_LOG_LEVEL":
                new_level = data.get("level", "ALL")
                client_log_levels[websocket] = new_level
                print(f"Client changed log level to {new_level}")

    except websockets.exceptions.ConnectionClosed:
        pass

    finally:
        connected_clients.remove(websocket)
        client_log_levels.pop(websocket, None)
        print("Client disconnected!")

async def main():
    asyncio.create_task(event_engine(system_satellites, broadcast))
    
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server running on ws://localhost:8765")
        await asyncio.Future() # forever

if __name__ == "__main__":
    asyncio.run(main())