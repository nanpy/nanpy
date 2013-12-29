from nanpy.arduinotree import ArduinoTree
from nose.tools import eq_, ok_
from tests.util import ok_an
import common


def setup():
    common.setup()


def test():
    a = ArduinoTree()
    pin13 = a.pin.get(13)
    ok_(a.api.millis() > 1)

    ok_an(a.api.analogRead(0))

    eq_(pin13.read_mode(), 0)
    a.api.pinMode(13, 1)
    eq_(pin13.read_mode(), 1)
    a.api.pinMode(13, 0)
    eq_(pin13.read_mode(), 0)
