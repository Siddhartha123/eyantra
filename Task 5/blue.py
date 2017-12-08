import cv2
import numpy as np
def find_shape(c):
    shape = "unidentified"
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.047 * peri, True)
    if len(approx) == 3 :
        shape = "Triangle"
    elif len(approx) ==4 :
        shape = "4-sided"
    else:
        shape = "Circle"
    return shape
cap=cv2.VideoCapture(1)
for i in range(0,10):
	ret,frame=cap.read()

#ret,frame=cap.read()
frame2=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
###pink marker starts
lower_blue=np.array([78,41,90])
#lower_pink=np.array([0,222,162])
upper_blue=np.array([165,255,255])
mask=cv2.inRange(frame2,lower_blue,upper_blue)
res=cv2.bitwise_and(frame2,frame2,mask=mask)
#blur=cv2.medianBlur(res,5)
blur=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(blur,120,255,cv2.THRESH_BINARY)
contours= cv2.findContours(mask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours=contours[0]
for k in range(0,len(contours)):
    c = contours[k]
    M = cv2.moments(c)
    area=M['m00']
    if area>70:
        cX = int((M['m10'] / M['m00']))
        cY = int((M['m01'] / M['m00']))
        cv2.drawContours(frame,contours,k, (200,0,255),2)
        shape=find_shape(contours[k])
        cv2.putText(frame, str(shape), (int(cX), int(cY)), cv2.FONT_ITALIC,0.5, (0,0,0), 2)
#cv2.drawContours(frame,contours,-1, (200,0,255),2)
cv2.imshow("window",frame)
cv2.waitKey(0)
