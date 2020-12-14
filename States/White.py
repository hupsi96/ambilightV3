import logging

class White:
    strip = None
    def __init__ (self, strip):
        self.strip = strip

    def entry(self, strip, msg):
        print("White: entry")

    def exit(self):
        print("White: exit")

    def redundant(self):
        print("No action required")

    def handleRequest(self, stateHandler, event, msg):
        self.strip.fill((0,0,0,255))
        self.strip.show()
        
        self.strip.fill((0,0,0,int(msg.payload)))
        self.strip.show()
        print("White: handleRequest")

        if event.__class__.__name__ == "RGBW":
            stateHandler.setNewState(event,msg)
        elif event.__class__.__name__ == "Off":
            stateHandler.setNewState(event,msg)
        elif event.__class__.__name__ == "White":
            self.redundant()