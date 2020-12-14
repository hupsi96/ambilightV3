import logging

class RGB:

    def __init__ (self, strip):
        self.__strip = strip

    def entry(self, strip, msg):
        print("RGB: entry")

    def exit(self):
        print("RGB: exit")

    def redundant(self):
        print("No action required")

    def handleRequest(self, stateHandler, event, msg):
        print("RGB: handleRequest")

        if event.__class__.__name__ == "White": 
            stateHandler.setNewState(event)
        elif event.__class__.__name__ == "Off":
            stateHandler.setNewState(event)
        elif event.__class__.__name__ == "RGB":
            self.redundant()