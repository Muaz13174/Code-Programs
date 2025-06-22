import cv2
import numpy as np
def afm(img,fm):
    fm = str(fm)
    if fm.lower() == "gray" or fm.lower() == "grey":
        return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    elif fm.lower() == "gb":
        return cv2.GaussianBlur(img,(15,15),0)
    elif fm.lower() == "c":
        return cv2.Canny(img,100,200)
    elif fm.lower() == "sp":
        knl = np.array([[.272,.534,.131],[.349,.686,.168],[.393,.769,.189]])
        s = cv2.transform(img,knl)
        return np.clip(s,0,255).astype(np.uint8)
    elif fm.lower() == "i":
        return cv2.bitwise_not(img)
    return img

c = cv2.VideoCapture(0)
m = None
print("Please press a key :\n   - g = gray\n   - b = blur\n   - c = canny\n   - s = sepia\n   - i = invert\n   - n = normal\n   - q/esc = quit")
while 1:
    r,f = c.read()
    if not r:
        break
    ff = afm(f,m)
    if m == "gray" or m == "grey" or m == "c":
        cv2.imshow("Filtered Frame",ff)
    else:
        cv2.imshow("Filtered Frame",ff)
    k = cv2.waitKey(0) & 0xFF
    if k == ord("g"):
        m = "gray"
    elif k == ord("b"):
        m = "gb"
    elif k == ord("c"):
        m = "c"
    elif k == ord("s"):
        m = "sp"
    elif k == ord("i"):
        m = "i"
    elif k == ord("n"):
        m = None
    elif k in [ord("q"),27]:
        break

c.release()
cv2.destroyAllWindows()