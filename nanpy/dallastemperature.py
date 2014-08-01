from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, arduinoclassmethod, returns)

class DallasTemperature(ArduinoObject):

    def __init__(self, pin):
        ArduinoObject.__init__(self)
        self.pin = pin
        self.id = self.call('new', pin)

    @arduinoobjectmethod
    def setResolution(self, bits):
        pass

    @returns(int)
    @arduinoobjectmethod
    def getResolution(self, bits):
        pass

    @returns(int)
    @arduinoobjectmethod
    def getDeviceCount(self):
        pass

    @arduinoobjectmethod
    def getAddress(self, index):
        val = self.call('getAddress')
        if val == "1":
            return val
        return val.split(' ')


    @arduinoobjectmethod
    def requestTemperatures(self, address = None):
        pass

    @returns(float)
    @arduinoobjectmethod
    def getTempC(self, address):
        pass

    @returns(float)
    @arduinoobjectmethod
    def getTempF(self, address):
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

