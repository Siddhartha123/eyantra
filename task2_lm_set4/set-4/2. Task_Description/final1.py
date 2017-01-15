import cv2
<<<<<<< HEAD
import math as m
import numpy as np
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

def main(board_filepath):
    image_grid = cv2.imread(board_filepath)
    image_grid=cv2.copyMakeBorder(image_grid,0,1,0,1,cv2.BORDER_CONSTANT,(0,0,0))
    #cv2.rectangle(image_grid,(600,0),(0,600),(0,0,0),1)
    #cv2.imshow("image_grid",image_grid)
    image_grid_gray=cv2.cvtColor(image_grid,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("gray",image_grid_gray)
    image_grid_inrange=cv2.inRange(image_grid_gray,200,255)
    #cv2.imshow("board",image_grid_inrange)
    '''blank=np.zeros((601,601,1),np.uint8)
    blank[:,:]=0
    for i in range(0,600):
        for j in range(0,600):
            blank[i][j]=image_grid_inrange[i][j]
    cv2.imshow("window",blank)
    image_grid_inrange=blank
    '''
    cnts_b = cv2.findContours(image_grid_inrange.copy(),cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
    cnts_b = cnts_b[0]
    cnts_b1,heirarchy_b = cv2.findContours(image_grid_inrange.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

=======
import numpy as np
import math as m
def main(board_filepath):
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
>>>>>>> origin/master
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
                shape=find_shape(cnts_b[heirarchy_b[0][j][2]])
                M1=cv2.moments(cnts_b[heirarchy_b[0][j][2]])
                cX_object = int((M1['m10'] / M1['m00']))
                cY_object = int((M1['m01'] / M1['m00']))
<<<<<<< HEAD
                px=image_grid[cY_object,cX_object]
                color=detect_color(px)
                area=int(M1['m00'])
                cv2.drawContours(image_grid, cnts_b,heirarchy_b[0][j][2], (206, 255, 39), 1)
=======
                px=image_board[cY_object,cX_object]
                color=detect_color(px)
                area=int(M1['m00'])
>>>>>>> origin/master
            else:
                shape=None
                color=None
                area=0
            l_board.append([cX,cY,heirarchy_b[0][j][2],shape,color,area])

    l_board_sorted=sort_grid(l_board)
<<<<<<< HEAD

    cv2.imshow("image_grid",image_grid)
    path_board={}
    planned_path={}

    def stop_exists(start):
=======
    
    
    path_board={}
    planned_path={}
    
    def stopExists(start):
>>>>>>> origin/master
        for j in l_board_sorted:
            if(tuple([start[0],start[1]])!=tuple([j[0],j[1]]) and j[3]==start[3] and j[4]==start[4] and abs(j[5]-start[5])<=10):
                return(True)
                break
        else:
            return(False)
<<<<<<< HEAD
    def tagneighbour(x,y):
        if (x <= 0) or (y <= 0) or (x > (10)) or (y > (10)) or path_board[(x,y)][0] == '1':
            return 0
        else:
            return [x,y]
=======
    def lookup(x,y):
        if (x <= 0) or (y <= 0) or (x > (10)) or (y > (10)) or path_board[(x,y)][0] == '1':
            return 0
        else:
            return [x,y]    
>>>>>>> origin/master
    def neighbours(t):
        neighbour = set()
        if path_board[t][1] != 0:
            neighbour.add(tuple(path_board[t][1]))
        if path_board[t][2] != 0:
            neighbour.add(tuple(path_board[t][2]))
        if path_board[t][3] != 0:
            neighbour.add(tuple(path_board[t][3]))
        if path_board[t][4] != 0:
            neighbour.add(tuple(path_board[t][4]))
<<<<<<< HEAD

        return neighbour
    def path(current,before):
        try:
=======
        
        return neighbour
    def path(current,before):
        try: 
>>>>>>> origin/master
            p = path(before[current],before)
            return_path = []
            return_path.extend(p)
            return_path.append(current)
<<<<<<< HEAD

            return return_path


=======
            
            return return_path
            
            
>>>>>>> origin/master
        except KeyError:
            # we have reached the start node
            return [current]

    for start_object in l_board_sorted:
<<<<<<< HEAD
        if(not stop_exists(start_object)):
            planned_path[tuple([start_object[0],start_object[1]])]=["NO MATCH",[],0]
        elif(start_object[2]!=-1 and start_object[4]!="black" and stop_exists(start_object) ):
=======
        if(not stopExists(start_object)):
            planned_path[tuple([start_object[0],start_object[1]])]=["NO MATCH",[],0]
        elif(start_object[2]!=-1 and start_object[4]!="black" and stopExists(start_object) ):
>>>>>>> origin/master
            for object in l_board_sorted:
                    if object[2]==-1:
                        path_board[tuple([object[0],object[1]])]=["0"]
                    elif l_board_sorted.index(start_object)!=l_board_sorted.index(object) and object[3]==start_object[3] and object[4]==start_object[4] and abs(object[5]-start_object[5])<=10:
                        path_board[tuple([object[0],object[1]])]=["stop"]
                    else:
                        path_board[tuple([object[0],object[1]])]=["1"]
<<<<<<< HEAD

=======
                    
>>>>>>> origin/master
            for i in path_board:
                for j in range(4):
                    path_board[i].append([0,0])
            closed=set()
            opened=set()
            parent={}
            g={}
            gtemp={}

            start=tuple([start_object[0],start_object[1]])
            path_board[start][0]='0'

            stop=set()
            for j in path_board:
                if(path_board[j][0]=="stop"):
                    stop.add(j)
<<<<<<< HEAD

=======
                
>>>>>>> origin/master
            for t in path_board:
                    x=t[0]
                    y=t[1]
                    if path_board[t][0] == '1':
                        continue
<<<<<<< HEAD
                    path_board[t][1] = tagneighbour(x,y-1)#north
                    path_board[t][2] = tagneighbour(x-1,y)#west
                    path_board[t][3] = tagneighbour(x,y+1)#south
                    path_board[t][4] = tagneighbour(x+1,y)#east

            g[start] = 0
            gtemp[start] =g[start]
            opened.add(start)
            flag=0
            while ((len(opened) > 0) and stop.isdisjoint(closed)):
=======

                    path_board[t][1] = lookup(x,y-1)#north
                    path_board[t][2] = lookup(x-1,y)#west
                    path_board[t][3] = lookup(x,y+1)#south
                    path_board[t][4] = lookup(x+1,y)#east

            g[start] = 0
            gtemp[start] =g[start] 
            opened.add(start)
            flag=0
            while ((len(opened) > 0) and stop.isdisjoint(closed)):
                        
                        
>>>>>>> origin/master
                        gsort = sorted(gtemp, key=lambda t:g[t])
                        i = 0
                        for i in range(len(gsort)-1):
                            if(gsort[i] not in closed):
                                break

                        current = gsort[i]

<<<<<<< HEAD

                        if current in stop:
                            s=path(current,parent)
                            flag=1
                            end=current
                            s.remove(start)
                            s.remove(end)

=======
                        for w in stop:
                            if current == w:
                                s=path(w,parent)
                                flag=1
                                end=w
                                s.remove(start)
                                s.remove(end)
                                
>>>>>>> origin/master

                        try:
                            opened.remove(current)
                            gtemp.pop(current)

                        except KeyError:
                            pass
                        closed.add(current)



                        for neighbour in neighbours(current):
                            if neighbour not in closed:
<<<<<<< HEAD

                                temp_g = g[current] + 1
                                if (neighbour not in opened) or (temp_g < g[neighbour]):
                                    # if the neighbour node has not yet been evaluated yet, then we evaluate it
                                    # or, if we have just found a shorter way to reach neighbour from the start node,
                                    # then we replace the previous route to get to neighbour, with this new quicker route
                                    parent[neighbour]=current
                                    g[neighbour]=temp_g
                                    gtemp[neighbour]=temp_g

                                    if neighbour not in opened:
                                        opened.add(neighbour)

=======
                      
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
                        
>>>>>>> origin/master
            if(flag==1):
                planned_path[start]=[end,s,len(s)+1]
            else:
                planned_path[start]=["NO PATH",[],0]
<<<<<<< HEAD

            path_board={}
#####################################################################################################################################################################


=======
            
            path_board={}
#####################################################################################################################################################################
    
    
>>>>>>> origin/master
    occupied_grids=[]
    for j in range(0,len(l_board_sorted)):
        if l_board_sorted[j][2]!=-1:
            occupied_grids.append((l_board_sorted[j][0],l_board_sorted[j][1]))
<<<<<<< HEAD
    #print occupied_grids
    #print""
    print planned_path
    #v=sorted(planned_path)
    #for i in v:
    #    print i,"  -----> ",planned_path[i]
    #cv2.imshow("contour",image_grid)
fyl=4
=======
    print occupied_grids
    print""
    #print planned_path
    v=sorted(planned_path)
    for i in v:
        print i,"  -----> ",planned_path[i]
fyl=5
>>>>>>> origin/master
if __name__ == '__main__':
    board_filepath = "test_images/test_image"+str(fyl)+".jpg"
    main(board_filepath)
cv2.waitKey(0)
cv2.destroyAllWindows()
