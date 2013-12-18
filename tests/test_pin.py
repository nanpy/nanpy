from config import config
from nanpy.arduinopin import ArduinoPin
from nanpy.resgister import Register
from nanpy.watchdog import Watchdog
from nose.tools import eq_, ok_
from tests.util import ok_an
from util import exc_
import time

def setup():
    Watchdog.soft_reset()

def teardown():
    pass

INPUT, OUTPUT = 0, 1

def test_pin_nr():
    pin = ArduinoPin(8)

    eq_(pin.nr, 8)
    eq_(pin.nr_analog, None)

    pin = ArduinoPin(14)
    eq_(pin.nr, 14)
    eq_(pin.nr_analog, 0)

    pin = ArduinoPin('A1')
    eq_(pin.nr, 15)
    eq_(pin.nr_analog, 1)

    pin = ArduinoPin('D9')
    eq_(pin.nr, 9)
    eq_(pin.nr_analog, None)

    pin = ArduinoPin('A2')
    eq_(pin.nr, 16)
    eq_(pin.nr_analog, 2)


def test_is():
    eq_(ArduinoPin(8).is_digital, True)
    eq_(ArduinoPin(8).is_analog, False)
    eq_(ArduinoPin('A2').is_digital, False)
    eq_(ArduinoPin('A2').is_analog, True)


def test_name():
    eq_(ArduinoPin(8).name, 'D8')
    eq_(ArduinoPin('D8').name, 'D8')
    eq_(ArduinoPin(15).name, 'A1')
    eq_(ArduinoPin('A2').name, 'A2')


def test_dig():
    pin = ArduinoPin(8)
    pin.reset()

    pin.write_mode(OUTPUT)

    pin.write_digital_value(1)


    eq_(pin.read_digital_value(), 1)
    eq_(pin.digital_value, 1)

    pin.write_mode(INPUT)
    pin.write_mode(OUTPUT)

    pin.write_digital_value(0)
    eq_(pin.read_digital_value(), 0)
    eq_(pin.digital_value, 0)

    pin.write_mode(INPUT)
    pin.write_mode(OUTPUT)

    pin.write_mode(INPUT)
    pin.write_pullup(True)

    eq_(pin.read_digital_value(), 1)
    eq_(pin.digital_value, 1)




def test_an():
    pin = ArduinoPin('A0')
    pin.mode = INPUT
    ok_an(pin.read_analog_value())
    ok_an(pin.analog_value)

    pin.write_pullup(True)

    ok_an(pin.read_analog_value(), pullup=True)


def test_mode():
    pin = ArduinoPin(8)
    pin.reset()

    eq_(pin.mode, INPUT)
    eq_(pin.read_mode(), INPUT)
    eq_(Register('DDRB').value, 0)

    pin.write_mode(OUTPUT)
    eq_(pin.mode, OUTPUT)
    eq_(pin.read_mode(), OUTPUT)
    eq_(Register('DDRB').value, 1)

    Register('DDRB').value = 0
    eq_(pin.mode, INPUT)

    pin.mode = OUTPUT
    eq_(pin.mode, OUTPUT)

    pin.reset()
    eq_(pin.mode, INPUT)


def test_pullup():
    pin = ArduinoPin(8)
    pin.write_pullup(True)



def test_pin_range():
    eq_(ArduinoPin.count(), 20)
    eq_(ArduinoPin.count_analog(), 6)
    eq_(ArduinoPin.count_digital(), 14)

#     eq_(ArduinoPin.range_all, range(0, 20))
#     eq_(ArduinoPin.range_analog, range(14, 20))
#     eq_(ArduinoPin.range_digital, range(0, 14))

    ArduinoPin('A5')
    exc_(ValueError, lambda: ArduinoPin('A6'))
    exc_(ValueError, lambda: ArduinoPin('D14'))
