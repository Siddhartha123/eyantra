def grid_to_map(l,length,breadth):
    #l-->[0,0](example)
    X=length/2+l[0]*length
    Y=breadth/2+l[1]*breadth
    return X,Y

def color(px):
    # px is  a list, where px[0]=B, px[1]=G, px[2]=R
    b=px[0]
    g=px[1]
    r=px[2]
    if b>=130 and b<=170:
        if g>=90 and g<=140:
            if r>=175 and r<=200:
                return 'pink'
    if b>=0 and b<=120:
        if g>=210 and g<=255:
            if r>=210 and r<=255:
                return 'yellow'
    
def direction(l1,l2):
    #l1-->co-ord of yellow marker
    #l2-->co-ord of pink marker
    #l1[0]->x co-ord, l1[1]->y co-ord
    #    N
    #W __|__ E
    #    |
    #    S
    if abs(l1[0]-l2[0])<=10:
        if (l2[1]-l1[1])>=0:
            return 'north'
        else:
            return 'south'
    elif abs(l1[1]-l2[1])<=10:
        if l1[0]>l2[0]:
            return 'east'
        else:
            return 'west'
    else:
    	return 'undefined'
            
    
    
     
