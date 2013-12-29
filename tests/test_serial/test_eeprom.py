from nanpy.arduinotree import ArduinoTree
from nose.tools import eq_
import common


def setup():
    common.setup()


def test():
    a = ArduinoTree()

    eq_(a.eeprom.size, 1024)
    eq_(a.eeprom.read(17), 255)
