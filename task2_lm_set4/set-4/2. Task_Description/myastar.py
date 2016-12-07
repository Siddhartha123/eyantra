p={(7, 3): ['0'], (6, 9): ['0'], (1, 6): ['#'], (3, 7): ['0'], (2, 5): ['1'], (8, 5): ['*'], (5, 8): ['0'], (10, 8): ['0'], (6, 7): ['0'], (5, 5): ['0'], (10, 7): ['0'], (7, 6): ['0'], (6, 10): ['0'], (1, 1): ['0'], (4, 10): ['0'], (3, 2): ['0'], (2, 6): ['0'], (8, 2): ['0'], (4, 5): ['0'], (9, 3): ['0'], (7, 5): ['0'], (3, 1): ['0'], (9, 9): ['0'], (7, 8): ['0'], (2, 1): ['0'], (8, 9): ['0'], (9, 4): ['0'], (5, 1): ['0'], (10, 3): ['0'], (7, 2): ['0'], (1, 5): ['0'], (3, 6): ['0'], (2, 2): ['0'], (1, 10): ['0'], (8, 6): ['0'], (4, 1): ['0'], (10, 9): ['0'], (9, 7): ['0'], (6, 4): ['0'], (5, 4): ['0'], (10, 4): ['0'], (7, 1): ['0'], (3, 5): ['0'], (2, 7): ['0'], (8, 3): ['0'], (5, 10): ['0'], (4, 6): ['0'], (10, 10): ['0'], (9, 2): ['0'], (6, 1): ['0'], (5, 7): ['0'], (7, 4): ['0'], (1, 3): ['0'], (4, 8): ['0'], (2, 8): ['0'], (9, 8): ['0'], (6, 2): ['1'], (3, 10): ['0'], (8, 10): ['0'], (1, 4): ['0'], (3, 9): ['0'], (2, 3): ['0'], (1, 9): ['0'], (8, 7): ['0'], (4, 2): ['0'], (9, 6): ['0'], (6, 5): ['0'], (5, 3): ['0'], (10, 5): ['0'], (6, 8): ['0'], (1, 7): ['0'], (3, 4): ['0'], (2, 4): ['0'], (8, 4): ['0'], (5, 9): ['1'], (4, 7): ['0'], (9, 1): ['0'], (6, 6): ['0'], (5, 6): ['0'], (10, 6): ['0'], (7, 7): ['0'], (1, 2): ['0'], (4, 9): ['1'], (3, 3): ['0'], (2, 9): ['0'], (8, 1): ['0'], (4, 4): ['0'], (6, 3): ['1'], (7, 10): ['0'], (2, 10): ['0'], (9, 10): ['0'], (10, 1): ['0'], (7, 9): ['0'], (3, 8): ['0'], (1, 8): ['1'], (8, 8): ['0'], (4, 3): ['0'], (9, 5): ['0'], (5, 2): ['0'], (10, 2): ['0']}
for i in p:
    j=0
    for j in range(4):
        p[i].append([0,0])

        
closed=set()
opened=set()
parent={}
g={}
f={}
def lookup(x,y):
        if (x <= 0) or (y <= 0) or (x > (10)) or (y > (10)) or p[(x,y)][0] == '1':#checks if neighbour out of board or a obstacle
            return 0
        else:
            return [x,y]
def link(t):#adds neighbours of everything except obstacles
        
        x=t[0]
        y=t[1]
        if p[t][0] == '1':
            return

        p[t][1] = lookup(x,y-1)#north
        p[t][2] = lookup(x-1,y)#west
        p[t][3] = lookup(x,y+1)#south
        p[t][4] = lookup(x+1,y)#east
for i in p:
    if(p[i][0]=="#"):
        start=i
        break
for j in p:
    if(p[j][0]=="*"):
        stop=j
        break
'''
print(start)
print(stop)
'''
for i in p:
    link(i)

#for i in range(1,11):
 #   for j in range(1,11):
  #      print(i,j,p[(i,j)])

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

        if p[t][1] != 0:
            neighbour.add(tuple(p[t][1]))
        if p[t][2] != 0:
            neighbour.add(tuple(p[t][2]))
        if p[t][3] != 0:
            neighbour.add(tuple(p[t][3]))
        if p[t][4] != 0:
            neighbour.add(tuple(p[t][4]))
        
        return neighbour
def path(current_node):
    try: 
        
        parent[current_node]
        p = path(parent[current_node])
        return_path = []
        return_path.extend(p)
        return_path.append(current_node)
        
        return return_path
        
        print("reached here")
    except KeyError:
        # we have reached the start node
        return [current_node]

        

while ((len(opened) > 0) and (opened!={(10,1)} and opened!={(10,10)})):
            
            
            fsort = sorted(f, key=lambda t:fscore(t))
            i = 0
            for i in range(len(fsort)-1):
                if(fsort[i] not in closed):
                    break

            current = fsort[i]

            if current == stop:
                
                s=(path(stop))
                   

            try:
                opened.remove(current)
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
            print(len(opened),opened)

print(s)
                
                
                
                
                
