from surveillance import *
from virtualLED import *

cap = cv2.VideoCapture(0)
leds = LedArray(12,6)
ledchange = np.zeros(shape=72)
camera = Camera(cap)
while True:
    leds.LEDs[:]=0
    leds.plot_leds()
    ledchange[2]=1
    ledchange[5]=1
    ledchange[6]=0
    ledchange[8]=0
    leds.LEDs = leds.LEDs+ledchange
    leds.graphUpdate(leds.LEDs,1)
    # leds.plot.canvas.tight_layout()
    # leds.plot.canvas.show(block=False)
    
    leds.LEDs[:]=0
    ledchange[6]=1
    ledchange[8]=1
    ledchange[2]=0
    ledchange[5]=0
    leds.LEDs = leds.LEDs+ledchange
    leds.graphUpdate(leds.LEDs,1)

    #camera.camera_on()
    # leds.plot.canvas.tight_layout()
    # leds.plot.canvas.show(block=False)

    # if cv2.waitKey(1)==ord('q'):
    #     break

# cap.release()
cv2.destroyAllWindows()
