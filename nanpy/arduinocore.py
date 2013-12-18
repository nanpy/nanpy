from nanpy.arduinoboard import arduinoclassmethod, returns
from nanpy.define import Define
from nanpy.memo import memoized


class ArduinoCore(object):

    """Access to Arduino functions which are not part of the public API.

    There are some additional funtions implemented in C

    """

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def digitalPinToBitMask(cls, pin):
        """nonpublic Arduino function."""

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def digitalPinToPort(cls, pin):
        """nonpublic Arduino function."""

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def portModeRegister(cls, pin):
        """nonpublic Arduino function."""

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def digitalPinToTimer(cls, pin):
        """nonpublic Arduino function."""

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def analogInPinToBit(cls, pin):
        """nonpublic Arduino function."""

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def portOutputRegister(cls, pin):
        """nonpublic Arduino function."""

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def portInputRegister(cls, pin):
        """nonpublic Arduino function."""

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def totalPinCount(cls):
        """total pin count.

        The C implementation is a hack.

        """

    @classmethod
    @returns(lambda x: int(x) / 1000.0)
    @arduinoclassmethod
    def readVcc(cls):
        """VCC in Volt. This works on Arduinos with a 328 or 168 only.

        Source: http://code.google.com/p/tinkerit/wiki/SecretVoltmeter

        How it works

        The Arduino 328 and 168 have a built in precision voltage reference of 1.1V.
        This is used sometimes for precision measurement,
        although for Arduino it usually makes more sense to measure against Vcc,
        the positive power rail.
        The chip has an internal switch that selects which pin the analogue to digital converter reads.
        That switch has a few leftover connections, so the chip designers wired them up to useful signals.
        One of those signals is that 1.1V reference.
        So if you measure how large the known 1.1V reference is in comparison to Vcc,
        you can back-calculate what Vcc is with a little algebra. That is how this works.

        """

    @classmethod
    def model(cls):
        """The model of the AVR.

        Example: ATmega328P

        """
        s = Define.asDict().get('MCU')
        return s.strip('_').split('_')[-1]
