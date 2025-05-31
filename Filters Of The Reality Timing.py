import cv2
import os
import keyboard as kb
def acf(i,ft,its = 50):
    fimg = i.copy()
    if ft == "rt":
        fimg[:,:,1] = 0
        fimg[:,:,0] = 0
    elif ft == "bt":
        fimg[:,:,1] = 0
        fimg[:,:,2] = 0
    elif ft == "gt":
        fimg[:,:,0] = 0
        fimg[:,:,2] = 0
    elif ft == "ir":
        fimg[:,:,2] = cv2.add(fimg[:,:,2],its)
    elif ft == "ib":
        fimg[:,:,0] = cv2.add(fimg[:,:,0],its)
    elif ft == "ig":
        fimg[:,:,1] = cv2.add(fimg[:,:,1],its)
    elif ft == "dr":
        fimg[:,:,2] = cv2.subtract(fimg[:,:,2],its)
    elif ft == "db":
        fimg[:,:,0] = cv2.subtract(fimg[:,:,0],its)
    elif ft == "dg":
        fimg[:,:,1] = cv2.subtract(fimg[:,:,1],its)
    return fimg
img = None
while 1:
    fn = str(input("Enter the name of your file : "))
    if not os.path.exists(fn):
        print(f"Error : '{fn}' does not exist")
        continue
    img = cv2.imread(fn)
    if img is None:
        print(f"Failed to read '{fn}'. Type another filename.")
        continue
    else:
        break
if img is None:
    print("Error : Image not found")
else:
    ft = "original"
print("Press the following keys to apply filters :\n    -> r - Red Tint\n    -> b - Blue Tint\n    -> g - Green Tint\n    -> /|\ (up arrow) - Increase Color Intensity\n    -> \|/ (down arrow) - Decrease Color Intensity\n    -> p - Reset Image\n    -> q - Quit")
global fi
fi = img.copy()
global ic
ic = 50
global dc
dc = 50
fi = acf(fi,ft)
cv2.imshow("Filtered Image :",fi)
while 1:
    k = cv2.waitKey(0) & 0xFF
    if k == ord("r"):
        ft = "rt"
    elif k == ord("b"):
        ft = "bt"
    elif k == ord("g"):
        ft = "gt"
    elif k == ord("i"):
        print("Press the following keys to choose which color to intensify :\n    -> 'r' - Increase Red Tint\n    -> 'b' - Increase Blue Tint\n    -> 'g' - Increase Green Tint")
        ik = cv2.waitKey(0)
        if ik == ord("r"):
            ft = "ir"
        elif ik == ord("b"):
            ft = "ib"
        elif ik == ord("g"):
            ft = "ig"
        while 1:
            iyon = str(input("Do you want to input increase (default : 50)? : ")).lower()
            if iyon == "no":
                pass
            elif iyon == "yes":
                print("OK!",end = " ")
                while 1:
                    try:
                        ic = int(input("So how much increase do you want? : "))
                    except ValueError:
                        print("Error : Not able to increase. Must be whole number.")
                        continue
                    if ic < 0:
                        print("Error : Number must be greater than zero.")
                        continue
                    elif ic == 0:
                        print("Umm...OK?")
                    else:
                        print("OK")
                        fi = acf(fi,ft,ic)
                        cv2.imshow("Filtered Image :",fi)
                    break
            else:
                print("Not valid!")
        continue
    elif k == ord("d"):
        print("Press the following keys to choose which color to mitigate :\n    -> 'r' - Decrease Red Tint\n    -> 'b' - Decrease Blue Tint\n    -> 'g' - Decrease Green Tint")
        dk = cv2.waitKey(0)
        if dk == ord("r"):
            ft = "dr"
        elif dk == ord("b"):
            ft = "db"
        elif dk == ord("g"):
            ft = "dg"
        while 1:
            dyon = str(input("Do you want to input decrease (default : 50)? : ")).lower()
            if dyon == "no":
                pass
            elif dyon == "yes":
                print("OK!",end = " ")
                while 1:
                    try:
                        dc = int(input("So how much decrease do you want? : "))
                    except ValueError:
                        print("Error : Not able to decrease. Must be whole number.")
                        continue
                    if dc < 0:
                        print("Error : Number must be greater than zero.")
                        continue
                    elif dc == 0:
                        print("Umm...OK? So setting it to 1...")
                        dc = 1
                    else:
                        print("OK")
                    fi = acf(fi,ft,dc)
                    cv2.imshow("Filtered Image :",fi)
                    break
            else:
                print("Not valid!")
        continue
    elif k == ord("p"):
        fi = img.copy()
        print("File Resetted")
    elif k == ord("q"):
        print("Exiting...")
        break
    else:
        print("Not valid key!")
    fi = acf(fi,ft)
    cv2.imshow("Filtered Image :",fi)