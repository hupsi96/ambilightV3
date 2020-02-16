from States.Off import Off
import logging

class StateHandler:

    currentState = None
    strip = None
    events = None

    def setNewState(self, state):
        self.currentState.exit()
        self.currentState = state
        self.currentState.entry(self.strip)

    def getCurrentState(self):
        return self.currentState

    def handleRequest(self,event):
        self.currentState.handleRequest(self,event)

    def __init__ (self, strip, events):
        self.strip = strip
        self.events = events
        self.currentState = Off(strip)
