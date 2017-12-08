import cv2
import numpy as np
from getPerspective import *
from trackBot import *

def color(l):
    if l[0]<=10 and l[1]<=10 and l[2]<=10:
        return 'black'
    else :
        return 'others'
def find_shape(c):
    shape = "unidentified"
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.05 * peri, True)
    if len(approx) == 3 :
        shape = "Triangle"
    elif len(approx) ==4 :
        shape = "4-sided"
    else:
        shape = "Circle"
    return shape

cap=cv2.VideoCapture(1)
count=0
while count<30:
	ret,img=cap.read()
	count=count+1
cap.release()

#l=get_perspective_image(img)
#img = cv2.imread('98light.jpg')
'''
img[l[1]+10,l[0]+10]=[255,255,255]
img[l[3],l[2]]=[255,255,255]

img[l[5],l[4]]=[255,255,255]
img[l[7],l[6]]=[255,255,255]
'''
#img=get_perspective_image(img)
#cv2.rectangle(img,(20,20),(620,460),(0,255,0),2)
source=img

img2=img
cv2.imshow('Original', img)


img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img)
# generating the kernels
kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,10.7,-1], [-1,-1,-1]])
kernel_sharpen_2 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])


# applying different kernels to the input image
output_1 = cv2.filter2D(s, -1, kernel_sharpen_1)
output_2 = cv2.filter2D(s, -1, kernel_sharpen_2)
#output_3 = cv2.filter2D(s, -1, kernel_sharpen_3)

#cv2.imshow('Sharpening', output_1)



ret,thresh=cv2.threshold(output_1,160,255,cv2.THRESH_BINARY)
#cv2.imshow('thresh',thresh)
l=[]
'''
contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for k in range(0,len(hierarchy[0])):
	c = contours[k]
	M = cv2.moments(c)
	area=M['m00']
	if area>27 and area<5000:

		cX = int((M['m10'] / M['m00']))
		cY = int((M['m01'] / M['m00']))
		shape = find_shape(contours[k])
		color=img[cY,cX]
		color=list(color)
		l.append([cX,cY,shape,color,area])
		cv2.drawContours(source,contours,k, (200,0,255),2)
		#cv2.putText(source, str(cX)+','+str(cY)+','+shape, (int(cX), int(cY)), cv2.FONT_ITALIC,0.5, (0,0,0), 2)
		cv2.putText(img2, shape, (int(cX), int(cY)), cv2.FONT_ITALIC,0.5, (0,0,0), 2)


cv2.imshow('final',source)
'''
botX,botY=trackBot(source,2,2)
print botX,botY
y=botX
x=botY
y2=botX
x2=botY


for i in range(botX+10,480):
    if source[x,y][0]<2 and source[x,y][1]<2 and source[x,y][2]<2:
        break
    else:
        x=x+1
for i in range(botY+10,640):
    if source[x2,y2][0]<8 and source[x2,y2][1]<8 and source[x2,y2][2]<8:
        break
    else:
        y2=y2+1

#print source[x,y]
cv2.line(source,(botY,botX),(y,x),[0,255,255],2)
cv2.line(source,(botY,botX),(y2,x2),[0,255,255],2)
cv2.imshow('frame',source)
cv2.waitKey(0)
