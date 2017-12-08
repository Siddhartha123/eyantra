# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  Cross_A_Crater (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Resource
*  Filename: getPerspective.py
*  Version: 2.0.0
*  Date: February 23, 2017
*
*  Author: Sanam Shakya and Jayant Solanki, e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode
*
*
*  This software is made available on an “AS IS WHERE IS BASIS”.
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*  e-Yantra - An MHRD project under National Mission on Education using
*  ICT(NMEICT)
*
**************************************************************************
"""
############################################
## Import OpenCV
import numpy as np
import cv2
def get_perspective_image(frame):
    #hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lower = np.array([0, 0, 0]) #black color mask
    upper = np.array([100, 100, 100])
    mask = cv2.inRange(frame, lower, upper)
    cv2.imshow("mask",mask)
    ret,thresh1 = cv2.threshold(mask,130,255,cv2.THRESH_BINARY)
    cv2.imshow("thresh",thresh1)
    contours,heirarchy= cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    heirarchy=heirarchy[0]
    #cv2.imshow("window",)
    biggest = 0
    max_area = 0
    min_size = thresh1.size/4
    index1 = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 10000:
            peri = cv2.arcLength(i,True)
        if area > max_area:
            biggest = index1
            max_area = area
        index1 = index1 + 1


    '''
    index=heirarchy[biggest][2]
    area=cv2.contourArea(contours[index])
    while area<100:
        if heirarchy[index][0]!=-1:
            index=heirarchy[index][0]
            area=cv2.contourArea(contours[index])
    #cv2.drawContours(frame,contours,index,(0,255,0),3)
    '''
    approx = cv2.approxPolyDP(contours[biggest],0.05*peri,True)
    #cv2.drawContours(frame,contours,heirarchy[heirarchy[biggest][2]][0],(0,255,0),3)
    #print heirarchy[heirarchy[biggest][2]]
    x1 = approx[0][0][0]
    y1 = approx[0][0][1]
    x2 = approx[1][0][0]
    y2 = approx[1][0][1]
    x3 = approx[3][0][0]
    y3 = approx[3][0][1]
    x4 = approx[2][0][0]
    y4 = approx[2][0][1]
    cv2.imshow("1",frame)
    #points remapped from source image from camera
    #to cropped image try to match x1, y1,.... to the respective near values
    #you may need to edit below code to your own need
    #for LM
    pts1 = np.float32([[x2,y2],[x4,y4],[x1,y1],[x3,y3]])
    pts2 = np.float32([[0,700],[980,700],[0,0],[980,0]])#remarking each four side of the cropped image
    persM = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(frame,persM,(980,700))#setting output image resolution
    pts=np.array([[[0,0],[980,0],[980,700],[0,700]]])

    cv2.polylines(dst, pts, True, (255,255,255), 40)

    return dst
    #l=[x1,y1,x2,y2,x3,y3,x4,y4]
    #return l
