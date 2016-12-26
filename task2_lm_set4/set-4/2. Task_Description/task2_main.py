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
'''
* Team Id : LM#2370
* Author List : Ippilli Siddhartha Kumar, Piyush Panigrahi, Shubham Bhuyan, Pranoy Panda
* (Comma separated e.g. Name1, Name2)>
* Filename: task2_main.py
* Theme: launch_a_module
* Functions: sort_grid,find_shape,detect_color,duplicate_exists,check_for_valid_neighbour,neighbours,path
* Global Variables: <List of global variables defined in this file, none if no global
* variables>
'''



import cv2
import numpy as np
import math as m
# ******* WRITE YOUR FUNCTION, VARIABLES etc HERE
'''
* Function Name: sort_grid
* Input: unsorted_grid -> a list of all squares with information about image coordinates and shape,size,colour of element inside it
* Output: sorted_grid -> a list of squares provided with row and column info and sorted according to row and column
* Logic:
* Example Call: grid=sort_grid(grid)
'''
def sort_grid(unsorted_grid=[]):
    sorted_grid=sorted(unsorted_grid)
    index=0
    li=[]
    for i in sorted_grid:
        li.append(tuple(i))#function converts image pixel coordinates of each box/square into square coordinates(rows and columns) and sorts them accordingly
    for column in range(1,int(m.sqrt(len(unsorted_grid)))+1):
        for row in range(1,int(m.sqrt(len(unsorted_grid)))+1):
            sorted_grid[index][0]=column
            sorted_grid[index][1]=row
            index+=1
    return(sorted_grid)

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
'''
* Function Name: duplicate_exists
* Input: element-> of which it is to be found if duplicate exists on the board,sorted_grid->grid in which duplicate is to be found
* Output: Boolean-> True if duplicate exists and False if it doesnt
* Logic:
* Example Call: duplicate_exists((5,5),l_grid_sorted):
'''
def duplicate_exists(element,sorted_grid):
	for Object in sorted_grid:
		if(tuple([element[0],element[1]])!=tuple([Object[0],Object[1]]) and Object[3]==element[3] and Object[4]==element[4] and abs(Object[5]-element[5])<=10):
			return(True)
			break
	else:
		return(False)
'''
* Function Name: check_for_valid_neighbour
* Input: x_coordinate->column no of neighbour,y_coordinate->row no of neighbour,path_grid->grid in which neighbour is to be checked
* Output: [x_coordinate,y_coordinate] -> list of x_coordinate,y_coordinate if neighbour is legitimate else returns 0
* Logic: checks if proposed neighbour exists on grid,if it is an obstacle
* Example Call: check_for_valid_neighbour(4,3,path_grid)
'''
def check_for_valid_neighbour(x_coordinate,y_coordinate,path_grid):
	if (x_coordinate <= 0) or (y_coordinate <= 0) or (x_coordinate > (10)) or (y_coordinate > (10)) or path_grid[(x_coordinate,y_coordinate)][0] == "obstacle":
		return "not eligible neighbour"
	else:
		return [x_coordinate,y_coordinate]
'''
* Function Name: neighbours
* Input: Object->a tuple of (column,row) of object of which neighbour is to be found,path_grid->grid in which neighbour is to be checked
* Output: neighbour -> a set of coordinates of legitimate neighbours of the Object
* Logic: add objects in north,west,south,east of the Object as neighbours which are legit
* Example Call: neighbours(4,3,path_grid)
'''
def neighbours(Object,path_grid):
	neighbour = set()
	if path_grid[Object][1] != "not eligible neighbour":#North Neighbour
		neighbour.add(tuple(path_grid[Object][1]))
	if path_grid[Object][2] != "not eligible neighbour":#West Neighbour
		neighbour.add(tuple(path_grid[Object][2]))
	if path_grid[Object][3] != "not eligible neighbour":#South Neighbour
		neighbour.add(tuple(path_grid[Object][3]))
	if path_grid[Object][4] != "not eligible neighbour":#East Neighbour
		neighbour.add(tuple(path_grid[Object][4]))

	return neighbour
