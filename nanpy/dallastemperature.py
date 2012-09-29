from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import arduinoobjectmethod

class DallasTemperature(ArduinoObject):

    def __init__(self, pin):
        ArduinoObject.__init__(self)
        self.id = self.call('new', pin)

    @arduinoobjectmethod
    def begin(self):
        pass

    @arduinoobjectmethod
    def requestTemperatures(self):
        pass

    @arduinoobjectmethod
    def getTempCByIndex(self, index):
        pass

    @arduinoobjectmethod
    def getTempFByIndex(self, index):
        pass
