from nanpy.arduinoboard import ArduinoObject

class OneWireAddress():

    def __init__(self, bytes):
        self.__bytes = bytes

    def get(self):
        return self.__bytes

class OneWire(ArduinoObject):
    
    def __init__(self, pin):
        ArduinoObject.__init__(self, "OneWire")
        self.id = self.call('new', pin)

    def search(self):
        val = self.call('search')
        if val == "1":
            return val
        return OneWireAddress(val.split(" "))

    def reset_search(self):
        return self.call('reset_search')

    def reset(self):
        return self.call('reset')

    def select(self, address):
        return self.call('select', address.get())

    def write(self, address, value=None):
        return self.call('write', address, value)

    def read(self):
        return int(self.call('read'))

