import imutils
import cv2
def find_shape(c):
	# initialize the shape name and approximate the contour
    shape = "unidentified"
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    if len(approx) == 3:
	    shape = "Triangle"
    elif len(approx) == 4:
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

image_contain = cv2.imread("container_1.jpg")
image_contain_gray=cv2.cvtColor(image_contain,cv2.COLOR_BGR2GRAY)
image_contain_inrange=cv2.inRange(image_contain_gray,100,230)
#cv2.imshow("container",image_contain_inrange)

image_board = cv2.imread("container_2.jpg")
image_board_gray=cv2.cvtColor(image_board,cv2.COLOR_BGR2GRAY)
image_board_inrange=cv2.inRange(image_board_gray,100,230)
cv2.imshow("board",image_board_inrange)

cnts = cv2.findContours(image_board_inrange.copy(),cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0]
cnts1,heirarchy = cv2.findContours(image_board_inrange.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnts1 = cnts1[0]
l=[]    
for j in range(0,len(heirarchy[0])):
    if heirarchy[0][j][3]==-1:
        if heirarchy[0][j][2]!=-1:
            c1 = cnts[j]
            M1 = cv2.moments(c1)
            cX1 = int((M1['m10'] / M1['m00']))
            cY1 = int((M1['m01'] / M1['m00']))
            shape = find_shape(cnts[heirarchy[0][j][2]])
            c = cnts[heirarchy[0][j][2]]
            M = cv2.moments(c)
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            area=M["m00"]
            px=image_board[cY,cX]
            cv2.drawContours(image_board, cnts,heirarchy[0][j][2], (206, 255, 39), 2)
        else:
            shape=None
            area=0
            px=[260,260,260]
        l.append([cY1,cX1,heirarchy[0][j][2],detect_color(px),shape,area])       
        cv2.putText(image_board, detect_color(px), (cX, cY), cv2.FONT_ITALIC,0.5, (255, 255, 255), 2)
l.sort()
board_objects=[]
for i in range(0,9):
    board_objects.append([i+1,l[i][3],l[i][4]])
#print board_objects
print l
cv2.imshow("Container", image_board)
cv2.waitKey(0)