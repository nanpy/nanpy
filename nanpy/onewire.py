from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class OneWire(ArduinoObject):
    
    def __init__(self, pin):
        ArduinoObject.__init__(self)
        self.id = self.call('new', pin)

    def search(self):
        val = self.call('search')
        if val == "1":
            return val
        return val.split(' ')

    @arduinoobjectmethod
    def select(self, address):
        pass

    @returns(int)
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

