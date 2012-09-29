import serial
import time
import fnmatch
import serial

def _auto_detect_serial_unix(preferred_list=['*']):
    import glob
    glist = glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*')
    ret = []

    for d in glist:
        for preferred in preferred_list:
            if fnmatch.fnmatch(d, preferred):
                ret.append(d)
    if len(ret) > 0:
        return ret

    for d in glist:
        ret.append(d)
    return ret

class NoneSerialManager(object):

    def write(self, val):
        pass

    def read(self):
        return ""

    def readline(self):
        return ""
    

class SerialManager(object):
    
    def __init__(self):
        available_ports = _auto_detect_serial_unix()
        try:
            self.__serial = serial.Serial(available_ports[0], 9600, timeout=1)
            time.sleep(2)
        except:
            print "Error trying to connect to Arduino"
            self.__serial = NoneSerialManager()

    def connect(self, device, baud):
        self.__serial = serial.Serial(device, baud)
        time.sleep(2)

    def write(self, value):
        self.__serial.write(value)

    def readline(self):
        return self.__serial.readline()

serial_manager = SerialManager()
