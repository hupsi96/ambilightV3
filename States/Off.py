import logging

class Off:

    def __init__ (self, strip):
        self.__strip = strip

    def entry(self, msg,stripStorage):
        print("Off: entry")

    def exit(self):
        print("Off: exit")

    def redundant(self):
        print("No action required")

    def handleRequest(self, stateHandler, event, msg, stripStorage):
        print("Off: handleRequest")
        
        if event.__class__.__name__ == "White": 
            stateHandler.setNewState(event,msg, stripStorage)
        elif event.__class__.__name__ == "RGB":
            stateHandler.setNewState(event, msg, stripStorage)
        elif event.__class__.__name__ == "Off":
            self.redundant()
        