import serial

COM=raw_input("Enter COM Port to open\n")
    #global robot
robot=serial.Serial("COM"+COM,baudrate=115200,timeout=1)

def sendByte(x):
    global robot
    robot.write(x)
'''
def velocity(l,r):
    sendByte(45)
    sendByte(l)
    sendByte(43)
    sendByte(r)

def right():
    sendByte(ord('6'))
def left():
    sendByte(ord('4'))
def back():
    sendByte(ord('5'))
def forward():
    sendByte(ord('8'))
'''
#serialInit()
'''
while True:
    x=raw_input("Enter command")
    if x=='z':
        break
    robot.write(x)
'''
