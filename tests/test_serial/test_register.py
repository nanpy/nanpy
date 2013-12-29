from nose.tools import eq_, ok_, eq_, ok_
from tests.util import exc_
from nanpy.arduinotree import ArduinoTree
import common


def setup():
    common.setup()


def test_registers():
    a = ArduinoTree()
    print (a.register.names)
    ok_(len(a.register.names) > 77)

    eq_(a.register.get('DDRB').read_value(), 0)
    eq_(a.register.get('DDRB').value, 0)
    exc_(ValueError, lambda x: a.register.get('xxx').value, 0)

    a.register.get('DDRB').write_value(5)
    eq_(a.register.get('DDRB').value, 5)
    a.register.get('DDRB').value = 3
    eq_(a.register.get('DDRB').value, 3)
    a.register.get('DDRB').write_value(0)

    eq_(a.register.get('DDRB').address, 0x24)
    eq_(a.register.get('DDRB').name, 'DDRB')
    eq_(a.register.get('DDRB').size, 1)

    # 9 bit
    eq_(a.register.get('EEAR').size, 2)
    a.register.get('EEAR').value = 511
    eq_(a.register.get('EEAR').value, 511)


def test_register_proxy():
    a = ArduinoTree()
    r = a.register.proxy

    eq_(r.DDRB, 0)

    r.DDRB = 5
    eq_(r.DDRB, 5)
    r.DDRB = 3
    eq_(r.DDRB, 3)
    eq_(a.register.get('DDRB').value, 3)

    r.DDRB = 0

    # 9 bit
    r.EEAR = 511
    eq_(r.EEAR, 511)
