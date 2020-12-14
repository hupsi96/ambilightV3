from States.Off import Off
import logging

class StateHandler:

    currentState = None
    strip = None
    events = None

    def setNewState(self, state, msg,stripStorage):
        self.currentState.exit()
        self.currentState = state
        self.currentState.entry(self.strip,msg,stripStorage)

    def getCurrentState(self):
        return self.currentState

    def handleRequest(self,event, msg, stripStorage):
        self.currentState.handleRequest(self,event, msg, stripStorage)

    def __init__ (self, strip, events):
        self.strip = strip
        self.events = events
        self.currentState = Off(strip)