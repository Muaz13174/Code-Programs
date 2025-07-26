import cv2
import mediapipe as mp
import os
import time as t
import numpy as np
c = cv2.VideoCapture()
c.set(3,640)
c.set(4,1000)
c.set(10,150)
mph = mp.solutions.hands
hnd = mph.Hands()
mpd = mp.solutions.drawing_utils
pt = 0
folder = "Outputs"
myl = os.listdir(folder)
ovl = []
col = (0,0,255)
for i in myl:
    img = cv2.imread(fr"{folder}\{i}")
    print(img.shape)
    ovl.append(img)
hd = ovl[0]
print(myl)
xp,yp = 0,0
canvas = np.zeros((480,640,3),np.uint8)
while 1:
    s,f = c.read()
    f = cv2.flip(f,1)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    r = hnd.process(img)
    lm = []
    if r.multi_hand_landmarks:
        for hn in r.multi_hand_landmarks:
            for id,lnm in enumerate(hn.landmark):
                h,w,cl = f.shape
                cx,cy = int(lnm.x * w),int(lnm.y * h)
                lm.append([id,cx,cy])
            mpd.draw_landmarks(f,hn,mph.HandLandmark)
    if len(lm) != 0:
        x1,y1 = lm[8][1],lm[8][2]
        x2,y2 = lm[12][1],lm[12][2]
        if lm[8][2] < lm[6][2] and lm[12][2] < lm[10][2]:
            xp,yp = 0,0
            print("Selection Mode")
            if y1 < 100:
                if 71 < x1 < 142:
                    hd = ovl[7]
                    col = (0,0,0)
                elif 142 < x1 < 213:
                    hd = ovl[6]
                    col = (226,43,138)
            cv2.rectangle(f,(x1,y1),(x2,y2),col,-1)
        elif lm[8][2] < lm[6][2]:
            if xp == 0 and yp == 0:
                xp,yp = x1,y1
            if col == (0,0,0):
                cv2.line(f,(xp,yp),(x1,y1),col,100,-1)
                cv2.line(canvas,(xp,yp),(x1,y1),col,100,-1)
            cv2.line(f,(xp,yp),(x1,y1),col,25,-1)
            cv2.line(canvas,(xp,yp),(x1,y1),col,25,-1)
            print("Drawing Mode")
            xp,yp = x1,y1
    gimg = cv2.cvtColor(canvas,cv2.COLOR_BGR2GRAY)
    _,imgInv = cv2.threshold(gimg,50.0,255.0,cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    f = cv2.bitwise_and(f,imgInv)
    f = cv2.bitwise_or(f,canvas)
    f[0:100,0:640] = hd
    ct = t.time()
    fps = 1/(ct - pt)
    cv2.putText(f,f"FPS : {int(fps)}",(490,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),3)
    cv2.imshow("Cam",f)
    cv2.imshow("Canvas",canvas)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
c.release()
cv2.destroyAllWindows()