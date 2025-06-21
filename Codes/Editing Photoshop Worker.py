import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("test pic.jpg")
(h,w) = img.shape[:2]
c = (w//2,h//2)
m = cv2.getRotationMatrix2D(c,1,1)
r = cv2.warpAffine(img,m,(w,h))
bm = np.ones(img.shape,dtype = "uint8") * 50
br = cv2.add(r,bm)
cimg = img[450:700,400:700]
crgb = cv2.cvtColor(cimg,cv2.COLOR_BGR2RGB)
plt.imshow(crgb)
plt.show()