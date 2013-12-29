from nanpy.serialmanager import serial_manager
from threading import Lock

mutex = Lock()


def _write(data, connection):
    if connection:
        connection.write('%s\0' % str(data))
    else:
        serial_manager.write('%s\0' % str(data))


def return_value(connection):
    if connection:
        return connection.readline().replace('\r\n', '')
    else:
        return serial_manager.readline().replace('\r\n', '')


def _call(namespace, id, args, connection):

    toprint = []
    nel = 0

    mutex.acquire()
    _write(namespace, connection)
    _write(id, connection)

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

    _write(nel - 1, connection)

    for elprint in toprint:
        _write(elprint, connection)

    ret = return_value(connection)
    mutex.release()
    return ret


def returns(fconv):
    def wrapf(func):
        def wrapper(self, *args, **kwargs):
#             try:
                return fconv(func(self, *args, **kwargs))
#             except ValueError:
#                 return -1
        return wrapper
    return wrapf


def arduinoobjectmethod(funct, *args, **kwargs):
    def wrapper(self, *args, **kwargs):
        call_pars = [funct.__name__]
        call_pars.extend(args)
        funct(self, *args, **kwargs)
        connection = self.connection if hasattr(self, 'connection') else None
        return _call(self.namespace, self.id, call_pars, connection=connection)
    return wrapper

# def arduinoclassmethod(funct):
#     def wrapper(cls, *args, **kwargs):
#         call_pars = [funct.__name__]
#         call_pars.extend(args)
#         funct(cls, *args, **kwargs)
#         return _call(cls.__name__, 0, call_pars)
#     return wrapper


def class_get_firmware_id(cls):
    if hasattr(cls, 'get_firmware_id'):
        return cls.get_firmware_id()
    elif hasattr(cls, 'firmware_id'):
        return cls.firmware_id
    else:
        return cls.__name__


def arduinoclassmethod(param):
    is_func = hasattr(param, '__call__')
    if is_func:
        funct = param

        def wrapper(cls, *args, **kwargs):
            cls_name = class_get_firmware_id(cls)
            call_pars = [funct.__name__]
            call_pars.extend(args)
            funct(cls, *args, **kwargs)
            return _call(cls_name, 0, call_pars, connection=None)
        return wrapper
    else:
        name = param

        def wrapper2(funct):
            def wrapper(cls, *args, **kwargs):
                cls_name = class_get_firmware_id(cls)
                call_pars = [name]
                call_pars.extend(args)
                funct(cls, *args, **kwargs)
                return _call(cls_name, 0, call_pars, connection=None)
            return wrapper
        return wrapper2


def _wrapper3(name):
    def wrapper2(funct):
        def wrapper(obj, *args, **kwargs):
            cls_name = class_get_firmware_id(obj.__class__)
            connection = obj.connection if hasattr(obj, 'connection') else None
            call_pars = [name if name else funct.__name__]
            call_pars.extend(args)
            funct(obj, *args, **kwargs)
            return _call(cls_name, 0, call_pars, connection=connection)
        return wrapper
    return wrapper2


def arduinomethod(param):
    is_func = hasattr(param, '__call__')
    if is_func:
        funct = param
        name = None
        return _wrapper3(name)(funct)
    else:
        name = param
        return _wrapper3(name)


class ArduinoObject(object):
    connection=None

    def __init__(self, connection=None):
        self.namespace = self.__class__.__name__
        self.id = 0
        self.connection = connection

    def call(self, *args):
        return _call(self.namespace, self.id, args, self.connection)

    def __del__(self):
        return _call(self.namespace, self.id, ["remove"], self.connection)


class FirmwareClass(object):
    connection = None
    firmware_id = None

    @classmethod
    def get_firmware_id(cls):
        if cls.firmware_id:
            return cls.firmware_id
        else:
            return cls.__name__

    def __init__(self, connection=None):
        self.connection = connection


