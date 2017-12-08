import cv2
import numpy as np
cap=cv2.VideoCapture(1)
from function import *
from trackBot import *
from object_find import *
from corners import *
from serialCom import *
for i in range(0,10):
	ret,frame=cap.read()
pos=trackBot(frame,0,0) # trackbot to changed to give bot initial co-ord.
corner_list,obj=corners_objactual(pos[0],pos[1],frame)
find_objects(frame)
#from FINALE import *
#path=[(1,2),3]#path planning also needs the corner points of the grid(given by new2)

path=[(335, 210),(315, 210), (285, 240), (285, 245), 'p', (285, 240), (175, 350), (85, 350), 'd', (90, 350), (90, 380), 'p', (90, 375), (90, 390), (80, 400), 'd', (85, 395),(210, 395), (215, 390), 'p', (210, 395), (45, 230), (45, 180), 'd', (45, 185), (145, 185), 'p', (140, 185), (85, 240), 'd', (90, 235), (105, 235), (155, 185), (225, 185),(230, 180), (385, 180), (390, 175), (430, 175), (490, 115), 'p', (485, 120), (435, 70), (300, 70), (295, 75), (295, 115), (290, 120), (235, 120), (230, 125), (230, 180), (225, 185), (145, 185), (90, 130), (90, 100), (85, 95), 'd', (90, 100), (90, 115), (140, 165), (140, 180), (145, 185), (195, 185), (200, 190), (350, 190), (555, 395),'p', (550, 390), (370, 210), (85, 210), 'd']
#path=[(310, 200), (260, 200), (260, 240), 'p', (260, 230), (260, 300), (40, 300), (40, 310), 'd', (40, 300), (110, 300), (110, 380), 'p', (110, 370), (110, 420), (80, 420), 'd', (90, 420), (90, 350), (210, 350), 'p', (200, 350), (200, 260), (40, 260), (40, 180), 'd', (40, 190), (130, 190), (130, 210), (140, 210), 'p', (130, 210), (130, 280), (80, 280), 'd', (90, 280), (90, 190), (530, 190), (530, 110), 'p', (530, 120), (230, 120), (230, 190), (90, 190), (90, 70), (80, 70), 'd', (90, 70), (90, 230), (540, 230), (540, 410), (550, 410), 'p', (540, 410), (540, 210), (80, 210), 'd']

#path2=[]
#for i in path:
#	if(type(i)==tuple):
#		path2.append([i[0],i[1]])
#	else:
#		path2.append(i)

#print(type(path[0][0]))
pos=trackBot(frame,1,1)
for path1 in path:
	ret,frame=cap.read()
	cv2.imshow("frame",frame)
	if path1=='p':
		pickup()
	elif path1=='d':
		drop()
	elif type(path1)==tuple:
		pos=trackBot(frame,path1[0],path1[1])
		print pos
		traverse(cap,path1,pos[0],pos[1])
buzz()
