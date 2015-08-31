from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class TLC5947(ArduinoObject):

    def __init__(self, boardTotal, clock, data, latch, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', boardTotal, clock, data, latch)

    @arduinoobjectmethod
    def setLED(self, led, r, g, b):
        pass

    @arduinoobjectmethod
    def write(self):
        pass