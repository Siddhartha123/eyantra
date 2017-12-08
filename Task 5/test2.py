from serialCom import *
while True:
    x=raw_input("Enter command")
    if x=='z':
        break
    robot.write(x)
