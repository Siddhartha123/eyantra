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
*  Filename: task2_main.py
*  Version: 1.0.0  
*  Date: November 28, 2016
*  How to run this file: python task2_main.py
*  Author: e-Yantra Project, Department of Computer Science and Engineering, Indian Institute of Technology Bombay.
* ---------------------------------------------------

* ====================== GENERAL Instruction =======================
* 1. Check for "DO NOT EDIT" tags - make sure you do not change function name of main().
* 2. Return should be a list named occupied_grids and a dictionary named planned_path.
* 3. Do not keep uncessary print statement, imshow() functions in final submission that you submit
* 4. Do not change the file name
* 5. Your Program will be tested through code test suite designed and graded based on number of test cases passed 
**************************************************************************
'''
import cv2
import numpy as np

# ******* WRITE YOUR FUNCTION, VARIABLES etc HERE
import math as m

def main(image_filename):
	'''
This function is the main program which takes image of test_images as argument. 
Team is expected to insert their part of code as required to solve the given 
task (function calls etc).

***DO NOT EDIT THE FUNCTION NAME. Leave it as main****
Function name: main()

******DO NOT EDIT name of these argument*******
Input argument: image_filename

Return:
1 - List of tuples which is the coordinates for occupied grid. See Task2_Description for detail. 
2 - Dictionary with information of path. See Task2_Description for detail.
	'''

	occupied_grids = []		# List to store coordinates of occupied grid -- DO NOT CHANGE VARIABLE NAME
	planned_path = {}		# Dictionary to store information regarding path planning  	-- DO NOT CHANGE VARIABLE NAME
	



	##### WRITE YOUR CODE HERE - STARTS
        board_objects = []		# List to store output of board -- DO NOT CHANGE VARIABLE NAME
        output_list = []		# List to store final output 	-- DO NOT CHANGE VARIABLE NAME

        def sort_grid(l=[]):
        
                k=sorted(l)
                h=0
                li=[]
                for i in k:
                    li.append(tuple(i))

                for i in range(int(m.sqrt(len(l)))):
                    for j in range(int(m.sqrt(len(l)))):
                        k[h][0]=i+1
                        k[h][1]=j+1
                        h+=1
                return(k)

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
            elif px[0]<10 and px[1]<10 and px[2]<10:
                    return "black"
    image_board = cv2.imread(board_filepath)
    image_board_gray=cv2.cvtColor(image_board,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("gray",image_board_gray)
    image_board_inrange=cv2.inRange(image_board_gray,200,255)
    #cv2.imshow("board",image_board_inrange)

    cnts_b = cv2.findContours(image_board_inrange.copy(),cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
    cnts_b = cnts_b[0]
    cnts_b1,heirarchy_b = cv2.findContours(image_board_inrange.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image_board, cnts_b,-1, (206, 255, 39), 1)
    cnts_b1 = cnts_b1[0]
    shape=None
    l_board=[]
    for j in range(0,len(heirarchy_b[0])):
        if heirarchy_b[0][j][3]==-1:
            c = cnts_b[j]
            M = cv2.moments(c)
            cX = int((M['m10'] / M['m00']))
            cY = int((M['m01'] / M['m00']))
            if heirarchy_b[0][j][2]!=-1:
                #cv2.putText(image_board,str(j), (cX, cY), cv2.FONT_ITALIC,0.5, (0,0,0), 2)
                shape=find_shape(cnts_b[heirarchy_b[0][j][2]])
                M1=cv2.moments(cnts_b[heirarchy_b[0][j][2]])
                cX_object = int((M1['m10'] / M1['m00']))
                cY_object = int((M1['m01'] / M1['m00']))
                px=image_board[cY_object,cX_object]
                color=detect_color(px)
                area=int(M1['m00'])
            else:
                shape=None
                color=None
                area=None
            l_board.append([cX,cY,heirarchy_b[0][j][2],shape,color,area])

    l_board_sorted=sort_grid(l_board)
    #print("^^",l_board_sorted)
    
    path_board={}
    
    def stopExists(start):
        for j in l_board_sorted:
            if(tuple([start[0],start[1]])!=tuple([j[0],j[1]]) and j[3]==start[3] and j[4]==start[4] and abs(j[5]-start[5])<=10):
                return(True)
                break
        else:
            return(False)
        
    for start_object in l_board_sorted:
        if(start_object[2]!=-1 and start_object[4]!="black" and stopExists(start_object) ):
            for object in l_board_sorted:
                    if object[2]==-1:
                        path_board[tuple([object[0],object[1]])]=["0"]
                    elif l_board_sorted.index(start_object)!=l_board_sorted.index(object) and object[3]==start_object[3] and object[4]==start_object[4] and object[5]==start_object[5]:
                        path_board[tuple([object[0],object[1]])]=["*"]
                    elif l_board_sorted.index(start_object)==l_board_sorted.index(object):
                        path_board[tuple([object[0],object[1]])]=["#"]
                    else:
                        path_board[tuple([object[0],object[1]])]=["1"]
            #print ""
            #print path_board
            #print ""
    ##########################################################################################################################################################                
            for i in path_board:
                j=0
                for j in range(4):
                    path_board[i].append([0,0])


                    
            closed=set()
            opened=set()
            parent={}
            g={}
            gtemp={}
            def lookup(x,y):
                    if (x <= 0) or (y <= 0) or (x > (10)) or (y > (10)) or path_board[(x,y)][0] == '1':
                        return 0
                    else:
                        return [x,y]
            def link(t):
                    
                    x=t[0]
                    y=t[1]
                    if path_board[t][0] == '1':
                        return

                    path_board[t][1] = lookup(x,y-1)#north
                    path_board[t][2] = lookup(x-1,y)#west
                    path_board[t][3] = lookup(x,y+1)#south
                    path_board[t][4] = lookup(x+1,y)#east
            start=tuple([start_object[0],start_object[1]])
            stop=set()
            for j in path_board:
                if(path_board[j][0]=="*"):
                    stop.add(j)
                    #break
                  
            '''
            print(start)
            print(stop)
            '''
            for i in path_board:
                link(i)

            #for i in range(1,11):
             #   for j in range(1,11):
              #      print(i,j,path_board[(i,j)])

            
            g[start] = 0
            gtemp[start] =g[start] 
            opened.add(start)
           

            def neighbours(t):
                    """ Generate a set of neighbouring nodes """
                    neighbour = set()
                    if path_board[t][1] != 0:
                        neighbour.add(tuple(path_board[t][1]))
                    if path_board[t][2] != 0:
                        neighbour.add(tuple(path_board[t][2]))
                    if path_board[t][3] != 0:
                        neighbour.add(tuple(path_board[t][3]))
                    if path_board[t][4] != 0:
                        neighbour.add(tuple(path_board[t][4]))
                    
                    return neighbour
            def path(current_node):
                try: 
                    p = path(parent[current_node])
                    return_path = []
                    return_path.extend(p)
                    return_path.append(current_node)
                    
                    return return_path
                    
                    
                except KeyError:
                    # we have reached the start node
                    return [current_node]

                    

            while ((len(opened) > 0) and stop.isdisjoint(closed)):
                        
                        
                        gsort = sorted(gtemp, key=lambda t:g[t])
                        i = 0
                        for i in range(len(gsort)-1):
                            if(gsort[i] not in closed):
                                break

                        current = gsort[i]

                        for w in stop:
                            if current == w:
                                s=path(w)
                                #print(path(w))
                                end=w
                                s.remove(start)
                                s.remove(end)
                                

                        try:
                            opened.remove(current)
                            gtemp.pop(current)
                           # print("*",len(opened),opened)
                        except KeyError:
                            pass
                        closed.add(current)



                        for neighbour in neighbours(current):
                            if neighbour not in closed:
                      
                                temp_g = g[current] + 1
                                if (neighbour not in opened) or (temp_g < g[neighbour]): 
                                    # if the neighbour node has not yet been evaluated yet, then we evaluate it
                                    # or, if we have just found a shorter way to reach neighbour from the start node, 
                                    # then we replace the previous route to get to neighbour, with this new quicker route
                                    parent[neighbour] = current
                                    g[neighbour] = temp_g
                                    gtemp[neighbour] = temp_g
                        
                                    if neighbour not in opened:
                                        opened.add(neighbour)
                        #print(len(opened),opened)

            planned_path[(start)]=[end,s,len(s)+1]
            path_board={}
#####################################################################################################################################################################
    
    
    
    for j in range(0,len(l_board_sorted)):
        if l_board_sorted[j][2]!=-1:
            occupied_grids.append((l_board_sorted[j][0],l_board_sorted[j][1]))
    
	# cv2.imshow("board_filepath - press Esc to close",cv2.imread(board_filepath))			- For check - remove
	# cv2.imshow("container_filepath - press Esc to close",cv2.imread(container_filepath))


	# #### NO EDIT AFTER THIS

# DO NOT EDIT
# return Expected output, which is a list of tuples. See Task1_Description for detail.
	return occupied_grids, planned_path



'''
Below part of program will run when ever this file (task1_main.py) is run directly from terminal/Idle prompt.

'''
if __name__ == '__main__':

    # change filename to check for other images
    image_filename = "test_images/test_image1.jpg"

    main(image_filename)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
