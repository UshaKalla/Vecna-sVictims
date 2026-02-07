# run this file to test the camera and red masking function
from surveillance import *

cap = cv2.VideoCapture(0)
camera = Camera(cap)

while True:
    camera.camera_on()

    if cv2.waitKey(1)==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
    

