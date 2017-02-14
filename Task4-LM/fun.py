p={(7, 3): ['0'], (6, 9): ['0'], (1, 6): ['0'], (3, 7): ['0'], (2, 5): ['1'], (8, 5): ['*'], (5, 8): ['0'], (10, 8): ['0'], (6, 7): ['0'], (5, 5): ['0'], (10, 7): ['0'], (7, 6): ['0'], (6, 10): ['0'], (1, 1): ['0'], (4, 10): ['0'], (3, 2): ['0'], (2, 6): ['0'], (8, 2): ['0'], (4, 5): ['0'], (9, 3): ['0'], (7, 5): ['0'], (3, 1): ['0'], (9, 9): ['0'], (7, 8): ['0'], (2, 1): ['0'], (8, 9): ['0'], (9, 4): ['0'], (5, 1): ['0'], (10, 3): ['0'], (7, 2): ['0'], (1, 5): ['0'], (3, 6): ['0'], (2, 2): ['0'], (1, 10): ['0'], (8, 6): ['0'], (4, 1): ['0'], (10, 9): ['0'], (9, 7): ['0'], (6, 4): ['0'], (5, 4): ['0'], (10, 4): ['0'], (7, 1): ['0'], (3, 5): ['0'], (2, 7): ['0'], (8, 3): ['0'], (5, 10): ['0'], (4, 6): ['0'], (10, 10): ['0'], (9, 2): ['0'], (6, 1): ['0'], (5, 7): ['0'], (7, 4): ['0'], (1, 3): ['0'], (4, 8): ['0'], (2, 8): ['0'], (9, 8): ['0'], (6, 2): ['1'], (3, 10): ['0'], (8, 10): ['0'], (1, 4): ['0'], (3, 9): ['0'], (2, 3): ['0'], (1, 9): ['0'], (8, 7): ['0'], (4, 2): ['0'], (9, 6): ['0'], (6, 5): ['0'], (5, 3): ['0'], (10, 5): ['0'], (6, 8): ['0'], (1, 7): ['0'], (3, 4): ['0'], (2, 4): ['0'], (8, 4): ['0'], (5, 9): ['1'], (4, 7): ['0'], (9, 1): ['0'], (6, 6): ['0'], (5, 6): ['0'], (10, 6): ['0'], (7, 7): ['0'], (1, 2): ['0'], (4, 9): ['1'], (3, 3): ['0'], (2, 9): ['0'], (8, 1): ['0'], (4, 4): ['0'], (6, 3): ['1'], (7, 10): ['0'], (2, 10): ['0'], (9, 10): ['0'], (10, 1): ['0'], (7, 9): ['0'], (3, 8): ['0'], (1, 8): ['1'], (8, 8): ['0'], (4, 3): ['0'], (9, 5): ['0'], (5, 2): ['0'], (10, 2): ['0']}

