from trackBot import *
from object_find import *
from corners import *
cap=cv2.VideoCapture(1)
for i in range(0,10):
	ret,frame=cap.read()
image,o=find_objects(frame)
#print o
cv2.imshow("window",image)
x=int(raw_input("x"))
y=int(raw_input("y"))
target=[x,y]
while True:
	pos=trackBot(frame,x,y)
	traverse(cap,target,pos[0],pos[1])
	if cv2.waitKey(10)==27:
		break
cv2.destroyAllWindows()
