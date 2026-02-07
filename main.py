from surveillance import *
from virtualLED import *

cap = cv2.VideoCapture(0)
camera = Camera(cap)
camera.camera_on()