#p={(7, 3): ['0'], (6, 9): ['0'], (1, 6): ['0'], (3, 7): ['0'], (2, 5): ['0'], (8, 5): ['1'], (5, 8): ['0'], (10, 8): ['0'], (6, 7): ['1'], (5, 5): ['0'], (10, 7): ['0'], (7, 6): ['*'], (6, 10): ['0'], (1, 1): ['0'], (4, 10): ['0'], (3, 2): ['1'], (2, 6): ['0'], (8, 2): ['0'], (4, 5): ['0'], (9, 3): ['0'], (7, 5): ['0'], (3, 1): ['0'], (9, 9): ['1'], (7, 8): ['1'], (2, 1): ['0'], (8, 9): ['0'], (9, 4): ['0'], (5, 1): ['0'], (10, 3): ['0'], (7, 2): ['0'], (1, 5): ['1'], (3, 6): ['0'], (2, 2): ['1'], (1, 10): ['0'], (8, 6): ['0'], (4, 1): ['0'], (10, 9): ['0'], (9, 7): ['0'], (6, 4): ['0'], (5, 4): ['0'], (10, 4): ['0'], (7, 1): ['1'], (3, 5): ['0'], (2, 7): ['0'], (8, 3): ['0'], (5, 10): ['0'], (4, 6): ['0'], (10, 10): ['0'], (9, 2): ['0'], (6, 1): ['0'], (5, 7): ['0'], (7, 4): ['0'], (1, 3): ['1'], (4, 8): ['0'], (2, 8): ['0'], (9, 8): ['1'], (6, 2): ['1'], (3, 10): ['0'], (8, 10): ['0'], (1, 4): ['1'], (3, 9): ['0'], (2, 3): ['0'], (1, 9): ['0'], (8, 7): ['0'], (4, 2): ['0'], (9, 6): ['0'], (6, 5): ['1'], (5, 3): ['1'], (10, 5): ['0'], (6, 8): ['1'], (1, 7): ['0'], (3, 4): ['0'], (2, 4): ['0'], (8, 4): ['0'], (5, 9): ['0'], (4, 7): ['0'], (9, 1): ['0'], (6, 6): ['0'], (5, 6): ['1'], (10, 6): ['0'], (7, 7): ['0'], (1, 2): ['1'], (4, 9): ['#'], (3, 3): ['1'], (2, 9): ['0'], (8, 1): ['0'], (4, 4): ['0'], (6, 3): ['0'], (7, 10): ['0'], (2, 10): ['0'], (9, 10): ['0'], (10, 1): ['0'], (7, 9): ['0'], (3, 8): ['0'], (1, 8): ['0'], (8, 8): ['1'], (4, 3): ['0'], (9, 5): ['0'], (5, 2): ['0'], (10, 2): ['0']}

#p[(9,8)][0]="0"
#p[(9,9)][0]="0"
#p[(10,1)][0]='*'
#p[(5,1)][0]='*'
#p[(10,6)][0]='*'
#for i in range(2,11):
#    p[(6,i)][0]='1'
#p={}
S=0
#for i in range(1,11-S):
#    for j in range(1,11-S):
#        p[(i,j)]=['0']
#p[(1,10-S)][0]='#'
#p[(10-S-6,7)][0]='*'
p[(1,4)][0]='1'
p[(4,10)][0]='1'
p[(2,7)][0]='1'
p[(8,5)][0]='0'
p[(5,5)][0]='#'
p[(1,8)][0]='0'
p[(4,10)][0]='0'
p[(1,10)][0]='1'
#p[(1,5)][0]='*'
p[(10,9)][0]='1'
p[(2,6)][0]='1'
p[(6,9)][0]='1'
p[(8,5)][0]='1'
import time
for i in p:
    for j in range(4):
        p[i].append([0,0])

        
closed=set()
opened=set()
parent={}
g={}
f={}
#f1={}
def lookup(x,y):
        if (x <= 0) or (y <= 0) or (x > (10-S)) or (y > (10-S)) or p[(x,y)][0] == '1':
            return 0
        else:
            return [x,y]
def link(t):
        
        x=t[0]
        y=t[1]
        if p[t][0] == '1':
            return

        p[t][1] = lookup(x,y-1)#north
        p[t][2] = lookup(x-1,y)#west
        p[t][3] = lookup(x,y+1)#south
        p[t][4] = lookup(x+1,y)#east
#stop=set()
for i in p:
    if(p[i][0]=="#"):
        start=i
        break
for j in p:
    if(p[j][0]=="*"):
        stop=j
        break
stop=None
'''
print(start)
print(stop)
'''
for i in p:
    link(i)

#for i in range(1,11):
 #   for j in range(1,11):
  #      print(i,j,p[(i,j)])

def path(current_node):
    try: 
        
        
        p = path(parent[current_node])
        return_path = []
        return_path.extend(p)
        return_path.append(current_node)
        
        return return_path
        
        #print("reached here")
    except KeyError:
        # we have reached the start node
        return [current_node]

def ABS(k):
    if(k!=0):
        return(abs(k))
    else:
        return(1)
