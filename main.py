# run this file to test the camera and LED simulation simultaneously
from surveillance import *
from virtualLED import *
import time

cap = cv2.VideoCapture(0)
leds = LedArray(12,6)
ledchange = np.zeros(shape=72)
camera = Camera(cap)
end_time = time.time() + 10.0

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
    leds.LEDs = leds.LEDs+turnonleds
    leds.graphUpdate(leds.LEDs,.1)


