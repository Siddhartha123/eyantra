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
cam = cv2.VideoCapture(0)
for i in range(0,20):
    ret,source=cam.read()
while True:
    ret,source=cam.read()
    cv2.imshow("source",source)
    source=get_perspective_image(source)
    cv2.imshow("window",source)
    if cv2.waitKey(10)==27:
        break
cv2.destroyAllWindows()
