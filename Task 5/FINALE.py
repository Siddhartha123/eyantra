
div=5
START=(336//div,213//div)
from  copy import deepcopy






p={}

k=40//div

p1={(48//div,72//div):['B','S','L'],(47//div,142//div):['G','T','M'],(48//div,214//div):['R','T','L'],
(46//div,282//div):['B','S','L'],(47//div,354//div):['B','C','L'],(44//div,423//div):['G','C','M']}

p2={(254//div,79//div):['G','T','M'],(533//div,78//div):['B','S','L'],(185//div,211//div):['B','S','L'],
(260//div,286//div):['B','C','L'],(256//div,353//div):['G','T','M'],(394//div,355//div):['R','S','L'],
(115//div,423//div):['G','C','M'],(396//div,424//div):['B','T','L'],(596//div,418//div):['R','T','L']}#(4,2):['G','S','L']}
p3=[(189//div,143//div),(330//div,283//div),(596//div,353//div)]


DOOROCCUPIED={}
for i in p1:
    DOOROCCUPIED[i]=False

def doorfull():
    full=True
    for i in DOOROCCUPIED:
        if DOOROCCUPIED[i]==False:
            full=False
            break
    return(full)




for i in range(1,480//div+1):
    for j in range(1,640//div+1):
        p[(j,i)]=['2']
for i in range(47//div,449//div+1):
    for j in range(14//div,622//div+1):
        p[(j,i)]=['0']

def enlargeobjects(p2):
    global p,k

    for i in p2:
        x=i[0]
        y=i[1]
        for X in range(x-k,x+k+1):
            p[(X,y-k)]=['#']
        for X in range(x-k,x+k+1):
            p[(X,y+k)]=['#']
        for Y in range(y-k,y+k+1):
            p[(x-k,Y)]=['#']
        for Y in range(y-k,y+k+1):
            p[(x+k,Y)]=['#']
        j=k-1
        for X in range(x-j,x+j+1):
            p[(X,y-j)]=['1']
        for X in range(x-j,x+j+1):
            p[(X,y+j)]=['1']
        for Y in range(y-j,y+j+1):
            p[(x-j,Y)]=['1']
        for Y in range(y-j,y+j+1):
            p[(x+j,Y)]=['1']



def mapobjectstopoints(t):
    global k
    s=set()
    x=t[0]
    y=t[1]
    for X in range(x-k,x+k+1):
        s.add((X,y-k))
    for X in range(x-k,x+k+1):

        s.add((X,y+k))
    for Y in range(y-k,y+k+1):

        s.add((x-k,Y))
    for Y in range(y-k,y+k+1):

        s.add((x+k,Y))
    return(s)
def mappointstoobjects(t):
    global k,p2
    s=mapobjectstopoints(t)

    for i in s:
        if i in p2:
            return(i)
def mappointstodoor(t,ends):
    global k,p1
    s=mapobjectstopoints(t)
    for i in s:
        if i in p1 and i in ends:
            return(i)

def enlargeobstacles(p3):
    global p,k

    for i in p3:
        x=i[0]
        y=i[1]
        for X in range(x-k,x+k+1):
            p[(X,y-k)]=['2']
        for X in range(x-k,x+k+1):
            p[(X,y+k)]=['2']
        for Y in range(y-k,y+k+1):
            p[(x-k,Y)]=['2']
        for Y in range(y-k,y+k+1):
            p[(x+k,Y)]=['2']

enlargeobjects(p2)
enlargeobstacles(p3)

#print(p[(10,17)])
p4={}
objects=set()
for i in p2:
    AA=set()
    for j in p1:
        if p2[i]==p1[j]:
            AA.add(j)
            objects.add(i)
    p4[i]=AA
P2=set(p2.keys())
enlargeobstacles(P2.difference(objects))
for i in p:
    for j in range(8):
        p[i].append([0,0])


def lookup(x,y):
        if (x <= 0) or (y <= 0) or (x > 640//div) or (y > 480//div) or p[(x,y)][0] == '1' or p[(x,y)][0] == '2' :
            return 0
        else:
            return [x,y]
def link(px):
    for t in px:
        x=t[0]
        y=t[1]

        if px[t][0] == '1' or px[t][0] == '2':
            px[t][1] = 0
            px[t][2] = 0
            px[t][3] = 0
            px[t][4] = 0
            px[t][5] = 0
            px[t][6] = 0
            px[t][7] = 0
            px[t][8] = 0
            continue

        px[t][1] = lookup(x,y-1)#north
        px[t][2] = lookup(x-1,y)#west
        px[t][3] = lookup(x,y+1)#south
        px[t][4] = lookup(x+1,y)#east
        px[t][5] = lookup(x-1,y-1)#northwest
        px[t][6] = lookup(x-1,y+1)#southwest
        px[t][7] = lookup(x+1,y+1)#southeast
        px[t][8] = lookup(x+1,y-1)#northeast

def removeobjectandlink(t):
    global p,k
    x=t[0]
    y=t[1]
    change=set()
    for j in range(k-1,k+2):
        for X in range(x-j,x+j+1):
            if p[(X,y-j)][0]!='2':
                try:

                    p[(X,y-j)][0]='0'
                except KeyError:
                    pass
        for X in range(x-j,x+j+1):
            if p[(X,y+j)][0]!='2':
                try:
                    p[(X,y+j)][0]='0'
                except KeyError:
                    pass
        for Y in range(y-j,y+j+1):
            if p[(x-j,Y)][0]!='2':
                try:
                    p[(x-j,Y)][0]='0'
                except KeyError:
                    pass

        for Y in range(y-j,y+j+1):
            if p[(x+j,Y)][0]!='2':
                try:
                    p[(x+j,Y)][0]='0'
                except KeyError:
                    pass


    for j in range(k-2,k+2):
        for X in range(x-j,x+j+1):
            change.add((X,y-j))

        for X in range(x-j,x+j+1):
            change.add((X,y+j))

        for Y in range(y-j,y+j+1):
            change.add((x-j,Y))

        for Y in range(y-j,y+j+1):
            change.add((x+j,Y))


    ##print(change)
    ##print('')
    #print('')
    #print('')
    #print(p[10,17])

    for q in change:
        x=q[0]
        y=q[1]
        if(x<640//div and y<480//div and x>0 and y>0):
            if p[q][0] == '1' and p[q][0] == '2':
                p[q][1] = 0
                p[q][2] = 0
                p[q][3] = 0
                p[q][4] = 0
                p[q][5] = 0
                p[q][6] = 0
                p[q][7] = 0
                p[q][8] = 0
                continue

            p[q][1] = lookup(x,y-1)#north
            p[q][2] = lookup(x-1,y)#west
            p[q][3] = lookup(x,y+1)#south
            p[q][4] = lookup(x+1,y)#east
            p[q][5] = lookup(x-1,y-1)#northwest
            p[q][6] = lookup(x-1,y+1)#southwest
            p[q][7] = lookup(x+1,y+1)#southeast
            p[q][8] = lookup(x+1,y-1)#northeast
def addobstacleandlink(t):
    global p,k
    x=t[0]
    y=t[1]
    change=set()
    for X in range(x-k,x+k+1):
        try:
            p[(X,y-k)][0]='2'
        except KeyError:
            pass

    for X in range(x-k,x+k+1):
        try:
            p[(X,y+k)][0]='2'
        except KeyError:
            pass
    for Y in range(y-k,y+k+1):
        try:
            p[(x-k,Y)][0]='2'
        except KeyError:
            pass

    for Y in range(y-k,y+k+1):
        try:
            p[(x+k,Y)][0]='2'
        except KeyError:
            pass

    #p[(x+k-1,y)][0]=['0']
    #p[(x-k+1,y)][0]=['0']
    #p[(x,y+k-1)][0]=['0']
    #p[(x,y-k+1)][0]=['0']
    for j in range(k-1,k+2):
        for X in range(x-j,x+j+1):
            change.add((X,y-j))

        for X in range(x-j,x+j+1):
            change.add((X,y+j))

        for Y in range(y-j,y+j+1):
            change.add((x-j,Y))

        for Y in range(y-j,y+j+1):
            change.add((x+j,Y))
    #change.add((x+k-2,y))
    #change.add((x-k+2,y))
    #change.add((x,y+k-2))
    #change.add((x,y-k+2))
    for q in change:
        x=q[0]
        y=q[1]
        if(x<640//div and y<480//div and x>0 and y>0):
            if p[q][0] == '1' or p[q][0] == '2':
                p[q][1] = 0
                p[q][2] = 0
                p[q][3] = 0
                p[q][4] = 0
                p[q][5] = 0
                p[q][6] = 0
                p[q][7] = 0
                p[q][8] = 0
                continue

            p[q][1] = lookup(x,y-1)#north
            p[q][2] = lookup(x-1,y)#west
            p[q][3] = lookup(x,y+1)#south
            p[q][4] = lookup(x+1,y)#east
            p[q][5] = lookup(x-1,y-1)#northwest
            p[q][6] = lookup(x-1,y+1)#southwest
            p[q][7] = lookup(x+1,y+1)#southeast
            p[q][8] = lookup(x+1,y-1)#northeast

link(p)

def neighbours(t,px):

        neighbour = set()

        if px[t][1] != 0:
            neighbour.add(tuple(px[t][1]))
        if px[t][2] != 0:
            neighbour.add(tuple(px[t][2]))
        if px[t][3] != 0:
            neighbour.add(tuple(px[t][3]))
        if px[t][4] != 0:
            neighbour.add(tuple(px[t][4]))
        if px[t][5] != 0:
            neighbour.add(tuple(px[t][5]))
        if px[t][6] != 0:
            neighbour.add(tuple(px[t][6]))
        if px[t][7] != 0:
            neighbour.add(tuple(px[t][7]))
        if px[t][8] != 0:
            neighbour.add(tuple(px[t][8]))

        return neighbour

def neighboursoblique(t,px):
        neighbouroblique = set()
        if px[t][5] != 0:
            neighbouroblique.add(tuple(px[t][5]))
        if px[t][6] != 0:
            neighbouroblique.add(tuple(px[t][6]))
        if px[t][7] != 0:
            neighbouroblique.add(tuple(px[t][7]))
        if px[t][8] != 0:
            neighbouroblique.add(tuple(px[t][8]))
        return neighbouroblique



def ABS(k):
    if(k!=0):
        return(abs(k))
    else:
        return(1)

def findnearest(start):
    global p,p2
    #print('starting from',start)
    stop=set()
    #print(objects)
    for i in objects:
        if len(p4[i])!=0:
            stop.add(i)
    if(len(stop)==0):
        return('NO OBJECT FOUND')
    #print('$$$',stop)
    stops=set()
    for i in stop:
        stops.update(mapobjectstopoints(i))
    #print('@@@',stops)
    def path(current_node):
        return_path=[]
        cur=current_node
        while(cur!=start):
            return_path.append(cur)
            cur=parent[cur]
        return_path.append(start)
        return_path.reverse()
        return(return_path)
    def h(t):
        return(0)

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
    pathexists=False
    while ((len(opened) > 0) and (stops.isdisjoint(closed))):


            fsort = sorted(f, key=lambda t:fscore(t))
            i = 0

            for i in range(len(fsort)-1):
                if(fsort[i] not in closed):
                    break
            current = fsort[i]


            if current in stops:
                pathexists=True
                s=path(current)
                end=current
                s1=tuple(s)
                s1=list(s1)
                s2=[]
                i=0
                while(i<len(s)-1):
                    s2.append(s1[i])
                    j=i+2

                    if(j>=len(s1)):
                       break
                    X=(s1[j][0]-s1[i][0])/ABS(s1[j][0]-s1[i][0])
                    Y=(s1[j][1]-s1[i][1])/ABS(s1[j][1]-s1[i][1])
                    reachedend=False
                    while(j<len(s1)):
                        X1=(s1[j][0]-s1[j-1][0])/ABS(s1[j][0]-s1[j-1][0])
                        Y1=(s1[j][1]-s1[j-1][1])/ABS(s1[j][1]-s1[j-1][1])

                        if((X,Y)==(X1,Y1)):
                            j+=1
                        else:
                            i=j-1
                            break
                        if(j==len(s1)):
                            reachedend=True

                    if(reachedend):
                        break
                s2.append(s1[-1])
                #print('$$$$$',s2)



                #print('Reached object at',end)

            for neighbour in neighbours(current,p):
                if neighbour not in closed:
                    if neighbour in neighboursoblique(current,p):
                        temp_g = g[current] + 1.414
                    else:
                        temp_g = g[current] + 1

                    temp_f = temp_g+h(neighbour)


                    if (neighbour not in opened) or  (temp_f < f[neighbour]):
                        # if the neighbour node has not yet been evaluated yet, then we evaluate it
                        # or, if we have just found a shorter way to reach neighbour from the start node,
                        # then we replace the previous route to get to neighbour, with this new quicker route
                        parent[neighbour] = current
                        g[neighbour] = temp_g
                        f[neighbour] = fscore(neighbour)

                        if neighbour not in opened:
                            opened.add(neighbour)

            opened.discard(current)
            f.pop(current)
            closed.add(current)

    if(pathexists):
        print(p2[mappointstoobjects(end)],'picked from',mappointstoobjects(end))
        removeobjectandlink(mappointstoobjects(end))

        objects.discard(mappointstoobjects(end))


        #s.remove(end)
        endb4=s[-2]
        #s.append(d1[(Y,X)])
        #print(s)


        return([endb4,mappointstoobjects(end),s,s2])
    else:
        print('NO PATH')
        return('NO PATH')


def deposit(startlist):
    global p1,p2

    ptemp=deepcopy(dict(p))
    #print(p==ptemp)
    Ldash=set()
    for i in ptemp:
        if(ptemp[i][0]=='#'):
            ptemp[i][0]='1'
            Ldash.add(i)
    L=set()
    for i in Ldash:
        for j in range(i[0]-1,i[0]+2):
            for q in range(i[1]-1,i[1]+2):
                L.add((j,q))


    for t in L:
        x=t[0]
        y=t[1]
        if(x<640//div and y<480//div and x>0 and y>0):
            if ptemp[t][0] == '1':
                ptemp[t][1] = 0
                ptemp[t][2] = 0
                ptemp[t][3] = 0
                ptemp[t][4] = 0
                ptemp[t][5] = 0
                ptemp[t][6] = 0
                ptemp[t][7] = 0
                ptemp[t][8] = 0

                continue

            ptemp[t][1] = lookup(x,y-1)#north
            ptemp[t][2] = lookup(x-1,y)#west
            ptemp[t][3] = lookup(x,y+1)#south
            ptemp[t][4] = lookup(x+1,y)#east
            ptemp[t][5] = lookup(x-1,y-1)#northwest
            ptemp[t][6] = lookup(x-1,y+1)#southwest
            ptemp[t][7] = lookup(x+1,y+1)#southeast
            ptemp[t][8] = lookup(x+1,y-1)#northeast
    #print(p==ptemp)
    start=startlist[0]
    endss=set()
    ends=tuple(p4[startlist[1]])
    if (len(ends)==1):
        STOP1=True
        END=ends[0]
    else:
        STOP1=False

    for i in ends:
        endss.update(mapobjectstopoints(i))

    for t in p4[startlist[1]]:

        x=t[0]
        y=t[1]
        change=set()
        for X in range(x-k,x+k+1):
            try:
                ptemp[(X,y-k)][0]='#'
            except KeyError:
                pass

        for X in range(x-k,x+k+1):
            try:
                ptemp[(X,y+k)][0]='#'
            except KeyError:
                pass
        for Y in range(y-k,y+k+1):
            try:
                ptemp[(x-k,Y)][0]='#'
            except KeyError:
                pass

        for Y in range(y-k,y+k+1):
            try:
                ptemp[(x+k,Y)][0]='#'
            except KeyError:
                pass


        #p[(x+k-1,y)][0]=['0']
        #p[(x-k+1,y)][0]=['0']
        #p[(x,y+k-1)][0]=['0']
        #p[(x,y-k+1)][0]=['0']
        for j in range(k-1,k+2):
            for X in range(x-j,x+j+1):
                change.add((X,y-j))

            for X in range(x-j,x+j+1):
                change.add((X,y+j))

            for Y in range(y-j,y+j+1):
                change.add((x-j,Y))

            for Y in range(y-j,y+j+1):
                change.add((x+j,Y))
        #change.add((x+k-2,y))
        #change.add((x-k+2,y))
        #change.add((x,y+k-2))
        #change.add((x,y-k+2))
        for q in change:
            x=q[0]
            y=q[1]
            if(x<640//div and y<480//div and x>0 and y>0):

                if ptemp[q][0] == '1' or ptemp[q][0] == '2':
                    ptemp[q][1] = 0
                    ptemp[q][2] = 0
                    ptemp[q][3] = 0
                    ptemp[q][4] = 0
                    ptemp[q][5] = 0
                    ptemp[q][6] = 0
                    ptemp[q][7] = 0
                    ptemp[q][8] = 0
                    continue

                ptemp[q][1] = lookup(x,y-1)#north
                ptemp[q][2] = lookup(x-1,y)#west
                ptemp[q][3] = lookup(x,y+1)#south
                ptemp[q][4] = lookup(x+1,y)#east
                ptemp[q][5] = lookup(x-1,y-1)#northwest
                ptemp[q][6] = lookup(x-1,y+1)#southwest
                ptemp[q][7] = lookup(x+1,y+1)#southeast
                ptemp[q][8] = lookup(x+1,y-1)#northeast

    def path(current_node):
        return_path=[]
        cur=current_node
        while(cur!=start):
            return_path.append(cur)
            cur=parent[cur]
        return_path.append(start)
        return_path.reverse()
        return(return_path)
    def h(t):
        if(STOP1):
            return((t[0]-END[0])*(t[0]-END[0])+(t[1]-END[1])*(t[1]-END[1]))
        else:
            return(0)

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
    pathexists=False
    #print(ptemp[(2,1)])
    while ((len(opened) > 0) and (endss.isdisjoint(closed))):


            fsort = sorted(f, key=lambda t:fscore(t))
            i = 0
            for i in range(len(fsort)-1):
                if(fsort[i] not in closed):
                    break
            current = fsort[i]

            if current in endss:


                pathexists=True
                s=path(current)
                s1=tuple(s)
                s1=list(s1)
                s2=[]
                i=0
                while(i<len(s)-1):
                    s2.append(s1[i])
                    j=i+2

                    if(j>=len(s1)):
                       break
                    X=(s1[j][0]-s1[i][0])/ABS(s1[j][0]-s1[i][0])
                    Y=(s1[j][1]-s1[i][1])/ABS(s1[j][1]-s1[i][1])
                    reachedend=False
                    while(j<len(s1)):
                        X1=(s1[j][0]-s1[j-1][0])/ABS(s1[j][0]-s1[j-1][0])
                        Y1=(s1[j][1]-s1[j-1][1])/ABS(s1[j][1]-s1[j-1][1])

                        if((X,Y)==(X1,Y1)):
                            j+=1
                        else:
                            i=j-1
                            break
                        if(j==len(s1)):
                            reachedend=True

                    if(reachedend):
                        break
                s2.append(s1[-1])
                #print('$$$$$',s2)


                end=current
                print('Reached',end)
                #print(mappointstoobjects(end))



            #print(opened)
            #print("neighbours= ",neighbours(current,ptemp))

            for neighbour in neighbours(current,ptemp):
                if neighbour not in closed:
                    if neighbour in neighboursoblique(current,ptemp):
                        temp_g = g[current] + 1.414
                    else:
                        temp_g = g[current] + 1
                    temp_f = temp_g+h(neighbour)



                    if (neighbour not in opened) or  (temp_f < f[neighbour]):

                        # if the neighbour node has not yet been evaluated yet, then we evaluate it
                        # or, if we have just found a shorter way to reach neighbour from the start node,
                        # then we replace the previous route to get to neighbour, with this new quicker route
                        parent[neighbour] = current

                        g[neighbour] = temp_g
                        f[neighbour] = fscore(neighbour)

                        if neighbour not in opened:
                            opened.add(neighbour)
            opened.discard(current)
            f.pop(current)
            closed.add(current)




    if(pathexists):
        print(p1[mappointstodoor(end,ends)],'deposited at',mappointstodoor(end,ends))
        #p[end][0]='1'
        #print('1',p[(5,22)])
        #print('1',mappointstodoor(end,ends))
        DOOROCCUPIED[mappointstodoor(end,ends)]=True
        #print('1',mappointstodoor(end,ends))

        for i in p4:
            p4[i].discard(mappointstodoor(end,ends))
        #print('2',mappointstodoor(end,ends))
        #print(type(mappointstodoor(end,ends)))
        addobstacleandlink(mappointstodoor(end,ends))

        #print(p[(6,22)])
        #INPUT=int(input('continue'))
        #print('2',p[(5,22)])
        #s.remove(end)
        endb4=s[-2]
        #print(s)
        return([endb4,mappointstodoor(end,ends),s,s2])
    else:

        return('NO PATH')





masterRoute=[]

#goto(START[0],START[1])
#tr.penup()
m1=[]

plist=[]
dlist=[]
def path_plan(currentPos):
    while((not doorfull()) and len(objects)>0):

        q=findnearest(currentPos)

        masterRoute.append(q[2])
        m1.extend(q[3])
        m1.append('p')
        plist.append(q[1])

        w=deposit(q)

        m1.extend(w[3])
        masterRoute.append(w[2])

        m1.append('d')
        dlist.append(w[1])
        currentPos=w[0]



    m2=[]
    for i in m1:
        if type(i)==tuple:
            x=i[0]*div
            y=i[1]*div
            m2.append((x,y))
        else:
            m2.append(i)
    return(m2)
path=path_plan(START)
print path
