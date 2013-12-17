from config import config
from nanpy.arduino import Arduino
from nanpy.watchdog import Watchdog
from nose.tools import eq_, ok_
from tests.util import ok_an


def setup():
    Watchdog.soft_reset()

def teardown():
    pass

def test():
    ok_(Arduino.millis()>1)
    
    ok_an(Arduino.analogRead(0))
    
    
    eq_(Arduino.pinModeRead(13), 0)
    Arduino.pinMode(13,1)
    eq_(Arduino.pinModeRead(13), 1)
    Arduino.pinMode(13,0)
    eq_(Arduino.pinModeRead(13), 0)

