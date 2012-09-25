from SerialManager import *

def _write( data):
    data = str(data)
    for ch in data:
        sm.write('%c' % ch)
        print ch
    sm.write('\0')

def _read():
    return sm.readline()

def call_in_arduino(*args):
    _write(args[0])
    _write(0)
    _send_parameters(args[1:])

def _send_parameters(args):
    print args
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
    return sm.readline().replace("\r\n","")

class ArduinoObject():

    def __init__(self, namespace, single=False):
        self.namespace = namespace
        self.single = single
        self.id = 0

    def _return_value(self):
        return return_value()

    def call(self, *args):
        _write(self.namespace)
        _write(self.id)
        _send_parameters(args)

