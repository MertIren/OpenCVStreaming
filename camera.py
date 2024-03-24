import requests
import cv2

cap = cv2.VideoCapture(0)

scale : int = 0.75

while True:
    success, img = cap.read()
    img = cv2.resize(img, (0, 0), fx=scale, fy = scale)

    if success:    
        # cv2.imshow("OUTPUT", img)
        
        _, imdata = cv2.imencode('.JPG', img)

        print('.', end='', flush=True)

        requests.put('http://127.0.0.1:5000/upload', data=imdata.tobytes())
    
    if cv2.waitKey(40) == 27:  # 40ms = 25 frames per second (1000ms/40ms) 
        break

    time.sleep(0.04)

cv2.destroyAllWindows()
cap.release()
