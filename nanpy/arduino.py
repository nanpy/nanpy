from nanpy.arduinoboard import (call_static_method, return_value)
from nanpy.arduinoboard import arduinoclassmethod

class Arduino():

    @classmethod
    @arduinoclassmethod
    def digitalWrite(cls, pin, value):
        pass

    @classmethod
    @arduinoclassmethod
    def digitalRead(cls, pin):
        pass

    @classmethod
    @arduinoclassmethod
    def analogWrite(cls, pin, value):
        pass

    @classmethod
    @arduinoclassmethod
    def analogRead(cls, pin):
        pass

    @classmethod
    @arduinoclassmethod
    def pinMode(cls, pin, mode):
        pass

    @classmethod
    @arduinoclassmethod
    def delay(cls, value):
        pass

