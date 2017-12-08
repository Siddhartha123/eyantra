import cv2
import numpy as np
from function import *
'''
*Function Name- find_objects
*Input :- feed from the camera
*Output :- a list of the co-ordinates, shape, size and color of the objects and obstacles
*Logic:- objects are detected by applying threshold on the obtined image and extracting contours
Example Call: find_objects(frame)
'''
def find_objects(source):
    resize_image = np.zeros((source.shape[0],source.shape[1],3), np.uint8)
    image_gray=cv2.cvtColor(source,cv2.COLOR_BGR2GRAY)
    retval,image_bw=cv2.threshold(image_gray,100,255, cv2.THRESH_BINARY)
    cnts_b= cv2.findContours(image_bw.copy(),cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
    cnts_b=cnts_b[0]
    cnts1,heirarchy_b=cv2.findContours(image_bw.copy(),cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
    objects=[] ## stores the co-ordinates of the objects and obstacles
    for j in range(0,len(cnts_b)):
        c1 = cnts_b[j]
        shape = find_shape(cnts_b[j])
        M=cv2.moments(c1)
        if M['m00'] >70 and M['m00']<5000:
            cX = int((M['m10'] / M['m00']))
            cY = int((M['m01'] / M['m00']))
            cv2.drawContours(resize_image, cnts_b,j, (0, 255,255), 1)
            cv2.putText(resize_image, str(cX)+','+ str(cY), (cX, cY), cv2.FONT_ITALIC,0.5, (255, 255, 255), 2)
            px=source[cY,cX]
            objects.append([cY,cX,detect_color(px),shape,M['m00']])
        else:
            shape=None
            area=0
            px=[260,260,260]
    return resize_image,objects
