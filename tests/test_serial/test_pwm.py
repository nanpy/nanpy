from config import config
from nose.tools import eq_
from nanpy.arduinotree import ArduinoTree
import common


def setup():
    common.setup()


INPUT, OUTPUT = 0, 1
F_CPU = config.get('F_CPU')


def test_pwm():
    a = ArduinoTree()
    pin8 = a.pin.get(8)
    pin9 = a.pin.get(9)

    TCCR1B = a.register.get('TCCR1B')

    eq_(pin8.pwm.available, False)
    eq_(pin9.pwm.available, True)
    eq_(pin9.pwm.timer_register_name_b, 'TCCR1B')
    eq_(pin9.pwm.base_divisor, 512)
    eq_(pin9.pwm.divisors_available, [1, 8, 64, 256, 1024])

    frequencies = sorted([F_CPU / 2 ** 9,
                          F_CPU / 2 ** 12,
                          F_CPU / 2 ** 15,
                          F_CPU / 2 ** 17,
                          F_CPU / 2 ** 19,
                          ])
    eq_(pin9.pwm.frequencies_available, frequencies)

    TCCR1B.value = 3
    eq_(TCCR1B.value, 3)

    eq_(pin9.pwm.read_divisor(), 2 ** 6)
    eq_(pin9.pwm.divisor, 2 ** 6)
    eq_(pin9.pwm.read_frequency(), F_CPU / 2 ** 15)
    eq_(pin9.pwm.frequency, F_CPU / 2 ** 15)

    pin9.pwm.write_frequency(int(F_CPU / 2 ** 19))
    eq_(pin9.pwm.read_frequency(), F_CPU / 2 ** 19)
    eq_(TCCR1B.value, 5)

    TCCR1B.value = 2
    eq_(pin9.pwm.read_divisor(), 2 ** 3)
    eq_(pin9.pwm.divisor, 2 ** 3)
    eq_(pin9.pwm.read_frequency(), F_CPU / 2 ** 12)
    eq_(pin9.pwm.frequency, F_CPU / 2 ** 12)
    eq_(TCCR1B.value, 2)

    pin9.pwm.divisor = 2 ** 10
    eq_(pin9.pwm.read_divisor(), 2 ** 10)
    eq_(pin9.pwm.divisor, 2 ** 10)
    eq_(pin9.pwm.read_frequency(), F_CPU / 2 ** 19)
    eq_(pin9.pwm.frequency, F_CPU / 2 ** 19)
    eq_(TCCR1B.value, 5)

    pin9.pwm.write_frequency(F_CPU / 2 ** 9)
    eq_(pin9.pwm.read_frequency(), F_CPU / 2 ** 9)
    eq_(TCCR1B.value, 1)

    pin9.pwm.frequency = F_CPU / 2 ** 17
    eq_(pin9.pwm.read_frequency(), F_CPU / 2 ** 17)
    eq_(TCCR1B.value, 4)

    TCCR1B.value = 3
    eq_(TCCR1B.value, 3)

    pin9.pwm.write_value(45)
