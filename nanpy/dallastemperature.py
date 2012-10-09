from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, arduinoclassmethod, returns)

class DallasTemperature(ArduinoObject):

    def __init__(self, pin):
        ArduinoObject.__init__(self)
        self.id = self.call('new', pin)

    @arduinoobjectmethod
    def requestTemperatures(self):
        pass

    @returns(float)
    @arduinoobjectmethod
    def getTempCByIndex(self, index):
        pass

    @returns(float)
    @arduinoobjectmethod
    def getTempFByIndex(self, index):
        pass

    @classmethod
    @returns(float)
    @arduinoclassmethod
    def toCelsius(cls, value):
        pass

    @classmethod
    @returns(float)
    @arduinoclassmethod
    def toFahrenheit(cls, value):
        pass

