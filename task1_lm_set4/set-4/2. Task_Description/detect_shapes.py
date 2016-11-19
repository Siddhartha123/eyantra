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
def Sort(l):
    from operator import itemgetter, attrgetter
    import math
    l.sort()
    j=0
    d1=[]
    while(j<len(l)):
        d=[]
        for i in range(int(math.sqrt(len(l)))):
                       d.append(l[j])
                       j+=1
        d=sorted(d,key=itemgetter(6))
        for i in d:
            d1.append(i)
    return(d1)   
image_contain = cv2.imread("container_5.jpg")
image_contain_gray=cv2.cvtColor(image_contain,cv2.COLOR_BGR2GRAY)
image_contain_inrange=cv2.inRange(image_contain_gray,100,230)
#cv2.imshow("container",image_contain_inrange)

image_board = cv2.imread("board_4.jpg")
image_board_gray=cv2.cvtColor(image_board,cv2.COLOR_BGR2GRAY)
image_board_inrange=cv2.inRange(image_board_gray,100,230)
#cv2.imshow("board",image_board_inrange)

cnts_b = cv2.findContours(image_board_inrange.copy(),cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
cnts_b = cnts_b[0]
cnts_b1,heirarchy_b = cv2.findContours(image_board_inrange.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnts_b1 = cnts_b1[0]

l_board=[]   
 
for j in range(0,len(heirarchy_b[0])):
    if heirarchy_b[0][j][3]==-1:
        if heirarchy_b[0][j][2]!=-1:
            c1 = cnts_b[j]
            M1 = cv2.moments(c1)
            cX1 = int((M1['m10'] / M1['m00']))
            cY1 = int((M1['m01'] / M1['m00']))
            shape = find_shape(cnts_b[heirarchy_b[0][j][2]])
            c = cnts_b[heirarchy_b[0][j][2]]
            M = cv2.moments(c)
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            area=M["m00"]
            px=image_board[cY,cX]
            cv2.drawContours(image_board, cnts_b,heirarchy_b[0][j][2], (206, 255, 39), 2)
        else:
            shape=None
            area=0
            px=[260,260,260]
        l_board.append([cY1,cX1,heirarchy_b[0][j][2],detect_color(px),shape,area,cX1*cY1])       
        cv2.putText(image_board, detect_color(px), (cX, cY), cv2.FONT_ITALIC,0.5, (255, 255, 255), 2)

cnts_c = cv2.findContours(image_contain_inrange.copy(),cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
cnts_c = cnts_c[0]
cnts_c1,heirarchy_c = cv2.findContours(image_contain_inrange.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnts_c1 = cnts_c1[0]
l_container=[]
for j in range(0,len(heirarchy_c[0])):
    if heirarchy_c[0][j][3]==-1:
        if heirarchy_c[0][j][2]!=-1:
            c1 = cnts_c[j]
            M1 = cv2.moments(c1)
            cX1 = int((M1['m10'] / M1['m00']))
            cY1 = int((M1['m01'] / M1['m00']))
            shape = find_shape(cnts_c[heirarchy_c[0][j][2]])
            c = cnts_c[heirarchy_c[0][j][2]]
            M = cv2.moments(c)
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            area=M["m00"]
            px=image_contain[cY,cX]
            cv2.drawContours(image_contain, cnts_c,heirarchy_c[0][j][2], (206, 255, 39), 2)
        else:
            shape=None
            area=0
            px=[260,260,260]
        l_container.append([cY1,cX1,heirarchy_c[0][j][2],detect_color(px),shape,area,cX1*cY1])       
        cv2.putText(image_contain, detect_color(px), (cX, cY), cv2.FONT_ITALIC,0.5, (255, 255, 255), 2)
l_board=Sort(l_board)
board_objects=[]
for i in range(0,len(l_board)):
    board_objects.append([i+1,l_board[i][3],l_board[i][4]])
print board_objects
#print l_board
container_objects=[]
for i in range(0,len(l_container)):
    container_objects.append([i+1,l_container[i][3],l_container[i][4]])
#print container_objects
#print l_container
l_container=Sort(l_container)
final=[]
for i in l_board:
    flag=0
    for j in l_container:
            
        if i[3]==j[3] and i[4]==j[4] and abs(i[5]-j[5])<=10:
             final.append((l_board.index(i)+1,l_container.index(j)+1))
             
             flag=1
             break
    if flag==0:
        final.append((l_board.index(i)+1,0))
print final
        
    


cv2.imshow("Board", image_board)
cv2.imshow("Container", image_contain)
cv2.waitKey(0)