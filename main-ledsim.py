# run this file to test the led matrix simulation with predetermined LEDs turned on
from surveillance import *
from virtualLED import *

leds = LedArray(12,6)
ledchange = np.zeros(shape=72)
ledchange[15]=1
ledchange[18]=1
ledchange[67]=1
ledchange[56]=1
ledchange[51]=1
ledchange[65]=1
ledchange[66]=1

while True:
    
    leds.LEDs[:]=0
    leds.plot_leds()
    leds.LEDs = leds.LEDs+ledchange
    leds.graphUpdate(leds.LEDs,1)
    
    leds.LEDs[:]=0
    leds.graphUpdate(leds.LEDs,1)

