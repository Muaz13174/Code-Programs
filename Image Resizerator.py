import cv2
from time import sleep as slp
img = cv2.resize(cv2.imread("test pic.jpg"),(300,300))
cv2.imshow(str(img.shape),img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
def imgs():
    while True:
        rimg = cv2.resize(img,(300,300))
        size = str(input("\nWhat size do you want the image to be? (small/medium/large): ")).lower()
        if size == "s" or size == "small":
            rimg = cv2.resize(img,(200,200))
            cv2.imwrite("input_image_small.jpg",rimg)
            break
        elif size == "m" or size == "medium":
            rimg = cv2.resize(img,(400,400))
            cv2.imwrite("input_image_medium.jpg",rimg)
            break
        elif size == "l" or size == "large":
            rimg = cv2.resize(img,(600,600))
            cv2.imwrite("input_image_large.jpg",rimg)
            break
        else:
            print("\nSorry, no such size.")
            continue
    cv2.imshow(str(rimg.shape),rimg)

imgs()
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()