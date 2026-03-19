import asyncio
import random
from datetime import datetime, timezone

async def log_engine(satellites, callback):
    while True:
        await asyncio.sleep(random.uniform(2.0, 5.0))
        
        active_sats = [sat for sat in satellites if sat.state() not in ["new", "dead"]]
        
        if not active_sats:
            continue

        sat = random.choice(active_sats)
        state = sat.state()
        
        if state == "error":
            level = random.choices(["INFO", "WARN", "ERROR"], weights=[20, 40, 40])[0]
        elif state == "safe":
            level = random.choices(["INFO", "WARN", "ERROR"], weights=[50, 40, 10])[0]
        elif state in ["init", "orbit"]:
            level = random.choices(["INFO", "WARN", "ERROR"], weights=[70, 20, 10])[0]
        else:
            level = random.choices(["INFO", "WARN", "ERROR"], weights=[85, 12, 3])[0]

        # AI was used as a tool
        messages = {
            "init": {
                "INFO": [
                    "Boot sequence initiated.",
                    "Calibrating onboard sensors...",
                    "Self-test diagnostic passed.",
                    "Establishing preliminary ground link.",
                    "Power management subsystem online."
                ],
                "WARN": [
                    "Slight voltage fluctuation during boot.",
                    "Sensor calibration took longer than expected.",
                    f"Subsystem '{sat.type}' initialization delayed."
                ],
                "ERROR": [
                    "Failed to initialize primary communication module!",
                    "Memory self-test encountered a parity error in block 0xA1."
                ]
            },
            "orbit": {
                "INFO": [
                    "Orbit stabilization in progress.",
                    "Solar panel array deployed optimally.",
                    "Star tracker locked onto constellation.",
                    "Payload thermal controls stabilized."
                ],
                "WARN": [
                    "Minor trajectory deviation corrected.",
                    "Solar panel efficiency slightly below nominal.",
                    "Thermal delta detected on sun-facing side."
                ],
                "ERROR": [
                    "Attitude control thruster misfire!",
                    "Temporary loss of star tracker lock."
                ]
            },
            "run": {
                "INFO": [
                    f"Processing {sat.type} payload data.",
                    "Data block synchronized and buffered.",
                    "Heartbeat acknowledged; all systems nominal.",
                    "Routine telemetry packet transmitted.",
                    "Executing automated task sequence."
                ],
                "WARN": [
                    f"High latency detected on internal bus.",
                    f"Buffer usage approaching {random.randint(75, 95)}%.",
                    "Minor packet drop compensated via FEC.",
                    f"Internal temperature elevated to {random.uniform(35.0, 45.0):.1f}°C."
                ],
                "ERROR": [
                    f"Checksum mismatch in data block {hex(random.randint(0x1000, 0xFFFF))}!",
                    "Sensor timeout occurred. Attempting recovery sequence...",
                    "Buffer overflow prevented! Partial data loss logged."
                ]
            },
            "safe": {
                "INFO": [
                    "Running in low-power safe mode.",
                    "Non-essential subsystems disabled.",
                    "Awaiting further ground commands.",
                    "Basic telemetry successfully transmitted."
                ],
                "WARN": [
                    f"Battery charge level low at {random.randint(15, 30)}%.",
                    "Safe mode duration exceeding expected nominal limits.",
                    "Redundant systems on standby under safe config."
                ],
                "ERROR": [
                    "Critical power failure imminent in safe mode!",
                    "Unable to establish reliable link in safe configuration."
                ]
            },
            "error": {
                "INFO": [
                    "Diagnostic mode engaged.",
                    "Collecting crash dump data for downlink.",
                    "Attempting automated fault isolation.",
                    "Rebooting affected subsystems."
                ],
                "WARN": [
                    "Multiple initialization retry attempts failed.",
                    "Secondary fault detected in power routing.",
                    "Diagnostic data indicates progressive hardware degradation."
                ],
                "ERROR": [
                    "Catastrophic subsystem failure!",
                    "Automated recovery sequence aborted. Manual intervention required.",
                    "Persistent loss of payload control!"
                ]
            }
        }

        state_dict = messages.get(state, messages["run"])
        message_list = state_dict.get(level, messages["run"][level])
        message_text = random.choice(message_list)

        log_data = {
            "type": "LOG",
            "sender": sat.name,
            "level": level,
            "message": message_text,
            "timestamp": datetime.now(timezone.utc).strftime("%H:%M:%S")
        }

        await callback(log_data)

        if level == "ERROR" and state in ["init", "orbit", "run"]:
            try:
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
                    "message": f"Satellite {sat.name} state changed to ERROR due to critical fault",
                    "timestamp": timestamp
                })
            except ValueError:
                pass