import serial
import serial.tools.list_ports

def serial_ports():
    ports = list(serial.tools.list_ports.comports())

    for port_no, description, address in ports:
        if 'USB' in address:
            return port_no


def print_serial():
    with serial.Serial() as ser:
        ser.baudrate = 9600
        ser.port = serial_ports()
        ser.open()
    
        while(True):
            if (ser.inWaiting() > 0):
                myData = ser.readline()
                print myData



if __name__ == "__main__":
    print_serial()
