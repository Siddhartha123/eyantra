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
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lower = np.array([0, 0, 0]) #black color mask
    upper = np.array([120, 120, 120])
    mask = cv2.inRange(frame, lower, upper)
    #cv2.imshow("mask",mask)
    ret,thresh1 = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
    #cv2.imshow("thresh",thresh1)
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame,contours,-1,(0,255,0),3)
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
    approx = cv2.approxPolyDP(contours[biggest],0.05*peri,True)
    #drawing the biggest polyline

    x1 = approx[0][0][0]
    y1 = approx[0][0][1]
    x2 = approx[1][0][0]
    y2 = approx[1][0][1]
    x3 = approx[3][0][0]
    y3 = approx[3][0][1]
    x4 = approx[2][0][0]
    y4 = approx[2][0][1]

    #points remapped from source image from camera
    #to cropped image try to match x1, y1,.... to the respective near values
    #you may need to edit below code to your own need
    #for LM
    pts1 = np.float32([[x2,y2],[x4,y4],[x1,y1],[x3,y3]])
    pts2 = np.float32([[0,500],[700,500],[0,0],[700,0]])#remarking each four side of the cropped image
    persM = cv2.getPerspectiveTransform(pts1,pts2)
    dst = cv2.warpPerspective(frame,persM,(700,500))#setting output image resolution
    pts=np.array([[[0,0],[700,0],[700,500],[0,500]]])
    print pts
    cv2.polylines(dst, pts, True, (0,0,0), 25)
    cv2.imshow("123",dst)
    return dst
