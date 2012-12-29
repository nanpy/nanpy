from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class CapacitiveSensor(ArduinoObject):

    def __init__(self, pin1, pin2):
        ArduinoObject.__init__(self)
        self.id = self.call('new', pin1, pin2)

    @returns(int)
    @arduinoobjectmethod
    def capacitiveSensor(self, samples):
        pass

    @returns(int)
    @arduinoobjectmethod
    def capacitiveSensorRaw(self, samples):
        pass

