from statemachine import State, StateMachine

class FSM(StateMachine):

    # states
    new = State(name="NEW", initial=True)
    init = State(name="INIT")
    orbit = State(name="ORBIT")
    run = State(name="RUN")
    safe = State(name="SAFE")
    error = State(name="ERROR")
    # transitional states
    initializing = State(name="initializing")
    launching = State(name="launching")
    landing = State(name="landing")
    reconfiguring = State(name="reconfiguring")
    starting = State(name="starting")
    stopping = State(name="stopping")


    # initialize: NEW -> initializing -> INIT
    initialize = new.to(initializing)
    initialized = initializing.to(init)

    # launch: INIT -> launching -> ORBIT
    launch = init.to(launching)
    launched = launching.to(orbit)

    # land: ORBIT -> landing -> INIT
    land = orbit.to(landing)
    landed = landing.to(init)

    # reconfigure: ORBIT -> reconfiguring -> ORBIT
    reconfigure = orbit.to(reconfiguring)
    reconfigured = reconfiguring.to(orbit)

    # start: ORBIT -> starting -> RUN
    start = orbit.to(starting)
    started = starting.to(run)

    # stop: RUN -> stopping -> ORBIT
    stop = run.to(stopping)
    stopped = stopping.to(orbit)

    rule_violated = run.to(safe) | orbit.to(safe) | init.to(safe)
    recover_safe = safe.to(init)
    hardware_error = run.to(error) | orbit.to(error) | init.to(error)
    recover_error = error.to(init)

