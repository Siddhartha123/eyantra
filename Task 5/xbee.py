from serialCom import *
serialInit()
while True:
    l=int(raw_input("left speed"))
    r=int(raw_input("right speed"))
    velocity(l,r)
