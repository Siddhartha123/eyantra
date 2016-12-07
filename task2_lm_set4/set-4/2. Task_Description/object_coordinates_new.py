import cv2
import numpy as np

def main(board_filepath):
    board_objects = []		# List to store output of board -- DO NOT CHANGE VARIABLE NAME
    output_list = []		# List to store final output 	-- DO NOT CHANGE VARIABLE NAME

    def sort_grid(l=[]):
        import math as m
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
            else:
                shape=None
                color=None
            l_board.append([cX,cY,heirarchy_b[0][j][2],shape,color])

    l_board_sorted=sort_grid(l_board)
    #print(l_board_sorted)
    u=dict()
    path_board={}
    for start_object in l_board_sorted:
        if(start_object[2]!=-1 and start_object[4]!="black"):
            for object in l_board_sorted:
                    if object[2]==-1:
                        path_board[tuple([object[0],object[1]])]=["0"]
                    elif l_board_sorted.index(start_object)!=l_board_sorted.index(object) and object[3]==start_object[3] and object[4]==start_object[4]:
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
            f={}
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
            for i in path_board:
                if(path_board[i][0]=="#"):
                    start=i
                    break
            for j in path_board:
                if(path_board[j][0]=="*"):
                    stop=j
                    break
            '''
            print(start)
            print(stop)
            '''
            for i in path_board:
                link(i)

            #for i in range(1,11):
             #   for j in range(1,11):
              #      print(i,j,path_board[(i,j)])

            def h(t):
                return(abs(t[0]-stop[0])+abs(t[1]-stop[1]))
            g[start] = 0
            f[start] = g[start] + h(start)
            opened.add(start)
            def fscore(t):
                return(g[t]+h(t))

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
                    
                    parent[current_node]
                    p = path(parent[current_node])
                    return_path = []
                    return_path.extend(p)
                    return_path.append(current_node)
                    
                    return return_path
                    
                    
                except KeyError:
                    # we have reached the start node
                    return [current_node]

                    

            while (len(opened) > 0):
                        
                        
                        fsort = sorted(f, key=lambda t:fscore(t))
                        i = 0
                        for i in range(len(fsort)-1):
                            if(fsort[i] not in closed):
                                break

                        current = fsort[i]

                        if current == stop:
                            
                            s=path(stop)
                            break   

                        try:
                            opened.remove(current)
                            f.pop(current)
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
                                    f[neighbour] = fscore(neighbour)
                        
                                    if neighbour not in opened:
                                        opened.add(neighbour)
                        #print(len(opened),opened)

            u[(start,stop)]=s
            path_board={}
#####################################################################################################################################################################
    
    
    output_object=[]
    for j in range(0,len(l_board_sorted)):
        if l_board_sorted[j][2]!=-1:
            output_object.append((l_board_sorted[j][0],l_board_sorted[j][1]))
    print len(output_object)
    print output_object #this is the output of task 1 - coordinates of occupied grid
    cv2.imshow("contour",image_board)
    v=sorted(u)
    print ""
    for i in v:
        print i,"--->",u[i]
if __name__ == '__main__':
    board_filepath = "test_images/test_image4.jpg"
    main(board_filepath)
cv2.waitKey(0)
cv2.destroyAllWindows()
