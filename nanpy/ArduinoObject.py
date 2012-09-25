import Singleton
from SerialManager import *

class ArduinoObject():

    def __init__(self, namespace, single=False):
        self.namespace = namespace
        self.single = single
        self.id = 0

    def _write(self, data):
        data = str(data)
        for ch in data:
            sm.write('%c' % ch)
        sm.write('\0')

    def _read(self):
        return sm.readline()

    def _return_value(self):
        red = sm.readline().replace("\r\n","")
        return red

    def call(self, *args):
        self._write(self.namespace)
        self._write(self.id)
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

        self._write(nel - 1)

        for elprint in toprint:
            self._write(elprint)

class ArduinoSingleObject(ArduinoObject, Singleton.Singleton):
    def __init__(self, namespace):
        Singleton.Singleton.__init__( self )
        ArduinoObject.__init__(self, namespace, True)

