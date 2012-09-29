from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import arduinoobjectmethod

class Servo(ArduinoObject):

    def __init__(self, pin):
        self.id = self.call('new', pin)

    @arduinoobjectmethod
    def write(self, value):
        pass

    @arduinoobjectmethod
    def read(self):
        pass

    @arduinoobjectmethod
    def writeMicroseconds(self, value):
        pass

    @arduinoobjectmethod
    def readMicroseconds(self, value):
        pass

    @arduinoobjectmethod
    def attached(self):
        pass
