from config import config
from nanpy.arduinocore import ArduinoCore
from nanpy.watchdog import Watchdog
from nose.tools import eq_, ok_
from tests.util import ok_vcc


def setup():
    Watchdog.soft_reset()

def teardown():
    pass


def test():
    eq_(ArduinoCore.digitalPinToBitMask(2), 4)
    eq_(ArduinoCore.digitalPinToPort(2), 4)
    eq_(ArduinoCore.portModeRegister(2), 0)
    eq_(ArduinoCore.digitalPinToTimer(2), 0)
    eq_(ArduinoCore.analogInPinToBit(2), 2)

    eq_(ArduinoCore.portOutputRegister(2), 0)
    eq_(ArduinoCore.portInputRegister(2), 0)
    eq_(ArduinoCore.totalPinCount(), 20)
    ok_vcc(ArduinoCore.readVcc())
    eq_(ArduinoCore.model(), config['model'])
