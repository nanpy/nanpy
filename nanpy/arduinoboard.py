from nanpy.serialmanager import serial_manager

def _write( data):
    serial_manager.write('%s\0' % data)

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

def _call(namespace, id, args):
    _write(namespace)
    _write(id)
    _send_parameters(args)
    return return_value()

def call_static_method(*args):
    return _call(args[0], 0, args[1:])


class ArduinoObject():

    def __init__(self, namespace, single=False):
        self.namespace = namespace
        self.single = single
        self.id = 0

    def return_value(self):
        return return_value()

    def call(self, *args):
        return _call(self.namespace, self.id, args)

    def __del__(self):
        return _call(self.namespace, self.id, ["remove"])

