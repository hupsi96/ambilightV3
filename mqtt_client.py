import paho.mqtt.client as mqtt
import errno
from socket import error as socket_error
import logging
import time
import threading

from StateHandler import StateHandler
from States.Off import Off
from States.White import White
from States.RGB import RGB

class mqtt_client:

    states = None
    strip = None
    handler = None

    def __init__(self, states, strip):
        self.states = states
        self.strip = strip
        self.handler = StateHandler(strip, states)
        
        self.test()
        
        running = True
        try:
            t = threading.Thread(target=self.client.loop_forever,name='mqttAerver')
            t.daemon = True
            t.start()
            print("MQTT is started - waiting for further action")
            while running:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Forced Shutdown - Threat joined")
            t.join()
        except:
            t.join()
            print("Threat joined")
        
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
        print("Connected")
        client.subscribe("state")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        

    # The callback for when a PUBLISH message is received from the server.
    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))    
        
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect("127.0.0.1", 1883, 60)