from nose.tools import eq_
from nose.tools import ok_
from tests.util import ok_an,  exc_
from nanpy.arduinotree import ArduinoTree
import common


def setup():
    common.setup()


INPUT, OUTPUT = 0, 1


def test_pin_nr():
    a = ArduinoTree()
    pin = a.pin.get(8)

    eq_(pin.pin_number, 8)
    eq_(pin.pin_number_analog, None)

    pin = a.pin.get(14)
    eq_(pin.pin_number, 14)
    eq_(pin.pin_number_analog, 0)

    pin = a.pin.get('A1')
    eq_(pin.pin_number, 15)
    eq_(pin.pin_number_analog, 1)

    pin = a.pin.get('D9')
    eq_(pin.pin_number, 9)
    eq_(pin.pin_number_analog, None)

    pin = a.pin.get('A2')
    eq_(pin.pin_number, 16)
    eq_(pin.pin_number_analog, 2)


def test_is():
    a = ArduinoTree()
    eq_(a.pin.get(8).is_digital, True)
    eq_(a.pin.get(8).is_analog, False)
    eq_(a.pin.get('A2').is_digital, False)
    eq_(a.pin.get('A2').is_analog, True)


def test_name():
    a = ArduinoTree()
    eq_(a.pin.get(8).name, 'D8')
    eq_(a.pin.get('D8').name, 'D8')
    eq_(a.pin.get(15).name, 'A1')
    eq_(a.pin.get('A2').name, 'A2')


def test_dig():
    a = ArduinoTree()
    pin = a.pin.get(8)
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
    a = ArduinoTree()
    pin = a.pin.get('A0')
    pin.mode = INPUT
    ok_an(pin.read_analog_value())
    ok_an(pin.analog_value)

    pin.write_pullup(True)

    ok_an(pin.read_analog_value(), pullup=True)


def test_mode():
    a = ArduinoTree()
    DDRB = a.register.get('DDRB')
    pin = a.pin.get(8)
    pin.reset()

    eq_(pin.mode, INPUT)
    eq_(pin.read_mode(), INPUT)
    eq_(DDRB.value, 0)

    pin.write_mode(OUTPUT)
    eq_(pin.mode, OUTPUT)
    eq_(pin.read_mode(), OUTPUT)
    eq_(DDRB.value, 1)

    DDRB.value = 0
    eq_(pin.mode, INPUT)

    pin.mode = OUTPUT
    eq_(pin.mode, OUTPUT)

    pin.reset()
    eq_(pin.mode, INPUT)


def test_pullup():
    a = ArduinoTree()
    pin = a.pin.get(8)
    pin.write_pullup(True)


def test_pin_range():
    a = ArduinoTree()
    eq_(a.pin.count, 20)
    eq_(a.pin.count_analog, 6)
    eq_(a.pin.count_digital, 14)

#     eq_(a.pin.get.range_all, range(0, 20))
#     eq_(a.pin.get.range_analog, range(14, 20))
#     eq_(a.pin.get.range_digital, range(0, 14))

    a.pin.get('A5')
    exc_(ValueError, lambda: a.pin.get('A6'))
    exc_(ValueError, lambda: a.pin.get('D14'))
