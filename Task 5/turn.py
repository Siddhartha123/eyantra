from trackBot import *
import cv2
from function import *
from serialCom import *
cap=cv2.VideoCapture(1)
ret,frame=cap.read()
x=100
y=100
cv2.namedWindow("window")
#pos=trackBot(frame,x,y)
#angle=pos[2]
count=0
'''
while (pos[2]-angle)>-90:
    count=count+1
    rotate('a')
    cv2.waitKey(270)
    ret,frame=cap.read()
    pos=trackBot(frame,x,y)
print count
'''
for i in range(0,13):
    rotate('a')
    
