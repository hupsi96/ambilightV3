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
        while True:
            self.rainbow_cycle(0.005,strip)
        
    ### TEST
    def wheel(self, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b,0)
 
 
    def rainbow_cycle(self,wait,strip):
        for j in range(255):
            for i in range(len(strip)):
                pixel_index = (i * 256 // len(strip)) + j
                strip[i] = self.wheel(pixel_index & 255)
            strip.show()
            time.sleep(wait)
        

    def handleRequest(self, stateHandler, event, msg,stripStorage, strip):
        print("RGB: handleRequest")
        
        
        if event.__class__.__name__ == "White": 
            stateHandler.setNewState(event,msg,stripStorage,strip)
        elif event.__class__.__name__ == "Off":
            stateHandler.setNewState(event,msg,stripStorage,strip)
        elif event.__class__.__name__ == "RGB":
            self.redundant(msg,stripStorage,strip)