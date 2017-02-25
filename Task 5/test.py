import cv2
import numpy as np
from getPerspective import *
def find_shape(c):
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        if len(approx) == 3:
                shape = "Triangle"
        elif len(approx) == 4:
            shape = "4-sided"
        else:
            shape = "Circle"
        return shape

kernel = np.ones((3,3),np.uint8)
source=cv2.imread("99light.jpg")
source=get_perspective_image(source)
hsv=cv2.cvtColor(source,cv2.COLOR_BGR2HSV)
b,g,r=cv2.split(hsv)
#cv2.imshow("b",b)
#cv2.imshow("g",g)
#cv2.imshow("r",r)
#hist1=cv2.equalizeHist(source)
#cv2.imshow("hist",hist1)
resize_image = np.zeros((source.shape[0],source.shape[1],3), np.uint8)
image_gray=cv2.cvtColor(source,cv2.COLOR_BGR2GRAY)
image_gray=g
#image_gray=cv2.medianBlur(image_gray.copy(),3)
#canny=cv2.Canny(image_gray,200,240)
#cv2.imshow("canny",canny)
#image_bw=cv2.threshold(image_gray,255,128,cv2.THRESH_BINARY)
retval,image_bw=cv2.threshold(image_gray, 100,255, cv2.THRESH_BINARY)
cv2.imshow("threshold",image_bw)
'''
image_bw = cv2.erode(image_bw.copy(),kernel,iterations = 1)
image_bw = cv2.dilate(image_bw.copy(),kernel,iterations = 1)
cv2.imshow("erode",image_bw)
'''
cnts_b= cv2.findContours(image_bw.copy(),cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
cnts_b=cnts_b[0]
count =0
for j in range(0,len(cnts_b)):
    c1 = cnts_b[j]
    M=cv2.moments(c1)
    shape=find_shape(c1)

    if M['m00'] >100:
        cX = int((M['m10'] / M['m00']))
        cY = int((M['m01'] / M['m00']))
        cv2.drawContours(source, cnts_b,j, (0, 255,255), 2)
        cv2.putText(source, shape, (cX, cY), cv2.FONT_ITALIC,0.5, (20, 20, 20), 1)
        count=count+1
print count
cv2.imshow("contour",source)
cv2.waitKey(0)
cv2.destroyAllWindows()
