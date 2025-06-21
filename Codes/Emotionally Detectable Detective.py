import cv2
import numpy as np
from tensorflow.keras.models import load_model as lm #type: ignore
from keras.preprocessing.image import img_to_array as ita
fc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
em = lm("emotion_model.h5")
el = ["Angry","Disgust","Fear","Happy","Sad","Surprise","Neutral"]
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
        rg = g[y:y+h,x:x+w]
        rc = f[y:y+h,x:x+w]
        rr = cv2.resize(rg,(48,48))
        rr = rr.astype("float32")/255
        rr = ita(rr)
        rr = np.expand_dims(rr,axis = 0)
        ep = em.predict(rr)
        mi = np.argmax(ep[0])
        pe = el[mi]
        cv2.putText(f,pe,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
    cv2.imshow("Face & Emotion Detection",f)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Exiting...")
        break
c.release()
cv2.destroyAllWindows()