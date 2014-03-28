from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import arduinoobjectmethod


class Lcd_I2C(ArduinoObject):

    def __init__(self, pins, begin, connection=None):
        '''
        :param pins: [lcd_Addr, enable, Rw, Rs, d4, d5, d6, d7, backlighPin, pol]
        :param begin: [cols, rows]
        '''
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', pins, begin)

    @arduinoobjectmethod
    def printString(self, value, col=None, row=None):
        pass

    @arduinoobjectmethod
    def setCursor(self, col, row):
        pass

    @arduinoobjectmethod
    def setBacklight(self, value):
        pass
