from nanpy.arduinoboard import arduinoclassmethod, returns
from nanpy.define import Define
from nanpy.memo import memoized


class ArduinoCore(object):

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def digitalPinToBitMask(cls, pin):
        pass

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def digitalPinToPort(cls, pin):
        pass

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def portModeRegister(cls, pin):
        pass

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def digitalPinToTimer(cls, pin):
        pass

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def analogInPinToBit(cls, pin):
        pass

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def portOutputRegister(cls, pin):
        pass

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def portInputRegister(cls, pin):
        pass

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def totalPinCount(cls):
        pass

    @classmethod
    @returns(lambda x: int(x) / 1000.0)
    @arduinoclassmethod
    def readVcc(cls):
        """VCC in Volt."""

    @classmethod
    def model(cls):
        """"""
        s = Define.asDict().get('MCU')
        return s.strip('_').split('_')[-1]
