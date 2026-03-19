import asyncio
import websockets
import json
from datetime import datetime, timezone

from core.satellite import Satellite 
from simulation.engine import engine
from simulation.log_engine import log_engine

# clients
connected_clients = set()

# satellites
system_satellites = [
    # alpha-1 is enviro sensor. I will get temperature and pressure data from it
    Satellite("ALPHA-1", "Environment Monitor", "EnviroSensor"),

    # beta-2 is power supply. I will get voltage data from it
    Satellite("BETA-2", "Main Power Supply", "PowerSupply"),
]

async def broadcast(msg):
    # no clients
    if not connected_clients:
        return
    
    msg_as_json = json.dumps(msg)

    await asyncio.gather(*[client.send(msg_as_json) for client in connected_clients])

async def handler(websocket):
    print("New client connected!")
    connected_clients.add(websocket)

    # send all satellites to client
    await websocket.send(json.dumps({
        "type": "sync",
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
                new_state = data.get("new_state")
                
                success = False
                current_state = None
                current_last_message = None

                for sat in system_satellites:
                    if sat.id == satellite_id: # find correct satellite
                        success = sat.process_cmd(new_state) # process through fsm
                        current_state = sat.state()
                        current_last_message = sat.last_message
                        break
                
                if success:
                    await broadcast({
                        "type": "SATELLITE_STATE_UPDATE",
                        "satellite_id": satellite_id,
                        "new_state": current_state,
                        "last_message": current_last_message,
                        "timestamp": datetime.now(timezone.utc).strftime("%H:%M:%S")
                    })
                    print(f"State changed: {satellite_id} -> {current_state}")
                else:
                    print(f"Rejected: Invalid transition for {satellite_id} -> {new_state}")
                    await websocket.send(json.dumps({"error": "Invalid FSM transition"}))

    except websockets.exceptions.ConnectionClosed:
        pass

    finally:
        connected_clients.remove(websocket)
        print("Client disconnected!")

async def main():
    asyncio.create_task(engine(system_satellites, broadcast))
    asyncio.create_task(log_engine(system_satellites, broadcast))
    
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server running on ws://localhost:8765")
        await asyncio.Future() # forever

if __name__ == "__main__":
    asyncio.run(main())