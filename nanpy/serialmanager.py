import serial
import time
import fnmatch
import sys

DEFAULT_BAUDRATE = 9600


class SerialManagerError(Exception):
    pass


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
    
    def __init__(self, device=None, baudrate=DEFAULT_BAUDRATE):
        self.baudrate = baudrate
        if device:
            self.connect(device)
        else:
            # auto detection?
            available_ports = _auto_detect_serial_unix()
            try:
                self.connect(available_ports[0])
            except:
                print("Error trying to connect to Arduino")
                self._serial = NoneSerialManager()

    def connect(self, device):
        self._serial = serial.Serial(device, self.baudrate, timeout=1)
        time.sleep(2)

    def write(self, value):
        self._serial.write(bytes(value, 'latin-1'))

    def readline(self):
        s = self._serial.readline().decode()
        if not len(s):
            raise SerialManagerError('Serial timeout!')
        return s
    
    
class SerialManagerPy2(SerialManager):

    def __init__(self):
        SerialManager.__init__(self)

    def write(self, value):
        self._serial.write(value)

if sys.version_info[0] == 2:
    serial_manager = SerialManagerPy2()
elif sys.version_info[0] == 3:
    serial_manager = SerialManager()

