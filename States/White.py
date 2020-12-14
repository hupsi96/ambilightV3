import logging

class White:
    strip = None
    def __init__ (self, strip):
        self.strip = strip

    def entry(self, strip, msg,stripStorage):
        while True:
            self.rainbow_cycle(0.003)
        print("White: entry")

    def exit(self):
        print("White: exit")

    def redundant(self):
        print("No action required")


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
        #self.strip.fill((0,0,0,255))
        #self.strip.show()
        
        #self.strip.fill((0,0,0,int(msg.payload)))
        #self.strip.show()
        print("White: handleRequest")

        if event.__class__.__name__ == "RGB":
            stateHandler.setNewState(event,msg,stripStorage,strip)
        elif event.__class__.__name__ == "Off":
            stateHandler.setNewState(event,msg,stripStorage,strip)
        elif event.__class__.__name__ == "White":
            self.redundant()