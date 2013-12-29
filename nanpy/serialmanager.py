from nanpy.memo import memoized
import fnmatch
import logging
import serial
import sys
import time

DEFAULT_BAUDRATE = 115200

log = logging.getLogger(__name__)

PY3 = sys.version_info[0] == 3


class SerialManagerError(Exception):
    pass


def _auto_detect_serial_unix(preferred_list=['*']):
    import glob
    glist = glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*')
    glist += ['/dev/ttyS0', '/dev/ttyS1']
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
#         time.sleep(2)
        self.flush_input()

    def write(self, value):
        log.debug('sending:%s' % repr(value))
        if PY3:
            self._serial.write(bytes(value, 'latin-1'))
        else:
            self._serial.write(value)

    def readline(self):
        s = self._serial.readline()
        log.debug('received:%s' % repr(s))
        s = s.decode()
        if not len(s):
            raise SerialManagerError('Serial timeout!')
        return s

    def flush_input(self):
        '''Flush input buffer, discarding all it's contents.'''
        self._serial.flushInput()


# TODO: remove it
# created only for compaibility
class SerialManagerCompatibility(object):
    def __init__(self, device=None, baudrate=DEFAULT_BAUDRATE):
        self.baudrate = baudrate
        self.device = device

    @property
    @memoized
    def manager(self):
        return SerialManager(self.device, self.baudrate)

    def connect(self, device):
        return self.manager.connect(device)

    def write(self, value):
        return self.manager.write(value)

    def readline(self):
        return self.manager.readline()

    def flush_input(self):
        return self.manager.flush_input()

serial_manager = SerialManagerCompatibility()

