from statemachine import State, StateMachine

class FSM(StateMachine):

    # states
    new = State(name="NEW", initial=True)
    init = State(name="INIT")
    orbit = State(name="ORBIT")
    run = State(name="RUN")
    safe = State(name="SAFE")
    error = State(name="ERROR")
    dead = State(name="DEAD", final=True)

    # transitions
    init_system = new.to(init)
    launch_system = init.to(orbit)
    start = orbit.to(run)
    stop = run.to(orbit)
    reconfigure = orbit.to(init)

    rule_violated = run.to(safe) | orbit.to(safe) | init.to(safe)
    recover_safe = safe.to(init)

    hardware_error = run.to(error) | orbit.to(error) | init.to(error)
    recover_error = error.to(init)

    connection_lost = new.to(dead) | init.to(dead) | orbit.to(dead) | run.to(dead) | safe.to(dead) | error.to(dead)
