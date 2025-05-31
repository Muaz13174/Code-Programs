import cv2
def acf(img,ft):
    fimg = img.copy()
    if ft == "red_tint":
        fimg[:,:,1] = 0
        fimg[:,:,0] = 0
    elif ft == "blue_tint":
        fimg[:,:,1] = 0
        fimg[:,:,2] = 0
    elif ft == "green_tint":
        fimg[:,:,0] = 0
        fimg[:,:,2] = 0
    elif ft == "increase_red":
        fimg[:,:,2] = cv2.add(fimg[:,:,2],50)
    elif ft == "decrease_blue":
        fimg[:,:,0] = cv2.subtract(fimg[:,:,0],50)
    return fimg
img = cv2.imread("test pic.jpg")
if img is None:
    print("Error : Image not found")
else:
    ft = "original"
print("Press the following keys to apply filters :\n    -> r - Red Tint\n    -> b - Blue Tint\n    -> g - Green Tint\n    -> i - Increase Red Intensity\n    -> d - Decrease Blue Intensity\n    -> q - Quit")
while 1:
    fi = acf(img,ft)
    cv2.imshow("Filtered Image :",fi)
    k = cv2.waitKey(0) & 0xFF
    if k == ord("r"):
        ft = "red_tint"
    elif k == ord("b"):
        ft = "blue_tint"
    elif k == ord("g"):
        ft = "green_tint"
    elif k == ord("i"):
        ft = "increase_red"
    elif k == ord("d"):
        ft = "decrease_blue"
    elif k == ord("q"):
        print("Exiting...")
        break
    else:
        print("Invalid key! Please use 'r', 'b', 'g', 'i', 'd', or 'q'.")
cv2.destroyAllWindows()