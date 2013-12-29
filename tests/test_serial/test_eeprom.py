from nose.tools import eq_
from nose.tools import ok_
from nose.tools import eq_
from nose.tools import ok_
from tests.util import soft_reset
from tests.util import exc_
from nanpy.arduinotree import ArduinoTree


def setup():
    soft_reset()


def test():
    a = ArduinoTree()

    eq_(a.eeprom.size, 1024)
    eq_(a.eeprom.read(17), 255)
