import logging

class RGB:
    strip = None
    def __init__ (self, strip):
        self.__strip = strip

    def entry(self, strip, msg,stripStorage):
        print("RGB: entry")

    def exit(self):
        print("RGB: exit")

    def redundant(self,msg,stripStorage,strip):
        print("No action required") #
        for i in range(len(stripStorage)):
            strip[i] = stripStorage[i]
        strip.show()
        

    def handleRequest(self, stateHandler, event, msg,stripStorage, strip):
        print("RGB: handleRequest")
        
        
        if event.__class__.__name__ == "White": 
            stateHandler.setNewState(event,msg,stripStorage,strip)
        elif event.__class__.__name__ == "Off":
            stateHandler.setNewState(event,msg,stripStorage,strip)
        elif event.__class__.__name__ == "RGB":
            self.redundant(msg,stripStorage,strip)
            
            #self.strip.fill((0,0,0,int(msg.payload)))
            #self.strip.show()