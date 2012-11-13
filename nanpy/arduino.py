from nanpy.arduinoboard import (arduinoclassmethod, returns)

import time

class Arduino():

    HIGH = 1
    LOW  = 0
    INPUT  = 0
    OUTPUT = 1

    @classmethod
    @arduinoclassmethod
    def digitalWrite(cls, pin, value):
        pass

    @classmethod
    @returns(int)
    @arduinoclassmethod
    def digitalRead(cls, pin):
        pass

    @classmethod
    @arduinoclassmethod
    def analogWrite(cls, pin, value):
        pass

    @classmethod
    @returns(int)
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
        time.sleep(value/1000)

