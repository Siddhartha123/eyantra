import serial
robot=serial.Serial('COM5',baudrate=115200,timeout=1)
while True:
    x=raw_input("Enter")
    robot.write(x)
'''
robot.write('w')
robot.write('w')
robot.write('z')
'''
