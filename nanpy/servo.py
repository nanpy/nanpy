from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returnint)

class Servo(ArduinoObject):

    def __init__(self, pin):
        self.id = self.call('new', pin)

    @arduinoobjectmethod
    def write(self, value):
        pass

    @returnint
    @arduinoobjectmethod
    def read(self):
        pass

    @arduinoobjectmethod
    def writeMicroseconds(self, value):
        pass

    @returnint
    @arduinoobjectmethod
    def readMicroseconds(self, value):
        pass

    @arduinoobjectmethod
    def attached(self):
        pass
