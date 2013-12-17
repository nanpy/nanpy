from nanpy.arduinoboard import (arduinoclassmethod, returns)
from nanpy.memo import memoized

class EEPROM(object):

    @classmethod
    @arduinoclassmethod
    def write(cls, address, value):
        pass

    @classmethod
    @returns(int)
    @arduinoclassmethod
    def read(cls, address):
        pass
    
    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def size(cls):
        pass
