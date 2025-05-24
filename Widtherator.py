import cv2
import matplotlib.pyplot as plt
img = cv2.imread("test pic.jpg")
imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
h,w = imgrgb.shape[0:2]
r1w,r1h = 150,150
tl1 = (20,20)
br1 = (tl1[0] + r1w,tl1[1] + r1h)
cv2.rectangle(imgrgb,tl1,br1,(0,255,255),3)
r2w,r2h = 200,150
tl2 = (w-r2w-20,h-r2h-20)
br2 = (tl2[0] + r2w,tl2[1] + r2h)
cv2.rectangle(imgrgb,tl2,br2,(255,0,255),3)
c1x = tl1[0]+r1w//2
c1y = tl1[1]+r1h//2
c2x = tl2[0]+r2w//2
c2y = tl2[1]+r2h//2
cv2.circle(imgrgb,(c1x,c1y),15,(0,255,0),-1)
cv2.circle(imgrgb,(c2x,c2y),15,(0,0,255),-1)
cv2.line(imgrgb,(c1x,c1y),(c2x,c2y),(0,255,0),3)
f = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(imgrgb,"Region 1",(tl1[0],tl1[1] - 10),f,.7,(0,255,255),2,cv2.LINE_AA)
cv2.putText(imgrgb,"Region 2",(tl2[0],tl2[1] - 10),f,.7,(255,0,255),2,cv2.LINE_AA)
cv2.putText(imgrgb,"Center 1",(c1x-40,c1y + 40),f,.6,(0,255,0),2,cv2.LINE_AA)
cv2.putText(imgrgb,"Center 2",(c2x-40,c2y + 40),f,.6,(0,0,255),2,cv2.LINE_AA)
a_s = (20,w-50)
a_e = (h-20,w-50)
cv2.arrowedLine(imgrgb,a_s,a_e,(255,255,0),3,tipLength = .05)
cv2.arrowedLine(imgrgb,a_e,a_s,(255,255,0),3,tipLength = .05)
wlp = (a_s[0]+275,(a_s[1]+a_e[1])//2)
cv2.putText(imgrgb,f"Width : {w}px",wlp,f,.8,(255,255,0),2,cv2.LINE_AA)
plt.figure(figsize = (12,8))
plt.imshow(imgrgb)
plt.title("Annotated Image with Regions, Centers, and Bi-Directional Width Arrow")
plt.axis("off")
plt.show()