def h(t):
    #return(abs(t[0]-stop[0])+abs(t[1]-stop[1]))
    #return(abs(t[0]-7)+abs(t[1]-6
    #return(0)
    global start
    if t==start:
        return(0)
    A=0
    B=-1
    l=path(t)
    turns=0
    for i in range(len(l)-2):
        if((l[i][0]==l[i+1][0]==l[i+2][0]) or (l[i][1]==l[i+1][1]==l[i+2][1])):
            pass
        else:
            turns+=1
    X=(l[1][0]-start[0])/ABS(l[1][0]-start[0])
    Y=(l[1][1]-start[1])/ABS(l[1][1]-start[1])
    if (X,Y)==(A,B):
        pass
    elif X+A==0 and Y+B==0:
        turns+=2
    else:
        turns+=1
    return(turns)

#start=(6,5)       
g[start] = 0
f[start] = g[start] + h(start)
#f1[start] = g[start] + h(start)
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


import turtle as tr
r=50
tr.setworldcoordinates(0,0,(12-S)*r,(12-S)*r)
tr.speed('fastest')
tr.tracer(0,0)
tr.ht()
tr.penup()
clr={}
def colour(t):
    tr.setposition(t[0]*r,(11-S-t[1])*r)
    tr.color("pink","pink")
    tr.st()
    #time.sleep(0.5)
    tr.ht()
    tr.color("green","green")
    tr.pendown()
    tr.shape("square")
    q=tr.stamp()
    tr.penup()
    clr[t]=q
'''
def c1(t):
    c=['violet','indigo','blue','yellow','orange','grey','aqua']
    tr.setposition(t[0]*r,(11-S-t[1])*r)
    tr.color(c[int(fscore(t)%7)],c[int(fscore(t)%7)])
    tr.pendown()
    tr.stamp()
    tr.penup()
'''    
def fprint(t):
    
    tr.setposition(t[0]*r,(11-S-t[1])*r)
    tr.pendown()
    tr.write(str(fscore(t))+" ",False,'right')
    tr.penup()

for i  in range(1,11-S):
    for j in range(1,11-S):
        if(p[(i,j)][0]=='0'):
            tr.setposition(i*r,(11-S-j)*r)
            tr.pendown()
            tr.dot()
            tr.penup()
        elif(p[(i,j)][0]=='1'):
            tr.setposition(i*r,(11-S-j)*r)
            tr.pendown()
            tr.shape("square")
            tr.stamp()
            tr.penup()
        elif(p[(i,j)][0]=='*'):
            tr.setposition(i*r,(11-S-j)*r)
            tr.pendown()
            tr.shape("classic")
            tr.stamp()
            tr.penup()
        elif(p[(i,j)][0]=='#'):
            tr.setposition(i*r,(11-S-j)*r)
            tr.pendown()
            tr.shape("turtle")
            tr.stamp()
            tr.penup()
        else:
            pass        
#tr.update()
def path1(current_node,tree=dict()):
    nbor=set()
    for i in neighbours(current_node):
        #if i in g:
        nbor.add(i)
    nsort=min(nbor,key=lambda t:fscore(t))
    x=fscore(nsort)
    master=[]
    for neighbour in nbor:
        if fscore(neighbour)==x and fscore(neighbour)<fscore(current_node):
            master.append(neighbour)
    tree[current_node]=master
    #print('Done')
    dup=tuple(tree[current_node])
    for child in dup:
        path1(child,tree)
    return(tree)
    
