from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import arduinoclassmethod

class Lcd(ArduinoObject):

    def __init__(self, pins, begin):
        ArduinoObject.__init__(self)
        self.id = self.call('new', pins, begin)

    @arduinoclassmethod
    def printString(self, value):
        pass

    @arduinoclassmethod
    def setCursor(self, col, row):
        pass
