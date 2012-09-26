from nanpy.serialmanager import serial_manager

def _write( data):
    data = str(data)
    for ch in data:
        serial_manager.write('%c' % ch)
    serial_manager.write('\0')

def _read():
    return serial_manager.readline()

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

def call_static_method(*args):
    _write(args[0])
    _write(0)
    _send_parameters(args[1:])

class ArduinoObject():

    def __init__(self, namespace, single=False):
        self.namespace = namespace
        self.single = single
        self.id = 0

    def return_value(self):
        return return_value()

    def call(self, *args):
        _write(self.namespace)
        _write(self.id)
        _send_parameters(args)

