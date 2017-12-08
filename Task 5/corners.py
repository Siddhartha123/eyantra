from object_find import *
from trackBot import *

'''
*Function Name- corners
*Input :- feed image of the arena, co-ordinates of the bot
*Output :- list of the vertices of the entire grid(which is a rectangle) and the objects present in the arena
*Logic:- the vertices are obtained by determining the distance between the bot co-ord and the black pixels on either side,and the actual objects in the arena
Example Call: corners_objactual(botX,botY,img)
'''

def corners_objactual(botX,botY,img):
    x3=botX
    x4=botX
    y3=botY
    y4=botY
    x=botX
    y=botY
    x2=botX
    y2=botY
    for i in range(int(botX)+10,480):

        if img[x,y][0]<30 and img[x,y][1]<30 and img[x,y][2]<30:
            break
        else:
            x=x+1
    for i in range(int(botY)+10,640):
        if img[x2,y2][0]<20 and img[x2,y2][1]<20 and img[x2,y2][2]<20:
            break
        else:
            y2=y2+1

    for i in range(0,int(botX)):

        if img[x3,y3][0]<20 and img[x3,y3][1]<20 and img[x3,y3][2]<20:
            break
        else:
            x3=x3-1
    for i in range(0,int(botY)):
        if img[x4,y4][0]<20 and img[x4,y4][1]<20 and img[x4,y4][2]<20:
            break
        else:
            y4=y4-1


	corners=[]
	l=[]
	obj=[]
	corners=[[y4,x3],[y2,x3],[y2,x],[y4,x]]
	l=corners
	objects=find_objects(img)
	'''
	for i in range(0,len(objects)):
		if objects[i][1]<l[1][0] and objects[i][1]>l[0][0] and  objects[i][0]<l[2][1] and objects[i][0]>l[1][1] :
			obj.append([objects[i]])
	'''

    return corners,obj
