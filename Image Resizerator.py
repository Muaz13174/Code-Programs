import cv2
from time import sleep as slp
img = cv2.imread("test pic.jpg")
cv2.imshow(str(img.shape),img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
def imgs():
    while True:
        rimg = cv2.resize(img,(300,300))
        size = str(input("\nWhat size do you want the image to be? (small/medium/large): ")).lower()
        if size == "s" or size == "small":
            rimg = cv2.resize(img,(200,200))
            break
        elif size == "m" or size == "medium":
            rimg = cv2.resize(img,(400,400))
            break
        elif size == "l" or size == "large":
            rimg = cv2.resize(img,(600,600))
            break
        else:
            print("Sorry, no such size.")
            continue
    cv2.imshow(str(" "),rimg)
imgs()
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()