import logging

class RGB:

    def __init__ (self, strip):
        self.__strip = strip

    def entry(self, strip, msg,stripStorage):
        print("RGB: entry")

    def exit(self):
        print("RGB: exit")

    def redundant(self):
        print("No action required")

    def handleRequest(self, stateHandler, event, msg,stripStorage):
        print("RGB: handleRequest")

        if event.__class__.__name__ == "White": 
            stateHandler.setNewState(event,msg)
        elif event.__class__.__name__ == "Off":
            stateHandler.setNewState(event,msg)
        elif event.__class__.__name__ == "RGB":
            self.redundant()