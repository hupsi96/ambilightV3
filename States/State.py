class State:
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object (stateHandler.py),
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """
    strip = None

    def handleRequest(self, stateHandler, event, msg, stripStorage, strip):
        pass

    def entry(self, strip, msg, stripStorage):
        pass

    def exit(self):
        pass


