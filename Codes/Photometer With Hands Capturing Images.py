import cv2
import mediapipe as mp
import time as t
import numpy as np
mph = mp.solutions.hands
hnd = mph.Hands(min_detection_confidence = .7,min_tracking_confidence = .7)
mpd = mp.solutions.drawing_utils
ftrs = [
    None,
    "GRAYSCALE",
    "SEPIA",
    "NEGATIVE",
    "BLUR"
]
cftrs = 0
c = cv2.VideoCapture(0)
if not c.isOpened():
    print("Error : Could not access the webcam")
    quit()
lat = 0
dbt = 1
def af(f,ft):
    if ft == "GRAYSCALE": return cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    elif ft == "SEPIA": return np.clip(cv2.transform(f,np.array([[.272,.534,.131],[.349,.686,.168],[.393,.769,.189]])),0,255).astype(np.uint8)
    elif ft == "NEGATIVE": return cv2.bitwise_not(f)
    elif ft == "BLUR": return cv2.GaussianBlur(f,(15,15),0)
    return f
while 1:
    s,img = c.read()
    if not s: print("Error : Failed to read frame from webcam");break
    img = cv2.flip(img,1)
    imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hnd.process(imgrgb)
    if result.multi_hand_landmarks:
        for hndlm in result.multi_hand_landmarks:
            mpd.draw_landmarks(img,hndlm,mph.HAND_CONNECTIONS)
            tt = hndlm.landmark[mph.HandLandmark.THUMB_TIP]
            it = hndlm.landmark[mph.HandLandmark.INDEX_FINGER_TIP]
            mt = hndlm.landmark[mph.HandLandmark.MIDDLE_FINGER_TIP]
            rt = hndlm.landmark[mph.HandLandmark.RING_FINGER_TIP]
            pt = hndlm.landmark[mph.HandLandmark.PINKY_TIP]
            fh,fw,_ = img.shape
            tx,ty = int(tt.x * fw),int(tt.y * fh)
            ix,iy = int(it.x * fw),int(it.y * fh)
            mx,my = int(mt.x * fw),int(mt.y * fh)
            rx,ry = int(rt.x * fw),int(rt.y * fh)
            px,py = int(pt.x * fw),int(pt.y * fh)
            for i,j in [[(tx,ty),(255,0,0)],[(ix,iy),(0,255,0)],[(mx,my),(0,0,255)],[(rx,ry),(255,255,0)],[(px,py),(255,0,255)]]: cv2.circle(img,i,10,j,-1)
            ct = t.time()
            if abs(tx - ix) < 30 and abs(ty - iy) < 30:
                if (ct - lat) > dbt:
                    cv2.putText(img,"Picture Captured!",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                    lat = ct
                    cv2.imwrite(fr"Outputs\Pic_{int(t.time())}.jpg",img)
                    print("Picture Saved!")
            elif (abs(tx - mx) < 30 and abs(ty - my) < 30) or (abs(tx - rx) < 30 and abs(ty - ry) < 30) or (abs(tx - px) < 30 and abs(ty - py) < 30):
                if (ct - lat) > dbt:
                    cftrs = (cftrs + 1) % len(ftrs)
                    lat = ct
                    print(f"Switched filter to {str(ftrs[cftrs]).lower()}")
    fimg = af(img,ftrs[cftrs])
    title = "Gesture-Controlled Photo App"
    if ftrs[cftrs] == "GRAYSCALE":
        cv2.imshow(title,cv2.cvtColor(fimg,cv2.COLOR_GRAY2BGR))
    else:
        cv2.imshow(title,fimg)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
c.release()
cv2.destroyAllWindows()