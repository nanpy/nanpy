from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class ColorSensor(ArduinoObject):
    cfg_h_name = 'USE_ColorSensor'

    def __init__(self, s0, s1, s2, s3, sensorInput, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', s0, s1, s2, s3, sensorInput)

    @returns(int)
    @arduinoobjectmethod
    def get_color(self, color):
        pass
