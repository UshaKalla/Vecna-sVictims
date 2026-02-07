from surveillance import *
from virtualLED import *
import time

cap = cv2.VideoCapture(0)
leds = LedArray(12,6)
ledchange = np.zeros(shape=72)
camera = Camera(cap)
end_time = time.time() + 10.0

# cap.release()
# cv2.destroyAllWindows()

def move_figure(f, x, y):
    f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))

while True:
    camera.camera_on()
    cv2.moveWindow('masking', 1000, 100)
    if cv2.waitKey(1)==ord('q'):
        break
    
    w = camera.cam_width
    h = camera.cam_height
    led_on=camera.scale_mask(w,h,12,6,camera.redmask)
    turnonleds=led_on.flatten()

    leds.LEDs[:]=0
    # ledchange[2]=1
    # ledchange[5]=1
    # ledchange[6]=0
    # ledchange[8]=0
    leds.LEDs = leds.LEDs+turnonleds
    leds.graphUpdate(leds.LEDs,.1)
    # leds.plot.canvas.tight_layout()
    # leds.plot.canvas.show(block=False)
    
    # leds.LEDs[:]=0
    # ledchange[6]=1
    # ledchange[8]=1
    # ledchange[2]=0
    # ledchange[5]=0
    # leds.LEDs = leds.LEDs+ledchange
    # leds.graphUpdate(leds.LEDs,1)

    #camera.camera_on()
    # leds.plot.canvas.tight_layout()
    # leds.plot.canvas.show(block=False)
    

