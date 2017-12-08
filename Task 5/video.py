import numpy as np
import cv2
#from getPerspective import *

cap=cv2.VideoCapture(1)

while True:
	ret,frame=cap.read()
#	frame=get_perspective_image(frame)
	cv2.imshow('frame',frame)
	if cv2.waitKey(10)==27:
		break


cap.release()
cv2.destroyAllWindows()
