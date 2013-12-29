from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class DHT(ArduinoObject):

    DHT11 = 11
    DHT22 = 22
    DHT21 = 21
    AM2301 = 21

    def __init__(self, pin, _type, count = 6):
        ArduinoObject.__init__(self)
        self.id = self.call('new', pin, _type, count)

    @returns(int)
    @arduinoobjectmethod
    def begin(self):
        pass

    @returns(float)
    @arduinoobjectmethod
    def readHumidity(self):
        pass

    @returns(float)
    @arduinoobjectmethod
    def readTemperature(self, value = False):
        pass
