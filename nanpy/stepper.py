from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import arduinoobjectmethod

class Stepper(ArduinoObject):

    def __init__(self, revsteps, pin1, pin2):
        ArduinoObject.__init__(self)
        self.id = self.call('new', revsteps, pin1, pin2)

    @arduinoobjectmethod
    def setSpeed(self, value):
        pass

    @arduinoobjectmethod
    def step(self, value):
        pass
