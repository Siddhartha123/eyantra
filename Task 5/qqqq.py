from serialCom import *
while True:
    x=int(raw_input("enter command"))
    x=ord(x)
    sendByte(x)
