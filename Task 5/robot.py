import numpy as np
import cv2

cap=cv2.VideoCapture(1)
for i in range(0,10):
	ret,frame=cap.read()
def nothing(x):
	pass

cv2.namedWindow("k")
cv2.createTrackbar("lh","k",0,255,nothing)
cv2.createTrackbar("ls","k",0,255,nothing)
cv2.createTrackbar("lv","k",0,255,nothing)
cv2.createTrackbar("uh","k",0,255,nothing)
cv2.createTrackbar("us","k",0,255,nothing)
cv2.createTrackbar("uv","k",0,255,nothing)

while True:
	ret,frame=cap.read()
	cv2.imshow("output.jpg",frame)
	frame2=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	###pink marker starts
	lower_pink=np.array([cv2.getTrackbarPos("lh","k"),cv2.getTrackbarPos("ls","k"),cv2.getTrackbarPos("lv","k")])
	upper_pink=np.array([cv2.getTrackbarPos("uh","k"),cv2.getTrackbarPos("us","k"),cv2.getTrackbarPos("uv","k")])
	mask=cv2.inRange(frame2,lower_pink,upper_pink)
	cv2.imshow("mask",mask)
	res=cv2.bitwise_and(frame,frame,mask=mask)
	cv2.imshow("res",res)
	gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
	#gray=cv2.medianBlur(gray,3)
	#cv2.imshow("gray",gray)
	gray=cv2.medianBlur(gray,9)
	ret,thresh=cv2.threshold(gray,120,255,cv2.THRESH_BINARY)

	contours= cv2.findContours(mask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	contours=contours[0]
	for k2 in range(0,len(contours)):
		c2 = contours[k2]
		M = cv2.moments(c2)
		area2=M['m00']
		if area2>100:
			cX2 = int((M['m10'] / M['m00']))
			cY2 = int((M['m01'] / M['m00']))
			cv2.drawContours(frame,contours,k2, (200,0,255),2)
	cv2.imshow("window",frame)
	if cv2.waitKey(10)==27:
		break
