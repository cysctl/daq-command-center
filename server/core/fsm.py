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

    # transitional states
    initializing = State(name="initializing")
    launching = State(name="launching")
    landing = State(name="landing")
    reconfiguring = State(name="reconfiguring")
    starting = State(name="starting")
    stopping = State(name="stopping")


    # initialize: NEW -> initializing -> INIT
    initialize = new.to(initializing)
    _initialized = initializing.to(init)

    # launch: INIT -> launching -> ORBIT
    launch = init.to(launching)
    _launched = launching.to(orbit)

    # land: ORBIT -> landing -> INIT
    land = orbit.to(landing)
    _landed = landing.to(init)

    # reconfigure: ORBIT -> reconfiguring -> ORBIT
    reconfigure = orbit.to(reconfiguring)
    _reconfigured = reconfiguring.to(orbit)

    # start: ORBIT -> starting -> RUN
    start = orbit.to(starting)
    _started = starting.to(run)

    # stop: RUN -> stopping -> ORBIT
    stop = run.to(stopping)
    _stopped = stopping.to(orbit)

    rule_violated = run.to(safe) | orbit.to(safe) | init.to(safe)
    recover_safe = safe.to(init)
    hardware_error = run.to(error) | orbit.to(error) | init.to(error)
    recover_error = error.to(init)

    connection_lost = (
        new.to(dead) | init.to(dead) | orbit.to(dead) |
        run.to(dead) | safe.to(dead) | error.to(dead)
    )

    # transitional states
    def on_enter_initializing(self):
        self._initialized()

    def on_enter_launching(self):
        self._launched()

    def on_enter_landing(self):
        self._landed()

    def on_enter_reconfiguring(self):
        self._reconfigured()

    def on_enter_starting(self):
        self._started()

    def on_enter_stopping(self):
        self._stopped()