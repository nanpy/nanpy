from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returnint)

class OneWireAddress():

    def __init__(self, bytes):
        self.__bytes = bytes

    def get(self):
        return self.__bytes

class OneWire(ArduinoObject):
    
    def __init__(self, pin):
        ArduinoObject.__init__(self)
        self.id = self.call('new', pin)

    def search(self):
        val = self.call('search')
        if val == "1":
            return val
        return OneWireAddress(val.split(" "))

    def select(self, address):
        return self.call('select', address.get())

    @returnint
    @arduinoobjectmethod
    def read(self):
        pass

    @arduinoobjectmethod
    def reset_search(self):
        pass

    @arduinoobjectmethod
    def reset(self):
        pass

    @arduinoobjectmethod
    def write(self, address, value=None):
        pass

