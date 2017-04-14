from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class MCP41xxx(ArduinoObject):
    cfg_h_name = 'USE_MCP41xxx'

    def __init__(self, dac, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', dac)


    @arduinoobjectmethod
    def analogWrite(self, gate, value):
        pass

