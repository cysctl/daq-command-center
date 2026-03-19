from .fsm import FSM
from datetime import datetime

class Satellite:
    def __init__(self, id, name, type):
        # satellite informations
        self.id = id
        self.name = name
        self.type = type

        self.fsm = FSM()

        self.lives = 3
        self.last_message = "Awaiting"
        self.heartbeat = "3000ms"
        self.created_at = datetime.now().isoformat()

    
    def state(self):
        return self.fsm.current_state_value  # return current state
    

    def process_cmd(self, cmd):
        cmd = cmd.upper()
        try:
            old_state = self.state()
            transition_occurred = False
            
            if cmd == "INIT":
                if old_state == "new":
                    self.fsm.init_system()
                    transition_occurred = True

                elif old_state == "safe":
                    self.fsm.recover_safe()
                    transition_occurred = True

                elif old_state == "error":
                    self.fsm.recover_error()
                    transition_occurred = True

                elif old_state == "orbit":
                    self.fsm.reconfigure()
                    transition_occurred = True


            elif cmd == "ORBIT":
                if old_state == "init":
                    self.fsm.launch_system()
                    transition_occurred = True

                elif old_state == "run":
                    self.fsm.stop()
                    transition_occurred = True


            elif cmd == "RUN":
                if old_state == "orbit":
                    self.fsm.start()
                    transition_occurred = True

            elif cmd == "SAFE":
                if old_state in ["init", "orbit", "run"]:
                    self.fsm.rule_violated()
                    transition_occurred = True

            elif cmd == "ERROR":
                if old_state in ["init", "orbit", "run"]:
                    self.fsm.hardware_error()
                    transition_occurred = True

            if not transition_occurred:
                raise ValueError("Invalid FSM transition!")

            new_state = self.state()
            self.last_message = f"Transitioned to {new_state}"
            return True
        
        except Exception:
            self.last_message = "Invalid FSM transition!"
            return False

    def kill(self):
        if self.state() != "dead":
            self.fsm.connection_lost()
            self.lives = 0
            self.last_message = "Connection lost!"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "state": self.state(),
            "lives": self.lives,
            "last_message": self.last_message,
            "heartbeat": self.heartbeat
        }
    
    
# tests
if __name__ == "__main__":
    satellite = Satellite("", "", "")

    print(
        satellite.state() # except new
    )

    satellite.process_cmd("INIT") # new -> init

    print(
        satellite.state() # except init
    )

    satellite.process_cmd("ORBIT") # init -> orbit

    print(
        satellite.state() # except orbit
    )

    print(
        satellite.to_dict() # except {'id': '', 'name': '', 'type': '', 'state': 'orbit', 'lives': 3, 'last_message': 'Transitioned to orbit'}
    )

    satellite.kill() # any -> dead
    
    print(
        satellite.state()  # except dead
    )

    print(
        satellite.to_dict() # except {'id': '', 'name': '', 'type': '', 'state': 'dead', 'lives': 0, 'last_message': 'Connection lost!'}
    )