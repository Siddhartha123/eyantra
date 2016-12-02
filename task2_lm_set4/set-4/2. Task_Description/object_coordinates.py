import cv2
import numpy as np

def main(board_filepath):
    board_objects = []		# List to store output of board -- DO NOT CHANGE VARIABLE NAME
    output_list = []		# List to store final output 	-- DO NOT CHANGE VARIABLE NAME

    def sort1(l=[]):
        import math as m
        k=sorted(l)
        d=dict()
        h=0
        li=[]
        for i in k:
            li.append(tuple(i))

        for i in range(int(m.sqrt(len(l)))):
            for j in range(int(m.sqrt(len(l)))):
                d[li[h]]=[i+1,j+1,li[h][2]]
                h+=1
        s=[]
        for i in range(len(l)):
            s.append(d[li[i]])
        return(s)

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

    def detect_color(px):
            if px[0]>240 and px[1]<10 and px[2]<10:
                    return "blue"
            elif px[0]<10 and px[1]<10 and px[2]>240:
                    return "red"
            elif px[0]<10 and px[1]>240 and px[2]<10:
                    return "green"
            elif px[0]<10 and px[1]>240 and px[2]>240:
                    return "yellow"

    image_board = cv2.imread(board_filepath)
    image_board_gray=cv2.cvtColor(image_board,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",image_board_gray)
    image_board_inrange=cv2.inRange(image_board_gray,200,255)
    cv2.imshow("board",image_board_inrange)

    cnts_b = cv2.findContours(image_board_inrange.copy(),cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
    cnts_b = cnts_b[0]
    cnts_b1,heirarchy_b = cv2.findContours(image_board_inrange.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image_board, cnts_b,-1, (206, 255, 39), 1)

    cnts_b1 = cnts_b1[0]
    #print heirarchy_b[0]
    l_board=[]
    for j in range(0,len(heirarchy_b[0])):
        if heirarchy_b[0][j][3]==-1:
            c = cnts_b[j]
            M = cv2.moments(c)
            cX = int((M['m10'] / M['m00']))
            cY = int((M['m01'] / M['m00']))
            if heirarchy_b[0][j][2]!=-1:
                cv2.putText(image_board,str(j), (cX, cY), cv2.FONT_ITALIC,0.5, (0,0,0), 2)
            l_board.append([cX,cY,heirarchy_b[0][j][2]])
    l_board=sort1(l_board)
    output_object=[]
    for j in range(0,len(l_board)):
        if l_board[j][2]!=-1:
            output_object.append((l_board[j][0],l_board[j][1]))
    print output_object
    cv2.imshow("contour",image_board)
    #print l_board
if __name__ == '__main__':
    board_filepath = "test_images/test_image4.jpg"
    main(board_filepath)

cv2.waitKey(0)
