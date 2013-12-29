from __future__ import with_statement
from nanpy.arduinotree import ArduinoTree
from nanpy.counter import Counter
from nose.tools import ok_, eq_
from config import config
import common

OUTPUT = 1


def setup():
    common.setup()


def test_counter():
    a = ArduinoTree()
    p = a.pin.get(5)
    p.write_mode(OUTPUT)
    p.pwm.write_value(128)

    counter1 = a.counter
    counter2 = Counter(F_CPU=config['F_CPU'])

    print ('frequencies_available: %s' % p.pwm.frequencies_available)
    for fset in p.pwm.frequencies_available:
        p.pwm.frequency = fset
        print('---------------------------')
        print('fset=%s' % fset)
        print('---------------------------')
        for ms in [10, 20, 50, 100, 200, 500, 1000]:
            print ('gate=%s ms' % ms)
            t = ms / 1000.0
            error = a.counter.error(t)
            print ('error=%s' % error)

            f1 = counter1.read_frequency(t)
            f2 = counter2.read_frequency(t)
            print (f1, f2)
            diff1 = abs(f1 - fset)
            diff2 = abs(f2 - fset)
            ok_(diff1 <= (1.1 * error))
            ok_(diff2 <= (1.1 * error))
