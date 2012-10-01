from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import arduinoobjectmethod

class Lcd(ArduinoObject):

    def __init__(self, pins, begin):
        ArduinoObject.__init__(self)
        self.id = self.call('new', pins, begin)

    @arduinoobjectmethod
    def printString(self, value):
        pass

    @arduinoobjectmethod
    def setCursor(self, col, row):
        pass
