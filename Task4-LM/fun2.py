A=5
B=3
import turtle as tr
import copy
import time
tr.setup(1260/2,900/2)
wn=tr.Screen()
wn.title("eYantra")
wn.bgpic('arena.gif')
d=['north','south','east','west']
for i in d:
    tr.register_shape('bot'+i+'.gif')
tr.register_shape('triangle',((10,10),(10,-10),(-10,0)))
a=17
b=76
r=60
tr.tracer(0,0)

tr.penup()
d1={(0,1):'south',(1,0):'east',(0,-1):'north',(-1,0):'west'}
def ABS(k):
    if(k!=0):
        return(abs(k))
    else:
        return(1)
def botmove(y,x):
    global A,B
    X=(x-A)/ABS(x-A)
    Y=(y-B)/ABS(y-B)
    if((X,Y)!=(0,0)):
        tr.shape('bot'+d1[(X,Y)]+'.gif')
        tr.st()
        global u
        tr.clearstamp(u)
    tr.setpos(-315+a+x*r,-225+b+(6-y)*r)
    
    A=x
    B=y


def goto(y,x):
    tr.setpos(-315+a+x*r,-225+b+(6-y)*r)

p={}
p1={(1,1):['R','S','L'],(2,1):['B','C','M'],(3,1):['G','C','L'],(4,1):['G','T','M'],(5,1):['B','S','M'],(6,1):['R','T','L']}
p2={(4,4):['B','C','M'],(6,3):['G','T','M'],(1,9):['R','T','L'],(1,6):['R','S','L'],(5,8):['G','C','L'],(3,2):['B','S','M']}
p3=[(2,4),(5,5)]
stamps={}
clr={'R':'red','B':'blue','G':'green','S':'square','C':'circle','T':'triangle'}
def obj(l):
    tr.shape(clr[l[1]])
    if(l[2]=='L'):
        tr.shapesize(0.9,0.9,0.9)
    elif(l[2]=='M'):
        tr.shapesize(0.6,0.6,0.6)
for i in p1:
    tr.ht()
    goto(i[0],i[1])
    obj(p1[i])
    tr.color('black',clr[p1[i][0]])
    x=tr.stamp()
    stamps[i]=x
for i in p2:
    goto(i[0],i[1])
    obj(p2[i])
    tr.color(clr[p2[i][0]])
    x=tr.stamp()
    stamps[i]=x
for i in p3:
    goto(i[0],i[1])
    tr.color('red','red')
    tr.shape('square')
    tr.shapesize(1.8,1.8,1.8)
    x=tr.stamp()
    stamps[i]=x
    
    
    
tr.tracer(1,50)
for i in range(1,7):
    for j in range(1,10):
        p[(i,j)]=['0']
for i in p:
    if i in p2:
        p[i]=['#']
for i in p3:
    p[i]=['1']
for i in p:
    for j in range(4):
        p[i].append([0,0])
p4={}
stop=set()
for i in p1:
    for j in p2:
        if p1[i]==p2[j]:
            p4[j]=i
            stop.add(j)

print(p4)
def lookup(y,x,t1=None):
        if(t1==(y,x)):
            return[y,x]
        elif (x <= 0) or (y <= 0) or (x > 9) or (y > 6) or p[(y,x)][0] == '1':
            return 0
        else:
            return [y,x]
def link(t,p,t1=None):
        
        y=t[0]
        x=t[1]
        if p[t][0] == '1' and t!=t1:
            return

        p[t][1] = lookup(y-1,x,t1)#north
        p[t][2] = lookup(y,x-1,t1)#west
        p[t][3] = lookup(y+1,x,t1)#south
        p[t][4] = lookup(y,x+1,t1)#east
for i in p:
    link(i,p)

def turn(l):
    turns=0
    for i in range(len(l)-2):
        if((l[i][0]==l[i+1][0]==l[i+2][0]) or (l[i][1]==l[i+1][1]==l[i+2][1])):
            pass
        else:
            turns+=1
    return(turns)

    

