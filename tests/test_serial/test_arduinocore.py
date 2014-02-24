import common
from nanpy.arduinotree import ArduinoTree
from nose.tools import eq_
from nose.tools import ok_


def setup():
    common.setup()


def test():
    a = ArduinoTree()
    eq_(a.core.digitalPinToBitMask(2), 4)
    eq_(a.core.digitalPinToPort(2), 4)
    eq_(a.core.digitalPinToTimer(2), 0)
    eq_(a.core.analogInPinToBit(2), 2)


def test_ports():
    a = ArduinoTree()
    eq_(a.core.portInputRegister(0), 0)   # NOT_A_PORT
    eq_(a.core.portInputRegister(1), 0)   # NOT_A_PORT
    eq_(a.core.portInputRegister(2), 35)  # PINB
    eq_(a.core.portInputRegister(3), 38)  # PINC
    eq_(a.core.portInputRegister(4), 41)  # PIND

    eq_(a.core.portModeRegister(0), 0)   # NOT_A_PORT
    eq_(a.core.portModeRegister(1), 0)   # NOT_A_PORT
    eq_(a.core.portModeRegister(2), 36)  # DDRB
    eq_(a.core.portModeRegister(3), 39)  # DDRC
    eq_(a.core.portModeRegister(4), 42)  # DDRD

    eq_(a.core.portOutputRegister(0), 0)   # NOT_A_PORT
    eq_(a.core.portOutputRegister(1), 0)   # NOT_A_PORT
    eq_(a.core.portOutputRegister(2), 37)  # PORTB
    eq_(a.core.portOutputRegister(3), 40)  # PORTC
    eq_(a.core.portOutputRegister(4), 43)  # PORTD
