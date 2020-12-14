import paho.mqtt.client as mqtt
import logging
import time
import board
import neopixel
from multiprocessing import Process, Manager

from StateHandler import StateHandler
from States.Off import Off
from States.White import White
from States.RGB import RGB

manager = Manager()
managedRunning = manager.dict({'mqttRunning' : True})

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 58

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRBW

strip = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

white = White(strip)
rgb = RGB(strip)
off = Off(strip)
handler = StateHandler(strip,[white,rgb,off])

stripStorage = [(0,0,0,0,0)]*num_pixels #(r,g,b,w,brightness)

class mqtt_client:


    states = None
    #handler = None

    def __init__(self, states, strp):
        #Global Variables
        global managedRunning
        global strip
        global handler
        
        #own Variables
        self.states = states
        #self.strip = strp
        #self.handler = StateHandler(strp, states)
        
        #Testing
        self.test()
        
        
        try:
            #create Process
            p = Process(target=self.client.loop_forever)
            p.start()
            
            print("MQTT is started - waiting for further action")
            
            #leave main thread open untill mqtt is shutdown
            while managedRunning['mqttRunning']:
                time.sleep(1)
            
            #mqtt is required to shutdown -> proicess is terminated and joined
            print("Exited MQTT Server")
            p.terminate()
            p.join()

            print("Thread joined")
        except:
            p.terminate()
            p.join()
            print("ERROR: Error in mqtt process -> terminated process")

        #current Test status to leave main thread open after process termination - may be removed in future releases
        try:
            while True:
                print("Im still up and running")
                time.sleep(5)
        except:
            print("Exit Programm")
        
    def test(self):
        try:
            self.handler.handleRequest(White(self.strip))
            self.handler.handleRequest(RGB(self.strip))
            self.handler.handleRequest(Off(self.strip))
        except AttributeError:
            print("No Handler set - connot test class")
            
        
    #Setup MQTT:
                        
    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        #logging.info("Mqtt connection established - " +str(rc))
        
        print("MQTT is connected")
        client.subscribe("ambilightLamp/#")
        
        global strip
        global stripStorage
                
        strip.fill((255,63,0,100))
        
        for i in range(len(strip)):
                stripStorage[i] = (strip[i][0],strip[i][1],strip[i][2],strip[i][3],255)
                
        print("strip prepated")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        
        global managedRunning
        global strip
        global handler
        global white
        global rgb
        global off
        global stripStorage
        
        global stripStorage
        
        if msg.topic == "ambilightLamp/light/set" and str(msg.payload) == "b'OFF'":
            for i in range(len(strip)):
                stripStorage[i] = (strip[i][0],strip[i][1],strip[i][2],strip[i][3],stripStorage[i][4])
            
        
        print(msg.topic+" "+str(msg.payload))
        print(str(msg.payload))
        #if msg.topic == "ambilightLamp/off":
        #    managedRunning['mqttRunning'] = False
        stripStorageTransfer = [(0,0,0,0)]*len(strip)
        if msg.topic == "ambilightLamp/set/brightness":
            for i in range(len(strip)):
                current = stripStorage[i]
                current0 = int((float(current[0])/float(current[4])) * float(msg.payload))
                current1 = int((float(current[1])/float(current[4])) * float(msg.payload))
                current2 = int((float(current[2])/float(current[4])) * float(msg.payload))
                current = (current0,current1,current2,current[3])
                
                stripStorageTransfer[i] = (current[0],current[1],current[2],current[3])
                
            handler.handleRequest(rgb, msg, stripStorageTransfer, strip)
        elif msg.topic == "ambilightLamp/set/rgb":
            payload = str(msg.payload)[2:]
            payload = payload[:(len(payload)-1)]
            print(payload)
            input = tuple(map(int,str(payload).split(',')))
            print(input)
            
            for i in range(len(strip)):
                current0 = input [0]
                current1 = input [1]
                current2 = input [2]
                stripStorage[i] = (current0,current1,current2,stripStorage[i][3],stripStorage[i][4])
                
        elif msg.topic == "ambilightLamp/light/set":
            stripStorage[i] = (strip[i][0],strip[i][1],strip[i][2],strip[i][3],stripStorage[i][4])
            handler.handleRequest(off, strip, msg, stripStorageTransfer)
            
            
        
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect("192.168.178.73", 1883, 60) #Connect to HA IP Adress