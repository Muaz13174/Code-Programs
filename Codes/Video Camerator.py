import cv2
import cv2.data
fc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
c = cv2.VideoCapture(0)
if not c.isOpened():
    print("Error : Could Not Open Camera")
    exit()
while 1:
    r,f = c.read()
    if not r:
        print("Error : Failed To Capture Image")
        break
    g = cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    fcs = fc.detectMultiScale(f,scaleFactor = 1.1,minNeighbors = 5,minSize = (30,30))
    for (x,y,w,h) in fcs:
        cv2.rectangle(f,(x,y),(x + w,y+ h),(255,0,0),2)
    cv2.imshow("Face Detection - Press Q to quit",f)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Exiting...")
        break
c.release()
cv2.destroyAllWindows()