import serial
import time

class SerialManager(object):
    
    def __init__(self, device, baud):
        self.__serial = serial.Serial(device, baud)
        time.sleep(2)

    def connect(self, device, baud):
        self.__serial = serial.Serial(device, baud)
        time.sleep(2)

    def write(self, value):
        self.__serial.write(value)

    def readline(self):
        return self.__serial.readline()

serial_manager = SerialManager('/dev/ttyACM0', 9600)
