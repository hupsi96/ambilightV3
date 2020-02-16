#Has a strip
#Has a mqtt (strip)
from States.Off import Off
from States.White import White
from States.RGB import RGB

from mqtt_client import mqtt_client
import logging

def main():
    #logging.basicConfig(LogFileName='ambilight.log', LogFileMode='w', logLevel=logging.DEBUG, logFormat='%(asctime)s - %(levelname)s: %(message)s', logdatefmt='%d.%m.%y %I:%M:%S %p')
    #logging.info('Main programm started')
    strip = "test"
    print("python main function")

    #define States
    white = White(strip)
    rgb = RGB(strip)
    off = Off(strip)
    
    mqtt_client_instance = mqtt_client([white,rgb,off],strip)

if __name__ == '__main__':
    main()