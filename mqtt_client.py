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

stripStorage = [(0,0,0,0)]*num_pixels

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
                stripStorage[i] = strip[i]
                
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
                stripStorage[i] = strip[i]
            
        
        print(msg.topic+" "+str(msg.payload))
        print(str(msg.payload))
        #if msg.topic == "ambilightLamp/off":
        #    managedRunning['mqttRunning'] = False
        if msg.topic == "ambilightLamp/set/brightness":
            for i in range(len(strip)):
                current = stripStorage[i]
                print(int(msg.payload))
                print(current[i])
                print(current[i][0])
                print(float(current[i][0]))
                current[i][0] = int(float(current[i][0]) * (float(msg.payload) /255.0))
                current[i][1] = int(float(current[i][1]) * (float(msg.payload) /255.0))
                current[i][2] = int(float(current[i][2]) * (float(msg.payload) /255.0))
                
            handler.handleRequest(rgb,msg,stripStorage)
        elif msg.topic == "ambilightLamp/set/rgb":
            print("rgb")
        #    if self.handler.getCurrentState() 
            
        
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect("192.168.178.73", 1883, 60) #Connect to HA IP Adress