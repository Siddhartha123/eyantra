import numpy as np
import cv2
from trackBot import *
cap=cv2.VideoCapture('tracking.avi')
x=int(raw_input("x"))
y=int(raw_input("y"))
botX=1000
boty=1000
while abs(botX-x)>50 or abs(botY-y)>50 or abs(diff)>=20:
	ret,frame=cap.read()
	pos=trackBot(frame,x,y)
	if cv2.waitKey(250)==27:
		break
		'''
while abs(pos[2])>5:
	if abs(pos[2])<90 and pos[2]<0:
		rotate('a')
	pos=trackBot(frame,x,y)
	ret,frame=cap.read()
	if cv2.waitKey(250)==27:
		break
		'''
cap.release()
cv2.destroyAllWindows()
