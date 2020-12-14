import logging

class White:

    def __init__ (self, strip):
        self.__strip = strip

    def entry(self, strip):
        print("White: entry")

    def exit(self):
        print("White: exit")

    def redundant(self):
        print("No action required")

    def handleRequest(self, stateHandler, event):
        self.strip.fill(0,0,0,255)
        self.strip.show()
        print("White: handleRequest")

        if event.__class__.__name__ == "RGB":
            stateHandler.setNewState(event)
        elif event.__class__.__name__ == "Off":
            stateHandler.setNewState(event)
        elif event.__class__.__name__ == "White":
            self.redundant()