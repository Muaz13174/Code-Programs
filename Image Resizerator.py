import cv2
from time import sleep as slp
img = cv2.imread("test pic.jpg")
rimg = cv2.resize(img,(300,300))
cv2.imshow(str(img.shape),img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
while True:
    size = str(input("\nWhat size do you want the image to be? (small/medium/large): ")).lower()
    if size == "s" or size == "small":
        rimg = cv2.resize(img,(200,200))
    elif size == "m" or size == "medium":
        rimg = cv2.resize(img,(400,400))
    elif size == "l" or size == "large":
        rimg = cv2.resize(img,(600,600))
    else:
        print("Sorry, no such size.")
        continue
    break
cv2.imshow(rimg)