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
    eq_(a.core.portModeRegister(2), 0)
    eq_(a.core.digitalPinToTimer(2), 0)
    eq_(a.core.analogInPinToBit(2), 2)

    eq_(a.core.portOutputRegister(2), 0)
    eq_(a.core.portInputRegister(2), 0)
