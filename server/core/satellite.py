from .fsm import FSM
from datetime import datetime

# maps transitional states to their completion method names
TRANSITION_COMPLETIONS = {
    "initializing": "initialized",
    "launching": "launched",
    "landing": "landed",
    "reconfiguring": "reconfigured",
    "starting": "started",
    "stopping": "stopped",
}

class Satellite:
    def __init__(self, id, name, type):
        # satellite informations
        self.id = id
        self.name = name
        self.type = type

        self.fsm = FSM()

        self.lives = 3
        self.last_message = "Awaiting"
        self.last_message_time = "-"
        self.heartbeat = "3000ms"
        self.created_at = datetime.now().isoformat()


    def state(self):
        return self.fsm.current_state_value  # return current state

    def is_transitioning(self):
        return self.state() in TRANSITION_COMPLETIONS

    def process_cmd(self, cmd):
        cmd = cmd.upper()
        try:
            old_state = self.state()
            transition_occurred = False

            if cmd == "INITIALIZE":
                if old_state == "new":
                    self.fsm.initialize()
                    transition_occurred = True

            elif cmd == "LAUNCH":
                if old_state == "init":
                    self.fsm.launch()
                    transition_occurred = True

            elif cmd == "LAND":
                if old_state == "orbit":
                    self.fsm.land()
                    transition_occurred = True

            elif cmd == "RECONFIGURE":
                if old_state == "orbit":
                    self.fsm.reconfigure()
                    transition_occurred = True

            elif cmd == "START":
                if old_state == "orbit":
                    self.fsm.start()
                    transition_occurred = True

            elif cmd == "STOP":
                if old_state == "run":
                    self.fsm.stop()
                    transition_occurred = True

            elif cmd == "RECOVER":
                if old_state == "safe":
                    self.fsm.recover_safe()
                    transition_occurred = True
                elif old_state == "error":
                    self.fsm.recover_error()
                    transition_occurred = True

            elif cmd == "SAFE":
                if old_state in ["init", "orbit", "run"]:
                    self.fsm.rule_violated()
                    transition_occurred = True

            elif cmd == "ERROR":
                if old_state in ["init", "orbit", "run"]:
                    self.fsm.hardware_error()
                    transition_occurred = True

            elif cmd == "SHUTDOWN":
                if old_state != "dead":
                    self.fsm.connection_lost()
                    self.lives = 0
                    transition_occurred = True

            if not transition_occurred:
                raise ValueError("Invalid FSM transition!")

            new_state = self.state()
            self.last_message = f"Transitioned to {new_state}"
            self.last_message_time = datetime.now().strftime("%H:%M:%S")
            return True

        except Exception:
            self.last_message = "Invalid FSM transition!"
            self.last_message_time = datetime.now().strftime("%H:%M:%S")
            return False

    def complete_transition(self):
        """Complete a transitional state (e.g. initializing -> INIT)."""
        current = self.state()
        method_name = TRANSITION_COMPLETIONS.get(current)
        if method_name:
            getattr(self.fsm, method_name)()
            new_state = self.state()
            self.last_message = f"Transitioned to {new_state}"
            self.last_message_time = datetime.now().strftime("%H:%M:%S")
            return True
        return False

    def kill(self):
        if self.state() != "dead":
            self.fsm.connection_lost()
            self.lives = 0
            self.last_message = "Connection lost!"
            self.last_message_time = datetime.now().strftime("%H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "state": self.state(),
            "lives": self.lives,
            "last_message": self.last_message,
            "last_message_time": self.last_message_time,
            "heartbeat": self.heartbeat
        }