tr.color("green","green")
#flag=0
cnt=0
s=[]
while ((len(opened) > 0) and (stop not in closed)):
            
           # v=opened
            fsort = sorted(f, key=lambda t:fscore(t))
            i = 0
        
            for i in range(len(fsort)-1):
                if(fsort[i] not in closed):
                    break
            #print("fscore",end='  ')
            #for j in fsort:
                #print(j,fscore(j),end='')
            #print('')
            
            current = fsort[i]
            #c1(current)
            
            #print('current=',current)
            tr.setposition(current[0]*r,(11-current[1])*r)
            tr.color("brown","brown")
            tr.st()
            #time.sleep(0.5)
            tr.ht()
            
            #for w in stop:
            if current == stop:
                s=path(current)
                '''
                tree={}
                tree1=path1(current,tree)
                
                l=[]
                for i in tree1:
                    l.append(i)
                l=sorted(l)
                for i in l:
                    print(i,'->',tree1[i],end='  ')
                print('')
                #print(tree1)
                '''
                    
                #break   

            
            
            
            try:
                tr.clearstamp(clr[current])
                # print("*",len(opened),opened)
            except KeyError:
                pass
            
            


            #print("neighbours",current,"-",neighbours(current))
            #time.sleep(1)
            for neighbour in neighbours(current):
                if neighbour not in closed:
                
                    temp_g = g[current] + 1
                    
                    l_temp=path(current)
                    if(len(l_temp)>1):
                        X=(l_temp[-1][0]-l_temp[-2][0])/ABS(l_temp[-1][0]-l_temp[-2][0])
                        Y=(l_temp[-1][1]-l_temp[-2][1])/ABS(l_temp[-1][1]-l_temp[-2][1])
                        X1=(neighbour[0]-current[0])/ABS(neighbour[0]-current[0])
                        Y1=(neighbour[1]-current[1])/ABS(neighbour[1]-current[1])
                        
                        if((X,Y)==(X1,Y1)):
                            temp_f=f[current]+1
                            
                        else:
                            temp_f=f[current]+2
                    
                           
                    if (neighbour not in opened) or (temp_g <g[neighbour])or (temp_f < f[neighbour]): 
                        # if the neighbour node has not yet been evaluated yet, then we evaluate it
                        # or, if we have just found a shorter way to reach neighbour from the start node, 
                        # then we replace the previous route to get to neighbour, with this new quicker route
                        parent[neighbour] = current
                        g[neighbour] = temp_g
                        fprint(neighbour)
                        f[neighbour] = fscore(neighbour)
                        #f1[neighbour] = fscore(neighbour)
                        if neighbour not in opened:
                            opened.add(neighbour)
                            colour(neighbour)
            closed.add(current)
            opened.discard(current)
            f.pop(current)

            #print(len(opened),opened)
            
            cnt+=1
            #if(v==opened):
            #    flag+=1
            #if(flag==3):
            #    break
l=[]
for i in g:
    l.append(i)
l.sort()
k=dict()
for i in l:    
    k[i]=fscore(i)
#print('*')
#print('*')
#print('*')
#print(k)
#print('')

tr.color("maroon","maroon")
for i in parent:
    tr.setposition(i[0]*r,(11-S-i[1])*r)
    tr.pendown()
    tr.setposition(parent[i][0]*r,(11-S-parent[i][1])*r)
    tr.penup()


tr.color("blue","blue")
tr.shape('classic')
q1=22
direction={(1,0):[0,-q1,0],(0,1):[-90,0,-q1],(0,-1):[90,0,q1],(-1,0):[180,q1,0]}
'''
for i in tree1:
    for j in tree1[i]:
        tr.penup()
        #tr.setposition(i[0]*r,(11-S-i[1])*r)
        #tr.pendown()
        tr.setposition(j[0]*r+direction[(j[0]-i[0],j[1]-i[1])][1],(11-S-j[1])*r-direction[(j[0]-i[0],j[1]-i[1])][2])
        tr.settiltangle(direction[(j[0]-i[0],j[1]-i[1])][0])
        tr.stamp()
        #tr.setposition(j[0]*r,(11-S-j[1])*r)
'''
tr.tracer(1,25)        
#print(parent)        
#print(cnt)
tr.color("red","red")
tr.pensize(5)
for i in s:
    tr.setposition(i[0]*r,(11-S-i[1])*r)
    tr.pendown()
    #print('hi')
    #print(s)
tr.exitonclick()        

