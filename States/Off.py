import logging

class Off:
    strip = None
    def __init__ (self, strip):
        self.__strip = strip

    def entry(self, strip, msg,stripStorage):
        strip.fill((0,0,0,0))
        strip.show()
        print("Off: entry")

    def exit(self):
        print("Off: exit")

    def redundant(self):
        print("No action required")

    def handleRequest(self, stateHandler, event, msg, stripStorage, strip):
        print("Off: handleRequest")
        
        if event.__class__.__name__ == "White": 
            stateHandler.setNewState(event,msg, stripStorage,strip)
        elif event.__class__.__name__ == "RGB":
            stateHandler.setNewState(event, msg, stripStorage,strip)
        elif event.__class__.__name__ == "Off":
            self.redundant()
        