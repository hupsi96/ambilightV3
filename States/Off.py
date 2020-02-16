import logging

class Off:

    def __init__ (self, strip):
        self.__strip = strip

    def entry(self, strip):
        print("Off: entry")

    def exit(self):
        print("Off: exit")

    def redundant(self):
        print("No action required")

    def handleRequest(self, stateHandler, event):
        print("Off: handleRequest")
        
        if event.__class__.__name__ == "White": 
            stateHandler.setNewState(event)
        elif event.__class__.__name__ == "RGB":
            stateHandler.setNewState(event)
        elif event.__class__.__name__ == "Off":
            self.redundant()
        