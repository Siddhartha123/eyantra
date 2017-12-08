import cv2
import numpy as np
from getPerspective import *

frame=cv2.imread("1.jpg")
frame=get_perspective_image(frame)
cv2.imshow("window",frame)
cv2.waitKey(0)
