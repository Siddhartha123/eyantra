import cv2
import numpy as np

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
    
img = cv2.imread('98light.jpg')
source=img
img2=img
cv2.imshow('Original', img)

img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img)
# generating the kernels
kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,11,-1], [-1,-1,-1]])
kernel_sharpen_2 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])


# applying different kernels to the input image
output_1 = cv2.filter2D(s, -1, kernel_sharpen_1)
output_2 = cv2.filter2D(s, -1, kernel_sharpen_2)
#output_3 = cv2.filter2D(s, -1, kernel_sharpen_3)

cv2.imshow('Sharpening', output_1)
#cv2.imshow('Excessive Sharpening', output_2)
#cv2.imshow('Edge Enhancement', output_3)

ret,thresh=cv2.threshold(output_1,160,255,cv2.THRESH_BINARY)
#cv2.imshow('thresh',thresh)
im2, contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for k in range(0,len(hierarchy[0])):
	c = contours[k]
	M = cv2.moments(c)
	area=M['m00']
	if area>27 and area<5000:
		cX = int((M['m10'] / M['m00']))
		cY = int((M['m01'] / M['m00']))
		cv2.drawContours(source,contours,k, (200,0,255),2)
		shape = find_shape(contours[k])
		cv2.putText(source, shape, (int(cX), int(cY)), cv2.FONT_ITALIC,0.5, (0,0,0), 2) 
cv2.imshow('final',source)
cv2.waitKey(0)

