from nanpy.arduino import Arduino
from nose.tools import eq_, ok_
from tests.util import ok_an, soft_reset


def setup():
    soft_reset()


def test():
    ok_(Arduino.millis()>1)
    
    ok_an(Arduino.analogRead(0))
    
    Arduino.pinMode(13,1)
    Arduino.pinMode(13,0)

