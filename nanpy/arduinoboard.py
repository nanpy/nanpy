from nanpy.serialmanager import serial_manager
from threading import Lock

mutex = Lock()

def _write( data):
    data = str(data)
    for ch in data:
        serial_manager.write('%c' % ch)
    serial_manager.write('\0')

def _send_parameters(args):
    toprint = []
    nel = 0
    for arg in args:
        if type(arg) == type(list()):
            for el in arg:
                if el != None:
                    toprint.append(el)
                    nel += 1
        else:
            if arg != None:
                toprint.append(arg)
                nel += 1

    _write(nel - 1)

    for elprint in toprint:
        _write(elprint)

def return_value():
    return serial_manager.readline().replace("\r\n","")

def arduinoclassmethod(funct, *args, **kwargs):
    def wrapper(self, *args, **kwargs):
        call_pars = [funct.__name__]
        call_pars.extend(args)
        return _call(self.namespace, self.id, call_pars)
    return wrapper

def _call(namespace, id, args):
    mutex.acquire()
    _write(namespace)
    _write(id)
    _send_parameters(args)
    ret = return_value()
    mutex.release()
    return ret

def call_static_method(*args):
    return _call(args[0], 0, args[1:])


class ArduinoObject():

    def __init__(self):
        self.namespace = self.__class__.__name__
        self.id = 0

    def call(self, *args):
        return _call(self.namespace, self.id, args)

    def __del__(self):
        return _call(self.namespace, self.id, ["remove"])

