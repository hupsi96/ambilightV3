from States.Off import Off
import logging

class StateHandler:

    currentState = None
    strip = None
    events = None

    def setNewState(self, state, msg,stripStorage,strip):
        self.currentState.exit()
        self.currentState = state
        self.currentState.entry(strip,msg,stripStorage)

    def getCurrentState(self):
        return self.currentState

    def handleRequest(self,event, msg, stripStorage, strip):
        self.currentState.handleRequest(self,event, msg, stripStorage, strip)

    def __init__ (self, strip, events):
        self.strip = strip
        self.events = events
        self.currentState = Off(strip)