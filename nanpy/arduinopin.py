from nanpy.arduino import Arduino
from nanpy.arduinoboard import arduinoclassmethod
from nanpy.arduinoboard import returns
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

    @classmethod
    @memoized
    def count_analog(cls):
        return len(cls.analog_names())

    @classmethod
    @memoized
    def count_digital(cls):
        return len(cls.digital_names())

    @classmethod
    @memoized
    def count(cls):
        return cls.count_analog() + cls.count_digital()

    @classmethod
    @memoized
    def digital_names(cls):
        A0 = Define.asDict()['A0']
        return ['D%s' % x for x in range(0, A0)]

    @classmethod
    @memoized
    def analog_names(cls):
        A0 = Define.asDict()['A0']
        return (
            ['A%s' % (x - A0) for x in range(A0, ArduinoCore.totalPinCount())]
        )

    def __init__(self, name):
        self.A0 = Define.asDict()['A0']
        self.nr = name2int(name, self.A0)
        if self.nr >= ArduinoCore.totalPinCount():
            raise ValueError('pin %s (Nr:%s) not in range' %
                             (name, self.nr))

    @property
    @memoized
    def pwm(self):
        return ArduinoPwmPin(self.nr)

    @property
    def is_digital(self):
        return self.nr < self.A0

    @property
    def is_analog(self):
        return not self.is_digital

    @property
    def avr_port(self):
        x = ArduinoCore.digitalPinToPort(self.nr)
        return chr(ord('A') + x - 1)

    @property
    def avr_bit(self):
        bitmask = ArduinoCore.digitalPinToBitMask(self.nr)
        i = 0
        while bitmask != 1:
            bitmask >>= 1
            i += 1
        return i

    @property
    def avr_pin(self):
        return 'P%s%s' % (self.avr_port, self.avr_bit)

    @property
    def name(self):
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
        self.write_mode(INPUT)
        self.write_pullup(LOW)
        if self.pwm.available:
            self.pwm.reset()

    def write_pullup(self, value):
        self.write_mode(INPUT)
        return self.write_digital_value(value)

    def read_digital_value(self, direction=None):
        if direction is not None:
            self.write_mode(direction)
        return Arduino.digitalRead(self.nr)

    def write_digital_value(self, value, direction=None):
        if direction == INPUT:
            raise ValueError('write_digital_value() to INPUT??')
        if direction is not None:
            self.write_mode(direction)
        value = 1 if value else 0
        return Arduino.digitalWrite(self.nr, value)

    digital_value = property(read_digital_value, write_digital_value)

    def read_analog_value(self):
        if not self.is_analog:
            return None
        return Arduino.analogRead(self.nr)
    analog_value = property(read_analog_value)

    def read_mode(self):
        return Arduino.pinModeRead(self.nr)

    def write_mode(self, value):
        return Arduino.pinMode(self.nr, value)
    mode = property(read_mode, write_mode)

#     def read_pwm_value(self):
#         return
#
#     def write_pwm_value(self, value):
#         return Arduino.analogWrite(self.nr, value)
#     pwm_value = property(read_pwm_value, write_pwm_value)
