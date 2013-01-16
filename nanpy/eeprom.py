from nanpy.arduinoboard import (arduinoclassmethod, returns)

class EEPROM():

    @classmethod
    @arduinoclassmethod
    def write(cls, address, value):
        pass

    @classmethod
    @returns(int)
    @arduinoclassmethod
    def read(cls, address):
        pass
