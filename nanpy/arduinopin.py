from nanpy.arduino import Arduino
from nanpy.arduinocore import ArduinoCore
from nanpy.define import Define
from nanpy.memo import memoized
from nanpy.pwm import ArduinoPwmPin
import sys

HIGH = Arduino.HIGH
LOW = Arduino.LOW
INPUT = Arduino.INPUT
OUTPUT = Arduino.OUTPUT

# from six
PY3 = sys.version_info[0] == 3
if PY3:
    string_types = str,
else:
    string_types = basestring,


def name2int(pin_name, A0):
    try:
        if isinstance(pin_name, string_types):
            if pin_name[0] == 'D':
                nr = int(pin_name[1:])
                if nr >= A0:
                    raise ValueError('invalid pin id:%r' % pin_name)
            elif pin_name[0] == 'A':
                nr = int(pin_name[1:]) + A0
            else:
                nr = int(pin_name)
        else:
            nr = int(pin_name)
    except IndexError:
        raise ValueError('invalid pin id:%r' % pin_name)
    return nr


class ArduinoPin(object):

    '''Object-oriented representation of an Arduino pin

    Examples:

        # they do the same
        ArduinoPin(0).value
        ArduinoPin('D0').value
        ArduinoPin('D0').read_value()
    '''
    @classmethod
    @memoized
    def count_analog(cls):
        """Count of analog pins."""
        return len(cls.analog_names())

    @classmethod
    @memoized
    def count_digital(cls):
        """Count of digital pins."""
        return len(cls.digital_names())

    @classmethod
    @memoized
    def count(cls):
        """Count of all pins."""
        return cls.count_analog() + cls.count_digital()

    @classmethod
    @memoized
    def digital_names(cls):
        """List of digital pin names."""
        A0 = Define.asDict()['A0']
        return ['D%s' % x for x in range(0, A0)]

    @classmethod
    @memoized
    def analog_names(cls):
        """List of analog pin names."""
        A0 = Define.asDict()['A0']
        return (
            ['A%s' % (x - A0) for x in range(A0, ArduinoCore.totalPinCount())]
        )

    def __init__(self, name):
        """name can be int or string."""
        self.A0 = Define.asDict()['A0']
        self.nr = name2int(name, self.A0)
        if self.nr >= ArduinoCore.totalPinCount():
            raise ValueError('pin %s (Nr:%s) not in range' %
                             (name, self.nr))

    @property
    @memoized
    def pwm(self):
        '''Object-oriented representation of the pin PWM functionality
        '''
        return ArduinoPwmPin(self.nr)

    @property
    def is_digital(self):
        return self.nr < self.A0

    @property
    def is_analog(self):
        return not self.is_digital

    @property
    def avr_port(self):
        '''AVR port name (example: "B")
        '''
        x = ArduinoCore.digitalPinToPort(self.nr)
        return chr(ord('A') + x - 1)

    @property
    def avr_bit(self):
        '''AVR bit name (example: "2")
        '''
        bitmask = ArduinoCore.digitalPinToBitMask(self.nr)
        i = 0
        while bitmask != 1:
            bitmask >>= 1
            i += 1
        return i

    @property
    def avr_pin(self):
        '''AVR pin name (example: "PB2")
        '''
        return 'P%s%s' % (self.avr_port, self.avr_bit)

    @property
    def name(self):
        """Arduino pin name.

        D -> digital
        A -> analog
        (examples: "D2", "A0")

        """
        if self.is_digital:
            return 'D%s' % self.nr
        else:
            return 'A%s' % self.nr_analog

    @property
    def nr_analog(self):
        x = self.nr - self.A0
        if x >= 0:
            return x

    @property
    def programming_function(self):
        """programming function (MISO, MOSI, SCK or SS)"""
        d = Define.asDict()
        if self.nr == d['MISO']:
            return 'MISO'
        if self.nr == d['MOSI']:
            return 'MOSI'
        if self.nr == d['SCK']:
            return 'SCK'
        if self.nr == d['SS']:
            return 'SS'

    def reset(self):
        '''reset to the pin default state: INPUT, no pullup
        '''
        self.write_mode(INPUT)
        self.write_pullup(LOW)
        if self.pwm.available:
            self.pwm.reset()

    def write_pullup(self, value):
        """set pullup  (0/1)"""
        self.write_mode(INPUT)
        return self.write_digital_value(value)

    def read_digital_value(self, direction=None):
        """read digital value  (0/1)

        direction can be set, if 'direction' parameter exists

        """
        if direction is not None:
            self.write_mode(direction)
        return Arduino.digitalRead(self.nr)

    def write_digital_value(self, value, direction=None):
        """write digital value  (0/1)

        direction can be set, if 'direction' parameter exists, and it is
        not INPUT

        """
        if direction == INPUT:
            raise ValueError('write_digital_value() to INPUT??')
        if direction is not None:
            self.write_mode(direction)
        value = 1 if value else 0
        return Arduino.digitalWrite(self.nr, value)

    digital_value = property(read_digital_value, write_digital_value)

    def read_analog_value(self):
        '''read analog value  (0-1023)
        '''
        if not self.is_analog:
            return None
        return Arduino.analogRead(self.nr)
    analog_value = property(read_analog_value)

    def read_mode(self):
        """read mode  (0/1)"""
        return Arduino.pinModeRead(self.nr)

    def write_mode(self, value):
        """write mode  (0/1)"""
        return Arduino.pinMode(self.nr, value)
    mode = property(read_mode, write_mode)
