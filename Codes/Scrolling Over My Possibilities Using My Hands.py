import cv2
import time as t
import pyautogui as pag
import mediapipe as mp
mph = mp.solutions.hands
hnd = mph.Hands(min_detection_confidence = .7,min_tracking_confidence = .7)
mpd = mp.solutions.drawing_utils
ScrSp = 300
ScrD = 1
cw,ch = 640.0,480.0
def dg(lm,hdn):
    f = []
    tips = [mph.HandLandmark.INDEX_FINGER_TIP,mph.HandLandmark.MIDDLE_FINGER_TIP,mph.HandLandmark.RING_FINGER_TIP,mph.HandLandmark.PINKY_TIP]
    for tip in tips:
        if lm.landmark[tip].y < lm.landmark[tip - 2].y:
            f.append(1)
    tt = lm.landmark[mph.HandLandmark.THUMB_TIP]
    ti = lm.landmark[mph.HandLandmark.THUMB_IP]
    if (hdn == "Right" and tt.x > ti.x) or (hdn == "Left" and tt.x < ti.x):
        f.append(1)
    return "scroll_up" if sum(f) == 5 else "scroll_down" if len(f) == 0 else "none"
c = cv2.VideoCapture(0)
c.set(3,cw)
c.set(4,ch)
ls = pt = 0
print("Gesture Scroll Control Active\nOpen Palm : Scroll Up\nFist : Scroll Down\nPress 'q' to exit")
while c.isOpened():
    s,img = c.read()
    if not s: break
    img = cv2.flip(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),1)
    results = hnd.process(img)
    g,hddns = "none","Unknown"
    if results.multi_hand_landmarks:
        for hand,hdni in zip(results.multi_hand_landmarks,results.multi_handedness):
            hddns = hdni.classification[0].label
            g = dg(hand,hddns)
            mpd.draw_landmarks(img,hand,mph.HAND_CONNECTIONS)
            if (t.time() - ls) > ScrD:
                if g == "scroll_up": pag.scroll(ScrSp)
                elif g == "scroll_down": pag.scroll(ScrSp * -1)
                ls = t.time()
    fps = 1/(t.time() - pt) if (t.time() - pt) > 0 else 0
    pt = t.time()
    cv2.putText(img,f"FPS : {int(fps)} | Hand : {hddns} | Gesture : {g}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,.7,(255,0,0),2)
    cv2.imshow("Gesture Control",cv2.cvtColor(img,cv2.COLOR_RGB2BGR))
    if cv2.waitKey(1) & 0xFF == ord("q") : break
c.release()
cv2.destroyAllWindows()