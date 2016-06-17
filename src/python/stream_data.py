import numpy
import matplotlib.pyplot as plt
import serial
from serial_data import arduino_serial_port
from drawnow import *


temp = []
humidity = []
plt.ion()
count = 0



def figure():
    plt.title('Streaming Sensor Data')
    plt.grid(True)
    plt.ylim(15,35)
    plt.ylabel('Temp C')
    plt.plot(temp, 'ro-', label="degree C")
    plt.legend(loc="upper left")

    plt2=plt.twinx()
    plt.ylim(0,100)
    plt2.plot(humidity, 'b^-', label='Humidity')
    plt2.set_ylabel('Humidity')
    plt2.ticklabel_format(useOffset=False)
    plt2.legend(loc="upper right")

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
            currentTemp = float( data[0] )
            currentHumidity = float( data[1] )
            temp.append(currentTemp)
            humidity.append(currentHumidity)
            drawnow(figure)
            plt.pause(.000001)
            ++count
            if(count>50):
                temp.pop(0)
                humidity.pop(0)



if __name__ == '__main__':
    main()
