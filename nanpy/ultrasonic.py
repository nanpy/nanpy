from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class Ultrasonic(ArduinoObject):
    cfg_h_name = 'USE_Ultrasonic'

    def __init__(self, echo, trig, useInches, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', echo, trig, useInches)

    @returns(float)
    @arduinoobjectmethod
    def get_distance(self):
        pass

    def reading_in_range(self, low, high):
        return low <= self.get_distance() <= high
        
