from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returnfloat)

class DallasTemperature(ArduinoObject):

    def __init__(self, pin):
        ArduinoObject.__init__(self)
        self.id = self.call('new', pin)

    @arduinoobjectmethod
    def requestTemperatures(self):
        pass

    @returnfloat
    @arduinoobjectmethod
    def getTempCByIndex(self, index):
        pass

    @returnfloat
    @arduinoobjectmethod
    def getTempFByIndex(self, index):
        pass
