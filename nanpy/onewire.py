from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import arduinoclassmethod

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

    def read(self):
        return int(self.call('read'))

    @arduinoclassmethod
    def reset_search(self):
        pass

    @arduinoclassmethod
    def reset(self):
        pass

    @arduinoclassmethod
    def write(self, address, value=None):
        pass

