import numpy as np
import cv2
from function import *

def nothing(x):
	pass

def find_shape(c):
    shape = "unidentified"
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    if len(approx) == 3 :
        shape = "Triangle"
    elif len(approx) ==4 :
        shape = "4-sided"
    else:
        shape = "Circle"
    return shape
    
cap=cv2.VideoCapture('tracking.avi')
'''
cv2.namedWindow('image1')
cv2.namedWindow('image2')
cv2.namedWindow('image3')
cv2.createTrackbar('h','image1',0,179,nothing)
cv2.createTrackbar('s','image2',0,255,nothing)
cv2.createTrackbar('v','image3',0,255,nothing)
'''

while True:
	
	ret,frame=cap.read()
	frame2=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	#cv2.imshow('frame',frame)

	
	'''
	b = cv2.getTrackbarPos('h','image1')
	g = cv2.getTrackbarPos('s','image2')
	r = cv2.getTrackbarPos('v','image3')
	'''
	#### pink marker
	
	#lower_pink=np.array([170,150,185])
	lower_pink=np.array([39,70,185])
	upper_pink=np.array([179,230,255])
	
	#mask=cv2.inRange(frame,lower_yellow,upper_yellow)
	mask=cv2.inRange(frame2,lower_pink,upper_pink)
	res=cv2.bitwise_and(frame2,frame2,mask=mask)
	blur=cv2.medianBlur(res,5)
	blur=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
	#cv2.imshow('frame2',blur)
	ret,thresh=cv2.threshold(blur,120,255,cv2.THRESH_BINARY)
	cv2.imshow('thresh',thresh)
	im2,contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	l=[]
	for k in range(0,len(contours)):
		c = contours[k]
		M = cv2.moments(c)
		area=M['m00']
		if area>50 and area<5000:
		
			cX = int((M['m10'] / M['m00']))
			cY = int((M['m01'] / M['m00']))
			l.append([cX,cY])
			cv2.drawContours(frame,contours,k, (200,0,255),2)
			shape = find_shape(contours[k])
			#cv2.putText(frame, shape, (int(cX), int(cY)), cv2.FONT_ITALIC,0.5, (0,0,0), 2)
			cv2.putText(frame, 'tail', (int(cX), int(cY)), cv2.FONT_ITALIC,0.5, (0,0,0), 2)
			#print 'loop'
	
	### end of pink marker
	
	#### yellow marker	
	
	lower_yellow=np.array([0,140,175])
	upper_yellow=np.array([150,255,255])
		
	mask2=cv2.inRange(frame,lower_yellow,upper_yellow)
	res2=cv2.bitwise_and(frame,frame,mask=mask2)
	blur2=cv2.medianBlur(res2,5)
	blur2=cv2.cvtColor(blur2,cv2.COLOR_BGR2GRAY)
	#cv2.imshow('frame2',blur)
	ret,thresh2=cv2.threshold(blur2,120,255,cv2.THRESH_BINARY)
	cv2.imshow('thresh2',thresh2)
	im2,contours2, hierarchy2 = cv2.findContours(thresh2.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	l2=[]
	for k2 in range(0,len(contours2)):
		c2 = contours2[k2]
		M = cv2.moments(c2)
		area2=M['m00']
		if area2>50 and area2<5000:
		
			cX2 = int((M['m10'] / M['m00']))
			cY2 = int((M['m01'] / M['m00']))
			l2=[cX2,cY2]
			cv2.drawContours(frame,contours2,k2, (200,0,255),2)
			shape = find_shape(contours2[k2])
			#cv2.putText(frame, shape, (int(cX2), int(cY2)), cv2.FONT_ITALIC,0.5, (0,0,0), 2)
			cv2.putText(frame, 'head', (int(cX2), int(cY2)), cv2.FONT_ITALIC,0.5, (0,0,0), 2)			
	
	####end of yellow marker
	cv2.imshow('hope',frame)
	
	sense=direction([cX2,cY2],[cX,cY])
	print sense
	
	#print l2[0:]
	q=cv2.waitKey(30) & 0xff	
	if q == 27:
		break	
		
cap.release()
cv2.destroyAllWindows()		
