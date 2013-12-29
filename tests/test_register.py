from config import config
from nanpy.arduino import Arduino
from nanpy.arduinocore import ArduinoCore
from nanpy.resgister import Register
from nanpy.watchdog import Watchdog
from nose.tools import eq_, ok_, eq_, ok_
from util import exc_
import time



def setup():
    Watchdog.soft_reset()

def teardown():
    pass


def test_registers():
    print (Register.names())
    ok_(len(Register.names()) > 77)

    eq_(Register('DDRB').read_value(), 0)
    eq_(Register('DDRB').value, 0)
    exc_(ValueError, lambda x: Register('xxx').value, 0)

    Register('DDRB').write_value(5)
    eq_(Register('DDRB').value, 5)
    Register('DDRB').value = 3
    eq_(Register('DDRB').value, 3)
    Register('DDRB').write_value(0)

    eq_(Register('DDRB').address, 0x24)
    eq_(Register('DDRB').name, 'DDRB')
    eq_(Register('DDRB').size, 1)
    
    
    # 9 bit
    eq_(Register('EEAR').size, 2)
    Register('EEAR').value = 511
    eq_(Register('EEAR').value, 511)



