#Has a strip
#Has a mqtt (strip)
from States.Off import Off
from States.White import White
from States.RGB import RGBW

import board
import neopixel
import time

from mqtt_client import mqtt_client
import logging

def main():
    #logging.basicConfig(LogFileName='ambilight.log', LogFileMode='w', logLevel=logging.DEBUG, logFormat='%(asctime)s - %(levelname)s: %(message)s', logdatefmt='%d.%m.%y %I:%M:%S %p')
    #logging.info('Main programm started')
    
    print("python main function")

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
    #test Strips
    strip.fill((255,0,0,0))
    strip.show()
    time.sleep(2)
    strip.fill((0,0,0,0))
    strip.show()
    
    
    #define States
    white = White(strip)
    rgbw = RGBW(strip)
    off = Off(strip)
    
    mqtt_client_instance = mqtt_client([white,rgbw,off],strip)

if __name__ == '__main__':
    main()