def neighbours(t,p):
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
print(neighbours((2,1),p))
def findnearest(start):
    print('starting from',start)
    def path(current_node):
        try: 
            
            
            p = path(parent[current_node])
            return_path = []
            return_path.extend(p)
            return_path.append(current_node)
            
            return return_path
            
            print("reached here")
        except KeyError:
            # we have reached the start node
            return [current_node]
    def h(t):
        #return(abs(t[0]-stop[0])+abs(t[1]-stop[1]))
        #return(abs(t[0]-7)+abs(t[1]-6))
        #return(0)
        l=path(t)
        turns=0
        for i in range(len(l)-2):
            if((l[i][0]==l[i+1][0]==l[i+2][0]) or (l[i][1]==l[i+1][1]==l[i+2][1])):
                pass
            else:
                turns+=1
        return(turns)
    def fscore(t):
        return(g[t]+h(t))
    closed=set()
    opened=set()
    parent={}
    g={}
    f={}
    g[start] = 0
    f[start] = g[start] + h(start)
    opened.add(start)
    s=[]
    while ((len(opened) > 0) and (stop.isdisjoint(closed))):
            
           # v=opened
            fsort = sorted(f, key=lambda t:fscore(t))
            i = 0
        
            for i in range(len(fsort)-1):
                if(fsort[i] not in closed):
                    break
            current = fsort[i]

            if current in stop:
                s=path(current)
                end=current
                print('Reached object at',end)
            opened.discard(current)
            f.pop(current)
            closed.add(current)
            for neighbour in neighbours(current,p):
                if neighbour not in closed:
          
                    temp_g = g[current] + 1
                    if (neighbour not in opened) or (temp_g <g[neighbour]): 
                        # if the neighbour node has not yet been evaluated yet, then we evaluate it
                        # or, if we have just found a shorter way to reach neighbour from the start node, 
                        # then we replace the previous route to get to neighbour, with this new quicker route
                        parent[neighbour] = current
                        g[neighbour] = temp_g
                        f[neighbour] = fscore(neighbour)
            
                        if neighbour not in opened:
                            opened.add(neighbour)
    global p,p2
    print(p2[end],'picked from',end)
    stop.discard(end)
    p[end][0]=['0']
    for i in p:
        link(i,p)
    return([end,s])
    
def deposit(start):
    global p
    ptemp=copy.deepcopy(dict(p))
    for i in ptemp:
        if(ptemp[i][0]=='#'):
            ptemp[i][0]='1'
    for i in ptemp:
        link(i,ptemp)

    end=p4[start]
    def path(current_node):
        try: 
            
            
            p = path(parent[current_node])
            return_path = []
            return_path.extend(p)
            return_path.append(current_node)
            
            return return_path
            
            print("reached here")
        except KeyError:
            # we have reached the start node
            return [current_node]
    def h(t):
        #return(abs(t[0]-stop[0])+abs(t[1]-stop[1]))
        #return(abs(t[0]-7)+abs(t[1]-6))
        #return(0)
        l=path(t)
        turns=0
        for i in range(len(l)-2):
            if((l[i][0]==l[i+1][0]==l[i+2][0]) or (l[i][1]==l[i+1][1]==l[i+2][1])):
                pass
            else:
                turns+=1
        return(turns)
    def fscore(t):
        return(g[t]+h(t))
    closed=set()
    opened=set()
    parent={}
    g={}
    f={}
    g[start] = 0
    f[start] = g[start] + h(start)
    opened.add(start)
    s=[]
    #print(ptemp[(2,1)])
    while ((len(opened) > 0) and (end not in closed)):
            
           # v=opened
            fsort = sorted(f, key=lambda t:fscore(t))
            i = 0
        
            for i in range(len(fsort)-1):
                if(fsort[i] not in closed):
                    break
            current = fsort[i]
            #print('current=',current)
            if current == end:
                s=path(current)
                #print(s)
                
            opened.discard(current)
            f.pop(current)
            closed.add(current)
            #print(opened)
            #print("neighbours= ",neighbours(current,ptemp))
            for neighbour in neighbours(current,ptemp):
                if neighbour not in closed:
          
                    temp_g = g[current] + 1
                    if (neighbour not in opened) or (temp_g <g[neighbour]): 
                        # if the neighbour node has not yet been evaluated yet, then we evaluate it
                        # or, if we have just found a shorter way to reach neighbour from the start node, 
                        # then we replace the previous route to get to neighbour, with this new quicker route
                        parent[neighbour] = current
                        g[neighbour] = temp_g
                        f[neighbour] = fscore(neighbour)
            
                        if neighbour not in opened:
                            opened.add(neighbour)
    global p1,p2
    print(p1[end],'deposited at',end)
    p[end][0]='1'
    for i in p:
        link(i,p,end)
    s.remove(end)
    #print(s)
    return([end,s])
start=(3,5)
masterRoute=[]

while(len(stop)>0):
    q=findnearest(start)
    masterRoute.append(q[1])
    w=deposit(q[0])
    masterRoute.append(w[1])
    start=w[1][-1]
print(masterRoute)    

tr.shape('botsouth.gif')

goto(3,5)
tr.shape('botsouth.gif')
tr.st()
time.sleep(1)

m=[]
for i in masterRoute:
    m.extend(i)
q1=((len(m)-1)*21)/15
q2=(turn(m)*21)/15
print(q1+q2,'seconds')
print(q1*15,'cms')
tr.tracer(1,25)


k=0
u=None
for i in masterRoute:
    for j in i:
        
        botmove(j[0],j[1])
        v=j
    if(k%2==0):
        tr.clearstamp(stamps[v])
        e=v

    elif(k%2==1):
        u=tr.stamp()
        tr.ht()
        tr.color('brown','brown')
        tr.shape('square')
        tr.shapesize(1.7,1.7,1.7)
        goto(p4[e][0],p4[e][1])
        tr.stamp()
        goto(v[0],v[1])
        #tr.clearstamp(u)
        
    
    k+=1


    
    
    

wn.exitonclick()
