from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, arduinoclassmethod, returnfloat, returnint)

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

    @classmethod
    @returnfloat
    @arduinoclassmethod
    def toCelsius(cls, value):
        pass

    @classmethod
    @returnfloat
    @arduinoclassmethod
    def toFahrenheit(cls, value):
        pass

