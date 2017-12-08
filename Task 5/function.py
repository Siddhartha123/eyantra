import cv2
from math import pi,atan2,degrees
from navigation import *
import time
def find_shape(c):
    shape = "unidentified"
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.049* peri, True)
    if len(approx) == 3 :
        shape = "Triangle"
    elif len(approx) ==4 :
        shape = "4-sided"
    else:
        shape = "Circle"
    return shape

def detect_color(px):
        if px[0]>240 and px[1]<10 and px[2]<10:
                return "blue"
        elif px[0]<10 and px[1]<10 and px[2]>240:
                return "red"
        elif px[0]<10 and px[1]>240 and px[2]<10:
                return "green"
        elif px[0]<10 and px[1]>240 and px[2]>240:
                return "yellow"
def orient(l2,l1):
    cX2=float(l2[0])
    cY2=float(l2[1])

    cX=float(l1[0])
    cY=float(l1[1])
    if not cX2==cX:

        angle=degrees(atan2((cY2-cY),(cX2-cX)))
    else:
        if cY2>=cY:
            angle=90
        else:
            angle=-90
    return angle

def rotate_left():
    sendByte('a')
def rotate_right():
    sendByte('d')
def stop():
    sendByte('s')
def forward():
    sendByte('w')