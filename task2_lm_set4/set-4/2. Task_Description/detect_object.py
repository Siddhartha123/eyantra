import cv2
import numpy as np

# ******* WRITE YOUR FUNCTION, VARIABLES etc HERE


def main(board_filepath):
	'''
This function is the main program which takes image of game-board and
container as argument. Team is expected to insert their part of code as
required to solve the given task (function calls etc).

***DO NOT EDIT THE FUNCTION NAME. Leave it as main****
Function name: main()

******DO NOT EDIT name of these argument*******
Input argument: board_filepath and container_filepath.

Return:
1 - List of tuples which is the expected final output. See Task1_Description for detail.
2 - List of tuples for objects on board. See Task1_Description for detail.
	'''

        board_objects = []		# List to store output of board -- DO NOT CHANGE VARIABLE NAME
	output_list = []		# List to store final output 	-- DO NOT CHANGE VARIABLE NAME




	##### WRITE YOUR CODE HERE - STARTS
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
        def Sort(l):
            from operator import itemgetter
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

        image_board = cv2.imread(board_filepath)
        image_board_gray=cv2.cvtColor(image_board,cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray",image_board_gray)
        image_board_inrange=cv2.inRange(image_board_gray,200,255)
        cv2.imshow("board",image_board_inrange)

        cnts_b = cv2.findContours(image_board_inrange.copy(),cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
        cnts_b = cnts_b[0]
        cnts_b1,heirarchy_b = cv2.findContours(image_board_inrange.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnts_b1 = cnts_b1[0]
        print heirarchy_b[0]
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
                    cX = int((M['m10'] / M['m00']))
                    cY = int((M['m01'] / M['m00']))
                    area=M['m00']
                    px=image_board[cY,cX]
                    cv2.drawContours(image_board, cnts_b,heirarchy_b[0][j][2], (206, 255, 39), 2)
                    l_board.append([cY,cX,detect_color(px),shape,area])
                else:
                    shape=None
                    area=0
                    px=[260,260,260]
                    cX=None
                    cY=None
        cv2.imshow("contour",image_board)
        print l_board
        #l_board=Sort(l_board)
        board_objects=[]
        for i in range(0,len(l_board)):
            board_objects.append((i+1,l_board[i][3],l_board[i][4]))

if __name__ == '__main__':


	board_filepath = "test_images/test_image2.jpg"    			# change filename of board provided to you
	# change filename of container as required for testing

	main(board_filepath)

	cv2.waitKey(0)
