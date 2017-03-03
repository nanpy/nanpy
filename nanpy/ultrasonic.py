from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class Ultrasonic(ArduinoOject):

    def __init__(self, echo, trig, connecion=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', echo, trig)

    @returns(float)
    @arduinoobjectmethod
    def get_distance(self):
        pass

    @returns(float)
    @arduinoobjectmethod
    def reading_in_range(self, low, high):
        pass
        
