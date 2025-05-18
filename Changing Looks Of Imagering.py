import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("test pic.jpg")
imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(imgrgb)
plt.title("RGB Image")
plt.show()
gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(gimg,cmap = "gray")
plt.title("Grayscale Image")
plt.show()
cimg = imgrgb[450:700,400:700]
crgb = cv2.cvtColor(cimg,cv2.COLOR_BGR2RGB)
plt.imshow(crgb)
plt.title("Cropped Region")
plt.show()
(h,w) = img.shape[:2]
c = (w//2,h//2)
m = cv2.getRotationMatrix2D(c,45,1)
r = cv2.warpAffine(imgrgb,m,(w,h))
rrgb = cv2.cvtColor(r,cv2.COLOR_BGR2RGB)
plt.imshow(rrgb)
plt.title("Rotated Image")
plt.show()
bm = np.ones(img.shape,dtype = "uint8") * 50
br = cv2.add(img,bm)
brrgb = cv2.cvtColor(br,cv2.COLOR_BGR2RGB)
plt.imshow(brrgb)
plt.title("Brighter Image")
plt.show()