'''
* Function Name: path
* Input: Object->a tuple of (column,row) of object from which path is tobe retraced to starting object,before->a dictionary whose key is object and value is its predecessor on the path
* Output: return_path -> a list of tuple of coordinates of objects from start to end
* Logic: Recursion
* Example Call: shortest_path=path((5,2),parent)
'''
def path(Object,before):
	try:
		predecessors_path = path(before[Object],before)
		return_path = []
		return_path.extend(predecessors_path)
		return_path.append(Object)

		return return_path


	except KeyError:
		# we have reached the start node
		return [Object]


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

	image_grid = cv2.imread(image_filename)
	image_grid=cv2.copyMakeBorder(image_grid,0,1,0,1,cv2.BORDER_CONSTANT,(0,0,0))
	#cv2.rectangle(image_grid,(600,0),(0,600),(0,0,0),1)
	#cv2.imshow("image_grid",image_grid)
	image_grid_gray=cv2.cvtColor(image_grid,cv2.COLOR_BGR2GRAY)
	#cv2.imshow("gray",image_grid_gray)
	image_grid_inrange=cv2.inRange(image_grid_gray,200,255)
	cv2.imshow("grid",image_grid_inrange)
	cnts_b = cv2.findContours(image_grid_inrange.copy(),cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
	cnts_b = cnts_b[0]
	cnts_b1,heirarchy_b = cv2.findContours(image_grid_inrange.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	cnts_b1 = cnts_b1[0]
	shape=None
	l_grid=[]
	for j in range(0,len(heirarchy_b[0])):
	    if heirarchy_b[0][j][3]==-1:
	        c = cnts_b[j]
	        M = cv2.moments(c)
	        cX = int((M['m10'] / M['m00']))
	        cY = int((M['m01'] / M['m00']))
	        if heirarchy_b[0][j][2]!=-1:
	            shape=find_shape(cnts_b[heirarchy_b[0][j][2]])
	            M1=cv2.moments(cnts_b[heirarchy_b[0][j][2]])
	            cX_object = int((M1['m10'] / M1['m00']))
	            cY_object = int((M1['m01'] / M1['m00']))
	            px=image_grid[cY_object,cX_object]
	            color=detect_color(px)
	            area=int(M1['m00'])
	            cv2.drawContours(image_grid, cnts_b,heirarchy_b[0][j][2], (206, 255, 39), 1)
	        else:
	            shape=None
	            color=None
	            area=0
	        l_grid.append([cX,cY,heirarchy_b[0][j][2],shape,color,area])

	l_grid_sorted=sort_grid(l_grid)

	#cv2.imshow("image_grid",image_grid)
	path_grid={}
	planned_path={}


	for start_object in l_grid_sorted:
	    if(not duplicate_exists(start_object,l_grid_sorted)):#if there is no matching duplicate for the star_object
	        planned_path[tuple([start_object[0],start_object[1]])]=["NO MATCH",[],0]
	    elif(start_object[2]!=-1 and start_object[4]!="black" and duplicate_exists(start_object,l_grid_sorted) ):
                #here for each Object we create a separate grid where duplicates are end points of path,other objects or black boxes are treated as obstacles
                #and blank boxes are treated as accessible areas.The STATE is given by string
	        for object in l_grid_sorted:
	                if object[2]==-1:
	                    path_grid[tuple([object[0],object[1]])]=["accessible"]
	                elif l_grid_sorted.index(start_object)!=l_grid_sorted.index(object) and object[3]==start_object[3] and object[4]==start_object[4] and abs(object[5]-start_object[5])<=10:
	                    path_grid[tuple([object[0],object[1]])]=["stop"]
	                else:
	                    path_grid[tuple([object[0],object[1]])]=["obstacle"]

                #The following code initialises neighbours for each object on grid to which we provide value later
	        for element in path_grid:
	            for index in range(4):
	                path_grid[element].append([0,0])


	        closed=set()    #This is the set of boxes which have already been visited
	        opened=set()    #This is the set of boxes which are yet to be visited
	        parent={}       #This is a dictionary whose key is a box and value is another box which lies just before on the shortest path
	        g_score={}      #This is a dictionary whose key is a box and value is a score which helps us determine shortest path, the smaller the g_score,the shorter the path
	        gtemp={}

	        start=tuple([start_object[0],start_object[1]])
	        path_grid[start][0]="accessible"

	        stop=set()  #stop is a set of all potential duplicates which can be endpoints of shortest path
	        for element in path_grid:
	            if(path_grid[element][0]=="stop"):
	                stop.add(element)

                #the following code finds,checks and adds neighbours of each element on the grid
	        for element in path_grid:
	                x_coordinate=element[0]
	                y_coordinate=element[1]
	                if path_grid[element][0] != "obstacle":

	                    path_grid[element][1] = check_for_valid_neighbour(x_coordinate,y_coordinate-1,path_grid)#North Neighbour
	                    path_grid[element][2] = check_for_valid_neighbour(x_coordinate-1,y_coordinate,path_grid)#West Neighbour
	                    path_grid[element][3] = check_for_valid_neighbour(x_coordinate,y_coordinate+1,path_grid)#South Neighbour
	                    path_grid[element][4] = check_for_valid_neighbour(x_coordinate+1,y_coordinate,path_grid)#East Neighbour

	        g_score[start] = 0
	        gtemp[start] = g_score[start]
	        opened.add(start)
	        path_exists=None
	        while ((len(opened) > 0) and stop.isdisjoint(closed)): #We shall be looking for path till one path is found or all of the board have been traced
	                    elements_sorted_according_to_gscore = sorted(gtemp, key=lambda t:g_score[t]) #elements_sorted_according_to_gscore is a list of all boxes sorted by gscore
                            #The following code looks for the box with lowest gscore not visited yet
	                    index = 0
	                    for index in range(len(elements_sorted_according_to_gscore)-1):
	                        if(elements_sorted_according_to_gscore[index] not in closed):
	                            break

	                    current = elements_sorted_according_to_gscore[index] #current is the box with lowest gscore not visited yet


	                    if current in stop: #if the current box possesses a duplicate,we will retrace path and move on
	                        shortest_path=path(current,parent)
	                        path_exists=True
	                        end=current
	                        shortest_path.remove(start)#This line is added to comply to Output Format of problem statement
	                        shortest_path.remove(end) #This line is added to comply to Output Format of problem statement


	                    #Since current box is visited we remove from opened set and add to closed set
	                    opened.discard(current)
	                    gtemp.pop(current)
	                    closed.add(current)
	                    # In the following code, if the neighbour boxes of current have not yet been evaluated yet, then we evaluate it
	                    # or, if we have just found a shorter way to reach neighbour from the start node,
	                    # then we replace the previous path to get to neighbour, with this new shorter path



	                    for neighbour in neighbours(current,path_grid):
	                        if neighbour not in closed:

	                            temporary_g_score = g_score[current] + 1
	                            if (neighbour not in opened) or (temporary_g_score < g_score[neighbour]):
	                                parent[neighbour]=current
	                                g_score[neighbour]=temporary_g_score
	                                gtemp[neighbour]=temporary_g_score

	                                if neighbour not in opened:
	                                    opened.add(neighbour)

	        if(path_exists):
	            planned_path[start]=[end,shortest_path,len(shortest_path)+1]
	        else:
	            planned_path[start]=["NO PATH",[],0]

	        path_grid={}


	for Object in l_grid_sorted:
	    if Object[2]!=-1:
	        occupied_grids.append((Object[0],Object[1]))






	# cv2.imshow("grid_filepath - press Esc to close",cv2.imread(grid_filepath))			- For check - remove
	# cv2.imshow("container_filepath - press Esc to close",cv2.imread(container_filepath))


	# #### NO EDIT AFTER THIS

	# DO NOT EDIT
	# return Expected output, which is a list of tuples. See Task1_Description for detail.
	print occupied_grids, planned_path



'''
Below part of program will run when ever this file (task1_main.py) is run directly from terminal/Idle prompt.

'''
if __name__ == '__main__':

    # change filename to check for other images
    image_filename = "test_images/test_image4.jpg"

    main(image_filename)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
