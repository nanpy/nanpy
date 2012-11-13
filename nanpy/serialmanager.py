import serial
import time
import fnmatch
import sys

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
            self._serial = serial.Serial(available_ports[0], 9600, timeout=1)
            time.sleep(2)
        except:
            print("Error trying to connect to Arduino")
            self._serial = NoneSerialManager()

    def connect(self, device):
        self._serial = serial.Serial(device, 9600)
        time.sleep(2)

    def write(self, value):
        self._serial.write(bytes(value, 'latin-1'))

    def readline(self):
        return self._serial.readline().decode()

class SerialManagerPy2(SerialManager):

    def __init__(self):
        SerialManager.__init__(self)

    def write(self, value):
        self._serial.write(value)

if sys.version_info.major == 2:
    serial_manager = SerialManagerPy2()
elif sys.version_info.major == 3:
    serial_manager = SerialManager()

