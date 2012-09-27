from nanpy.arduinoboard import ArduinoObject

class Lcd(ArduinoObject):

    def __init__(self, pins, begin):
        ArduinoObject.__init__(self, "Lcd")
        self.id = self.call('new', pins, begin)

    def printString(self, value):
        return self.call('print', value)

    def setCursor(self, col, row):
        return self.call('setCursor', col, row)
