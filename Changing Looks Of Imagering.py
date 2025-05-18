import cv2
import matplotlib.pyplot as plt
img = cv2.imread("boy.jpeg")
imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(imgrgb)
plt.title("RGB Image")
plt.show()
gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(gimg,cmap = "gray")
plt.title("Grayscale Image")
plt.show()
cimg = img[100:300,200:400]
crgb = cv2.cvtColor(cimg,cv2.COLOR_BGR2RGB)
plt.imshow(crgb)
plt.title("Cropped Region")
plt.show()