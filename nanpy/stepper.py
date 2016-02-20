from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import arduinoobjectmethod

class Stepper(ArduinoObject):

    def __init__(self, revsteps, pin1, pin2, speed=None, connection=None, pin3=None, pin4=None):
        ArduinoObject.__init__(self, connection=connection)
        if pin3 is not None and pin4 is not None:
            self.id = self.call('new', revsteps, pin1, pin2, pin3, pin4)
        else:
            self.id = self.call('new', revsteps, pin1, pin2)
        if speed:
            self.setSpeed(speed)

    @arduinoobjectmethod
    def setSpeed(self, value):
        pass

    @arduinoobjectmethod
    def step(self, value):
        pass
