from ArduinoObject import ArduinoObject

class OneWireAddress():

    def __init__(self, bytes):
        self.__bytes = bytes

    def get(self):
        return self.__bytes

class OneWire(ArduinoObject):
    
    def __init__(self, pin):
        ArduinoObject.__init__(self, "OneWire")
        self.call('new', pin)
        self.id = self._return_value()

    def search(self):
        self.call('search')
        val = self._return_value()
        if val == "1":
            return val
        else:
            return OneWireAddress(val.split(" "))

    def reset_search(self):
        self.call('reset_search')
        return self._return_value()

    def reset(self):
        self.call('reset')
        self._return_value()

    def select(self, address):
        self.call('select', address.get())
        return self._return_value()

    def write(self, address, value=None):
        self.call('write', address, value)
        return self._return_value()

    def read(self):
        self.call('read')
        return int(self._return_value())

