import cv2
import numpy as np
import mediapipe as mp
from pycaw.pycaw import AudioUtilities as au
from pycaw.pycaw import IAudioEndpointVolume as iaev
from comtypes import CLSCTX_ALL as ca
from math import hypot as hp
import screen_brightness_control as sbc
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
mph = mp.solutions.hands
hnd = mph.Hands(min_detection_confidence = .7,min_tracking_confidence = .7)
mpd = mp.solutions.drawing_utils
try:
    d = au.GetSpeakers()
    itf = d.Activate(iaev._iid_,ca,None)
    v = itf.QueryInterface(iaev)
    vr = v.GetVolumeRange()
    mnv = vr[0]
    mxv = vr[1]
except Exception as e:
    print(f"Error initializing pycaw : {e}")
    exit()
c = cv2.VideoCapture(0)
if not c.isOpened():
    print("Error : Could not access the webcam")
    exit()
while 1:
    s,img = c.read()
    if not s:
        print("Error : Failed to read from webcam")
        break
    img = cv2.flip(img,1)
    imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hnd.process(imgrgb)
    if result.multi_hand_landmarks and result.multi_handedness:
        for i,hlm in enumerate(result.multi_hand_landmarks):
            hl = result.multi_handedness[i].classification[0].label
            mpd.draw_landmarks(img,hlm,mph.HAND_CONNECTIONS)
            tt = hlm.landmark[mph.HandLandmark.THUMB_TIP]
            it = hlm.landmark[mph.HandLandmark.INDEX_FINGER_TIP]
            h,w,_ = img.shape
            tp = (int(tt.x * w),int(tt.y * h))
            ip = (int(it.x * w),int(it.y * h))
            cv2.circle(img,tp,10,(255,0,0),-1)
            cv2.circle(img,ip,10,(255,0,0),-1)
            cv2.line(img,tp,ip,(0,255,0),3)
            d = hp(ip[0] - tp[0],ip[1] - tp[1])
            if hl == "Right":
                vol = np.interp(d,[30,300],[mnv,mxv])
                try:
                    v.SetMasterVolumeLevel(vol,None)
                except Exception as e:
                    print(f"Error Adjusting Volume : {e}")
                vb = np.interp(d,[30,300],[400,150])
                cv2.rectangle(img,(50,150),(85,400),(255,0,0),2)
                cv2.rectangle(img,(50,int(vb)),(85,400),(255,0,0),-1)
                cv2.putText(img,f"Volume : {int(np.interp(d,[30,300],[0,100]))}%",(40,450),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0))
            elif hl == "Left":
                b = np.interp(d,[30,300],[0,100])
                try:
                    sbc.set_brightness(b)
                except Exception as e:
                    print(f"Error adjusting brightness : {e}")
                cv2.rectangle(img,(100,150),(135,400),(0,255,0),2)
                cv2.rectangle(img,(100,int(b)),(135,400),(0,255,0),-1)
                cv2.putText(img,f"Brightness : {int(np.interp(d,[30,300],[0,100]))}%",(90,450),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
    cv2.imshow("Gesture Volume and Brightness Controller",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
c.release()
cv2.destroyAllWindows()