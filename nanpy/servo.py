from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class Servo(ArduinoObject):

    def __init__(self, pin):
        ArduinoObject.__init__(self)
        self.id = self.call('new', pin)

    @arduinoobjectmethod
    def write(self, value):
        pass

    @returns(int)
    @arduinoobjectmethod
    def read(self):
        pass

    @arduinoobjectmethod
    def writeMicroseconds(self, value):
        pass

    @returns(int)
    @arduinoobjectmethod
    def readMicroseconds(self, value):
        pass

    @arduinoobjectmethod
    def attached(self):
        pass
