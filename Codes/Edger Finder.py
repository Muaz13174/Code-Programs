import cv2
import matplotlib.pyplot as plt
import numpy as np
def di(t,img):
    plt.figure(figsize = (8,8))
    if len(img.shape) == 2:
        plt.imshow(img,"gray")
    else:
        plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.title(t)
    plt.axis("off")
    plt.show()
def ied(imgp):
    img = cv2.imread(imgp)
    if img.all() == None:
        print("Error : Image Not Found")
        return
    gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    di("Original Grayscale Image",gimg)
    print("Select and option :\n   1. Sobel Edge Detection\n   2. Canny Edge Detection\n   3. Laplacian Edge Detection\n   4. Gaussian Smoothing\n   5. Median Filtering\n   6. Exit")
    while True:
        c = str(input("Enter your choice (1-6) : "))
        if c == "1":
            sx = cv2.Sobel(gimg,cv2.CV_64F,1,0,ksize = 3)
            sy = cv2.Sobel(gimg,cv2.CV_64F,0,1,ksize = 3)
            cs = cv2.bitwise_or(sx.astype(np.uint8),sy.astype(np.uint8))
            di("Sobel Edge Detection",cs)
        elif c == "2":
            print("Adjust thresholds for Canny (default : 100 and 200)")
            lt = int(input("Enter lower thresholds : "))
            ut = int(input("Enter upper thresholds : "))
            e = cv2.Canny(gimg,lt,ut)
            di("Canny Edge Detection",e)
        elif c == "3":
            l = cv2.Laplacian(gimg,cv2.CV_64F)
            di("Laplacian Edge Detection",l)
        elif c == "4":
            print("Adjust kernel size for Gaussian blur (must be odd, default : 5)")
            ks = int(input("Enter kernel size (odd number) : "))
            b = cv2.GaussianBlur(gimg,(ks,ks),0)
            di("Gaussian Smoothed Image",b)
        elif c == "5":
            print("Adjust kernel size for Gaussian blur (must be odd, default : 5)")
            ks = int(input("Enter kernel size (odd number) : "))
            mf = cv2.medianBlur(gimg,ks)
            di("Median Filtered Image",mf)
        elif c == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")
ied("test pic.jpg")