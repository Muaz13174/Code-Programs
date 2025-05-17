import cv2
img = cv2.imread("boy.jpeg")
gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rimg = cv2.resize(gimg,(224,224))
cv2.imshow("Processed Image :",rimg)
k = cv2.waitKey(0)
if k == ord("s"):
    cv2.imwrite("grayscale_resized_image.jpg",rimg)
    print("Image saved as 'grayscale_resized_image.jpg'")
else:
    print("Image not saved")
print("\nPress escape key to close window.\n")
if k == 27:
    cv2.destroyAllWindows()
    print("All windows destroyed")