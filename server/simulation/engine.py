import asyncio
import random
from datetime import datetime, timezone

# each satellite type has its own data generator
GENERATORS = {
    "EnviroSensor": lambda: {
        "temperature": round(random.uniform(22.0, 23.5), 2), # rand mock data
        "pressure": round(random.uniform(1010.0, 1015.0), 1), # rand mock data
    },
    "PowerSupply": lambda: {
        "voltage": round(random.uniform(4.9, 5.1), 2), # rand mock data
    },
}

async def engine(satellites, callback):
    while True:
        await asyncio.sleep(1)

        for satellite in satellites:
            if satellite.state() != "run":
                continue

            generator = GENERATORS.get(satellite.type)
            if not generator:
                continue

            await callback({
                "type": "TELEMETRY",
                "satellite_id": satellite.id,
                "metrics": generator(),
                "timestamp": datetime.now(timezone.utc).strftime("%H:%M:%S"),
            })