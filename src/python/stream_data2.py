import numpy
import matplotlib.pyplot as plt
import serial
from serial_data import arduino_serial_port
from drawnow import *


temp_contact = []
temp_ambient = []
pwm = []
plt.ion()
count = 0



def figure():
    plt.title('Streaming Sensor Data')
    plt.grid(True)
    plt.ylim(15,80)
    plt.ylabel('Contact')
    plt.plot(temp_contact, 'ro-', label="C")
    plt.legend(loc="upper left")

    plt2=plt.twinx()
    plt.ylim(15,80)
    plt2.plot(temp_ambient, 'b^-', label='C')
    plt2.set_ylabel('Ambient')
    plt2.ticklabel_format(useOffset=False)
    plt2.legend(loc="upper right")

    #plt3=plt.twinx()
    #plt.ylim(0,255)
    #plt3.plot(pwm, 'b--', label="?")
    #plt3.ticklabel_format(useOffset=False)
    #plt3.legend(loc="lower right")

def waitForDataFromArduino(serialIn):
    while(serialIn.inWaiting() == 0):
        pass
    return serialIn.readline().split(',')


def main():
    with serial.Serial() as ser:
        ser.baudrate = 9600
        ser.port = arduino_serial_port()
        ser.open()

        while True:
            data = waitForDataFromArduino(ser)
            current_temp_contact = float( data[0] )
            current_temp_ambient = float( data[1] )
            current_pwm = float( data[2] )
            temp_contact.append(current_temp_contact)
            temp_ambient.append(current_temp_ambient)
            #pwm.append(current_pwm)
            delta = current_temp_contact - current_temp_ambient
            print "pwm:{0} ambient:{1} contact:{2} delta:{3}".format(current_pwm, current_temp_ambient, current_temp_contact, delta)
            drawnow(figure)
            plt.pause(.000001)
            ++count
            if(count>50):
                temp_contact.pop(0)
                temp_ambient.pop(0)
            #    pwm.pop(0)



if __name__ == '__main__':
    main()
