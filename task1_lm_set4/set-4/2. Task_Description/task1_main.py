# -*- coding: utf-8 -*-
'''
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  Author: e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode
*
*
*  This software is made available on an “AS IS WHERE IS BASIS”.
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*  e-Yantra - An MHRD project under National Mission on Education using
*  ICT(NMEICT)
*
* ---------------------------------------------------
*  Theme: Launch a Module
*  Filename: task1_main.py
*  Version: 1.0.0
*  Date: November 11, 2016
*  How to run this file: python task1_main.py
*  Author: e-Yantra Project, Department of Computer Science and Engineering, Indian Institute of Technology Bombay.
* ---------------------------------------------------

* ====================== GENERAL Instruction =======================
* 1. Check for "DO NOT EDIT" tags - make sure you do not change function name of main().
* 2. Return should be board_objects and output_list. Both should be list of tuple
* 3. Do not keep uncessary print statement, imshow() functions in final submission that you submit
* 4. Do not change the file name
* 5. Your Program will be tested through code test suite designed and graded based on number of test cases passed
**************************************************************************
'''
import cv2
import numpy as np

# ******* WRITE YOUR FUNCTION, VARIABLES etc HERE


def main(board_filepath, container_filepath):
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
        image_contain = cv2.imread(container_filepath)
        image_contain_gray=cv2.cvtColor(image_contain,cv2.COLOR_BGR2GRAY)
        image_contain_inrange=cv2.inRange(image_contain_gray,100,230)
        #cv2.imshow("container",image_contain_inrange)

        image_board = cv2.imread(board_filepath)
        image_board_gray=cv2.cvtColor(image_board,cv2.COLOR_BGR2GRAY)
        image_board_inrange=cv2.inRange(image_board_gray,100,230)
        #cv2.imshow("board",image_board_inrange)

        cnts_b = cv2.findContours(image_board_inrange.copy(),cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
        cnts_b = cnts_b[0]
        cnts_b1,heirarchy_b = cv2.findContours(image_board_inrange.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
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
                else:
                    shape=None
                    area=0
                    px=[260,260,260]
                l_board.append([cY1,cX1,heirarchy_b[0][j][2],detect_color(px),shape,area,cX1*cY1])

		cv2.imshow("window",image_board)
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
                    cX = int((M['m10'] / M['m00']))
                    cY = int((M['m01'] / M['m00']))
                    area=M['m00']
                    px=image_contain[cY,cX]
                else:
                    shape=None
                    area=0
                    px=[260,260,260]
                l_container.append([cY1,cX1,heirarchy_c[0][j][2],detect_color(px),shape,area,cX1*cY1])

        l_board=Sort(l_board)
        board_objects=[]
        for i in range(0,len(l_board)):
            board_objects.append((i+1,l_board[i][3],l_board[i][4]))
        #print board_objects
        #print l_board
        container_objects=[]
        for i in range(0,len(l_container)):
            container_objects.append([i+1,l_container[i][3],l_container[i][4]])
        #print container_objects
        #print l_container
        l_container=Sort(l_container)
        for i in range(0,len(l_board)):
            flag=0
            for j in range(0,len(l_container)):
                if l_board[i][3]==l_container[j][3] and l_board[i][4]==l_container[j][4] and abs(l_board[i][5]-l_container[j][5])<=10:
                     output_list.append((i+1,j+1))
                     flag=1
                     break
            if flag==0:
                output_list.append((i+1,0))
	# cv2.imshow("board_filepath - press Esc to close",cv2.imread(board_filepath))			- For check - remove
	# cv2.imshow("container_filepath - press Esc to close",cv2.imread(container_filepath))


	# #### NO EDIT AFTER THIS

# DO NOT EDIT
# return Expected output, which is a list of tuples. See Task1_Description for detail.
	#return board_objects, output_list



'''
Below part of program will run when ever this file (task1_main.py) is run directly from terminal/Idle prompt.

'''
if __name__ == '__main__':


	board_filepath = "1.jpg"    			# change filename of board provided to you
	container_filepath = "test_images/container_1.jpg"		# change filename of container as required for testing

	main(board_filepath,container_filepath)

	cv2.waitKey(0)
	cv2.destroyAllWindows()
