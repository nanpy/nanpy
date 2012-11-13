from nanpy.serialmanager import serial_manager
from threading import Lock

mutex = Lock()

def _write(data):
    serial_manager.write('%s\0' % str(data))

def return_value():
    return serial_manager.readline().replace('\r\n', '')

def _call(namespace, id, args):

    toprint = []
    nel = 0

    mutex.acquire()
    _write(namespace)
    _write(id)

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

    ret = return_value()
    mutex.release()
    return ret

def returns(fconv):
    def wrapf(func):
        def wrapper(self, *args, **kwargs):
            try:
                return fconv(func(self, *args, **kwargs))
            except ValueError:
                return -1
        return wrapper
    return wrapf

def arduinoobjectmethod(funct, *args, **kwargs):
    def wrapper(self, *args, **kwargs):
        call_pars = [funct.__name__]
        call_pars.extend(args)
        funct(self, *args, **kwargs)
        return _call(self.namespace, self.id, call_pars)
    return wrapper

def arduinoclassmethod(funct):
    def wrapper(cls, *args, **kwargs):
        call_pars = [funct.__name__]
        call_pars.extend(args)
        funct(cls, *args, **kwargs)
        return _call(cls.__name__, 0, call_pars)
    return wrapper

class ArduinoObject():

    def __init__(self):
        self.namespace = self.__class__.__name__
        self.id = 0

    def call(self, *args):
        return _call(self.namespace, self.id, args)

    def __del__(self):
        return _call(self.namespace, self.id, ["remove"])

