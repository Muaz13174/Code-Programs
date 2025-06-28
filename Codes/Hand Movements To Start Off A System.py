import cv2
import numpy as np
c = cv2.VideoCapture(0)
if not c.isOpened():
    print("Error : Could Not Open Webcam")
    quit()
while 1:
    r,f = c.read()
    if not r:
        print("Error : Failed To Capture Image")
        break
    hsv = cv2.cvtColor(f,cv2.COLOR_BGR2HSV)
    ls = np.array([0,20,70],np.uint8)
    us = np.array([20,255,255],np.uint8)
    m = cv2.inRange(hsv,ls,us)
    result = cv2.bitwise_and(f,f,mask = m)
    cts,_ = cv2.findContours(m,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if cts:
        mxct = max(cts,key = cv2.contourArea)
        if cv2.contourArea(mxct) > 500:
            x,y,w,h = cv2.boundingRect(mxct)
            cv2.rectangle(f,(x,y),(x+w,y+h),(0,255,0),2)
            cx = int(x+w/2)
            cy = int(y+h/2)
            cv2.circle(f,(cx,cy),5,(0,0,255),-1)
    cv2.imshow("Original Frame",f)
    cv2.imshow("Filtered Frame",result)
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break
c.release()
cv2.destroyAllWindows()