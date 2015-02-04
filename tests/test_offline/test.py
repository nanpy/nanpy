from nanpy.arduinopin import to_pin_number
from nanpy.counter import Counter
from nose.tools import eq_
from tests.util import exc_


def test_to_pin_number():
    eq_(to_pin_number(0), 0)
    eq_(to_pin_number(1, A0=None), 1)
    eq_(to_pin_number(20, A0=5), 20)

    eq_(to_pin_number('D0', A0=None), 0)
    eq_(to_pin_number('D7', A0=8), 7)
    exc_(ValueError, lambda: to_pin_number('D7', A0=7))
    eq_(to_pin_number('D20', A0=21), 20)

    eq_(to_pin_number('A0', A0=0), 0)
    eq_(to_pin_number('A0', A0=7), 7)
    eq_(to_pin_number('A15', A0=5), 20)
    exc_(ValueError, lambda: to_pin_number('A7', A0=None))

    class Dummy(object):
        pass
    obj = Dummy()
    obj.pin_number = 23
    eq_(to_pin_number(obj, A0=0), 23)


def test_calculate_multiplier():
    Mhz = 1e6

    eq_(Counter.calculate_multiplier(16 * Mhz), 1)
    eq_(Counter.calculate_multiplier(8 * Mhz), 1)
    eq_(Counter.calculate_multiplier(4 * Mhz), 1)
    eq_(Counter.calculate_multiplier(2 * Mhz), 1)
    eq_(Counter.calculate_multiplier(1 * Mhz), 1)

    eq_(Counter.calculate_multiplier(20 * Mhz), 20 / 16.0)
    eq_(Counter.calculate_multiplier(10 * Mhz), 10 / 8.0)
