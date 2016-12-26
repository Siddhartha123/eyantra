import cv2
import numpy as np
import math as m
def main(board_filepath):

    def sort_grid(l=[]):#
        
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

    def detect_color(pixel):
            if pixel[0]>240 and pixel[1]<10 and pixel[2]<10:
                    return "blue"
            elif pixel[0]<10 and pixel[1]<10 and pixel[2]>240:
                    return "red"
            elif pixel[0]<10 and pixel[1]>240 and pixel[2]<10:
                    return "green"
            elif pixel[0]<10 and pixel[1]>240 and pixel[2]>240:
                    return "yellow"
            elif pixel[0]<10 and pixel[1]<10 and pixel[2]<10:
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
                shape=find_shape(cnts_b[heirarchy_b[0][j][2]])
                M1=cv2.moments(cnts_b[heirarchy_b[0][j][2]])
                cX_object = int((M1['m10'] / M1['m00']))
                cY_object = int((M1['m01'] / M1['m00']))
                central_pixel=image_board[cY_object,cX_object]
                color=detect_color(central_pixel)
                area=int(M1['m00'])
            else:
                shape=None
                color=None
                area=0
            l_board.append([cX,cY,heirarchy_b[0][j][2],shape,color,area])

    l_board_sorted=sort_grid(l_board)
    
    
    path_board={}
    planned_path={}
    
    def stop_exists(start):
        for element in l_board_sorted:
            if(tuple([start[0],start[1]])!=tuple([element[0],element[1]]) and element[3]==start[3] and element[4]==start[4] and abs(element[5]-start[5])<=10):
                return(True)
                break
        else:
            return(False)
    def check_for_valid_neighbour(x_coordinate,y_coordinate):
        if (x_coordinate <= 0) or (y_coordinate <= 0) or (x_coordinate > (10)) or (y_coordinate > (10)) or path_board[(x_coordinate,y_coordinate)]['type'] == 'obsatacle':
            return 'non-existent'
        else:
            return [x_coordinate,y_coordinate]    
    def neighbours(t):
        neighbour = set()
        if path_board[t]['north neighbour'] != 'non-existent':
            neighbour.add(tuple(path_board[t]['north neighbour']))
        if path_board[t]['west neighbour'] != 'non-existent':
            neighbour.add(tuple(path_board[t]['west neighbour']))
        if path_board[t]['south neighbour'] != 'non-existent':
            neighbour.add(tuple(path_board[t]['south neighbour']))
        if path_board[t]['east neighbour'] != 'non-existent':
            neighbour.add(tuple(path_board[t]['east neighbour']))
        
        return neighbour
    def path(current,before):
        try: 
            p = path(before[current],before)
            return_path = []
            return_path.extend(p)
            return_path.append(current)
            
            return return_path
            
            
        except KeyError:
            # we have reached the start node
            return [current]

    for start_object in l_board_sorted:
        if(not stop_exists(start_object)):
            planned_path[tuple([start_object[0],start_object[1]])]=["NO MATCH",[],0]
        elif(start_object[2]!=-1 and start_object[4]!="black" and stop_exists(start_object) ):
            
            for object in l_board_sorted:
                    path_board[tuple([object[0],object[1]])]=dict()
                    if object[2]==-1:
                        path_board[tuple([object[0],object[1]])]["type"]=["accessible"]
                    elif l_board_sorted.index(start_object)!=l_board_sorted.index(object) and object[3]==start_object[3] and object[4]==start_object[4] and abs(object[5]-start_object[5])<=10:
                        path_board[tuple([object[0],object[1]])]["type"]=["duplicate"]
                    else:
                        path_board[tuple([object[0],object[1]])]["type"]=["obstacle"]
                    
            for i in path_board:
                for direction in ["north","west","south","east"]:
                    path_board[i][direction+" neighbour"]=[0,0]
            #path_board[(element_x_coordinate,element_y_coordinate]=[state,north,west,south,east]
            closed=set()
            opened=set()
            parent={}
            g_score={}
            gtemp={}

            start=tuple([start_object[0],start_object[1]])
            path_board[start]["type"]='accessible'

            stop=set()
            for j in path_board:
                if(path_board[j]["type"]=="duplicate"):
                    stop.add(j)
                
            for t in path_board:
                    x_coordinate=t[0]
                    y_coordinate=t[1]
                    if path_board[t]["type"] == 'obstacle':
                        continue

                    path_board[t]['north neighbour'] = check_for_valid_neighbour(x_coordinate,y_coordinate-1)
                    path_board[t]['west neighbour'] = check_for_valid_neighbour(x_coordinate-1,y_coordinate)
                    path_board[t]['south neighbour'] = check_for_valid_neighbour(x_coordinate,y_coordinate+1)
                    path_board[t]['east neighbourt'] = check_for_valid_neighbour(x_coordinate+1,y_coordinate)

            g_score[start] = 0
            gtemp[start] =g_score[start] 
            opened.add(start)
            path_exists=None
            while ((len(opened) > 0) and stop.isdisjoint(closed)):
                        
                        
                        gsort = sorted(gtemp, key=lambda t:g_score[t])
                        i = 0
                        for i in range(len(gsort)-1):
                            if(gsort[i] not in closed):
                                break

                        current = gsort[i]

                     
                        if current in stop:
                            shortest_path=path(current,parent)
                            path_exists=True
                            end=current
                            shortest_path.remove(start)
                            shortest_path.remove(end)
                            

                        
                        opened.discard(current)
                        gtemp.pop(current)
                        closed.add(current)



                        for neighbour in neighbours(current):
                            if neighbour not in closed:
                      
                                temp_g = g_score[current] + 1
                                if (neighbour not in opened) or (temp_g < g_score[neighbour]): 
                                    # if the neighbour node has not yet been evaluated yet, then we evaluate it
                                    # or, if we have just found a shorter way to reach neighbour from the start node, 
                                    # then we replace the previous route to get to neighbour, with this new quicker route
                                    parent[neighbour]=current
                                    g_score[neighbour]=temp_g
                                    gtemp[neighbour]=temp_g
                        
                                    if neighbour not in opened:
                                        opened.add(neighbour)
                        
            if(path_exists):
                planned_path[start]=[end,shortest_path,len(shortest_path)+1]
            else:
                planned_path[start]=["NO PATH",[],0]
            
            path_board={}
#####################################################################################################################################################################
    
    
    occupied_grids=[]
    for j in l_board_sorted:
        if j[2]!=-1:
            occupied_grids.append((j[0],j[1]))
    print occupied_grids
    print""
    #print planned_path
    v=sorted(planned_path)
    for i in v:
        print i,"  -----> ",planned_path[i]
    cv2.imshow("contour",image_board)
fyl=4
if __name__ == '__main__':
    board_filepath = "test_images/test_image"+str(fyl)+".jpg"
    main(board_filepath)
cv2.waitKey(0)
cv2.destroyAllWindows()
