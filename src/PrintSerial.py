import serial

with serial.Serial() as ser:
    ser.baudrate = 9600
    ser.port = '/dev/cu.usbmodem1411'
    ser.open()
    
    while(True):
        if (ser.inWaiting() > 0):
            myData = ser.readline()
            print myData
