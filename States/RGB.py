import logging
import neopixel
import time

class RGB:
    strip = None
    def __init__ (self, strip):
        self.__strip = strip

    def entry(self, strip, msg,stripStorage):
        print("RGB: entry")
        #TODO: implement starting animation
        for i in range(len(stripStorage)):
            strip[i] = stripStorage[i]
        strip.show()

    def exit(self):
        print("RGB: exit")

    def redundant(self,msg,stripStorage,strip):
        print("No action required") 
        #TODO: implement fade
        for i in range(len(stripStorage)):
            strip[i] = stripStorage[i]
        strip.show()
        #while True:
        #    self.rainbow_cycle(0.005,strip)

    def handleRequest(self, stateHandler, event, msg,stripStorage, strip):
        print("RGB: handleRequest")
        
        
        if event.__class__.__name__ == "White": 
            stateHandler.setNewState(event,msg,stripStorage,strip)
        elif event.__class__.__name__ == "Off":
            stateHandler.setNewState(event,msg,stripStorage,strip)
        elif event.__class__.__name__ == "RGB":
            self.redundant(msg,stripStorage,strip)
            