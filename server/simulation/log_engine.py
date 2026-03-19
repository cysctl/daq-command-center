import asyncio
import random
from datetime import datetime, timezone

async def log_engine(satellites, callback):
    while True:
        await asyncio.sleep(random.uniform(2.0, 5.0))
        
        active_sats = [sat for sat in satellites if sat.state() not in ["new", "dead"]]
        
        if not active_sats:
            continue

        # random satellite
        sat = random.choice(active_sats)
        
        # random level selection
        level = random.choices(["INFO", "WARN", "ERROR"], weights=[80, 15, 5])[0]
        
        # mock messages
        # this messages created by AI
        messages = {
            "INFO": [
                "Event block processed successfully.",
                "Buffer synchronization complete.",
                "Heartbeat acknowledged.",
                "Data link stable."
            ],
            "WARN": [
                "High latency detected on internal bus.",
                "Buffer usage approaching 80%.",
                "Minor packet drop compensated.",
                "Temperature delta detected."
            ],
            "ERROR": [
                "Checksum mismatch in event payload!",
                "Sensor timeout. Attempting recovery...",
                "Buffer overflow prevented! Data loss possible."
            ]
        }

        message_text = random.choice(messages[level])

        log_data = {
            "type": "LOG",
            "sender": sat.name,
            "level": level,
            "message": message_text,
            "timestamp": datetime.now(timezone.utc).strftime("%H:%M:%S")
        }

        await callback(log_data)

        # if ERROR log then transition satellite to ERROR state
        if level == "ERROR" and sat.state() in ["init", "orbit", "run"]:
            sat.process_cmd("ERROR")
            timestamp = datetime.now(timezone.utc).strftime("%H:%M:%S")
            await callback({
                "type": "SATELLITE_STATE_UPDATE",
                "satellite_id": sat.id,
                "new_state": sat.state(),
                "last_message": sat.last_message,
                "timestamp": timestamp
            })
            await callback({
                "type": "LOG",
                "sender": "SYSTEM",
                "level": "INFO",
                "message": f"Satellite {sat.id} state changed to ERROR",
                "timestamp": timestamp
            })