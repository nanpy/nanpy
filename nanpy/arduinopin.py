from nanpy.memo import memoized
from nanpy.pwm import ArduinoPwmPin
import sys

LOW, HIGH = 0, 1
INPUT, OUTPUT = 0, 1

# from six
PY3 = sys.version_info[0] == 3
if PY3:
    string_types = str,
else:
    string_types = basestring,


class PinError(Exception):
    pass


def to_pin_number(pin_name, A0=None):
    try:
        if isinstance(pin_name, string_types):
            if pin_name[0] == 'D':
                nr = int(pin_name[1:])
                if A0 is not None:
                    if nr >= A0:
                        raise ValueError('invalid pin id:%r' % pin_name)
            elif pin_name[0] == 'A':
                if A0 is None:
                    raise ValueError('A0 is None, but analog pin was set! (%s)' % pin_name)
                nr = int(pin_name[1:]) + A0
            else:
                nr = int(pin_name)
        elif hasattr(pin_name, 'pin_number'):
            nr=pin_name.pin_number
        else:
            nr = int(pin_name)
    except IndexError:
        raise ValueError('invalid pin id:%r' % pin_name)
    return nr


class ArduinoPin(object):

    '''Object-oriented representation of an Arduino pin

    Examples:

        # they do the same
        a=ArduinoTree()
        a.pin.get(0).value
        a.pin.get('D0').value
        a.pin.get('D0').read_value()
    '''

    def __init__(self, name, total_pin_count, define, register, core, ram, api):
        """name can be int or string."""
        self.register = register
        self.core = core
        self.ram = ram
        self.api = api
        self.define = define
        self.A0 = define.get('A0')
        self.pin_number = to_pin_number(name, self.A0)
        if self.pin_number >= total_pin_count:
            raise ValueError('pin %s (Nr:%s) not in range' %
                             (name, self.pin_number))

    @property
    @memoized
    def pwm(self):
        '''Object-oriented representation of the pin PWM functionality
        '''
        return (
            ArduinoPwmPin(
                self.pin_number,
                self.define,
                self.register,
                self.core,
                self.api)
        )

    @property
    def is_digital(self):
        return self.pin_number < self.A0

    @property
    def is_analog(self):
        return not self.is_digital

    @property
    def avr_port(self):
        '''AVR port name (example: "B")
        '''
        x = self.core.digitalPinToPort(self.pin_number)
        return chr(ord('A') + x - 1)

    @property
    def avr_bit(self):
        '''AVR bit name (example: "2")
        '''
        bitmask = self.core.digitalPinToBitMask(self.pin_number)
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
            return 'D%s' % self.pin_number
        else:
            return 'A%s' % self.pin_number_analog

    @property
    def pin_number_analog(self):
        x = self.pin_number - self.A0
        if x >= 0:
            return x

    @property
    def programming_function(self):
        """programming function (MISO, MOSI, SCK or SS)"""
        if self.pin_number == self.define.get('MISO'):
            return 'MISO'
        if self.pin_number == self.define.get('MOSI'):
            return 'MOSI'
        if self.pin_number == self.define.get('SCK'):
            return 'SCK'
        if self.pin_number == self.define.get('SS'):
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
        return self.api.digitalRead(self.pin_number)

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
        return self.api.digitalWrite(self.pin_number, value)

    digital_value = property(read_digital_value, write_digital_value)

    def read_analog_value(self):
        '''read analog value  (0-1023)
        '''
        if not self.is_analog:
            return None
        return self.api.analogRead(self.pin_number)
    analog_value = property(read_analog_value)

    def read_mode(self):
        """read mode  (0/1)"""
        bitmask = self.core.digitalPinToBitMask(self.pin_number)
        port = self.core.digitalPinToPort(self.pin_number)
        reg_address = self.core.portModeRegister(port)
        reg_value = self.ram.read(reg_address)
        mode = OUTPUT if reg_value & bitmask else INPUT
        return mode

    def write_mode(self, value):
        """write mode  (0/1)"""
        return self.api.pinMode(self.pin_number, value)
    mode = property(read_mode, write_mode)


class PinFeature(object):

    def __init__(self, define, register, core, ram, api):
        self.A0 = define.get('A0')
        self.define = define
        self.register = register
        self.core = core
        self.ram = ram
        self.api = api

    @memoized
    def get(self, name):
        return (
            ArduinoPin(
                name,
                self.count,
                self.define,
                self.register,
                self.core,
                self.ram,
                self.api)
        )

    @property
    @memoized
    def count_analog(self):
        """Count of analog pins."""
        return len(self.names_analog)

    @property
    @memoized
    def count_digital(self):
        """Count of digital pins."""
        return len(self.names_digital)

    @property
    @memoized
    def count(self):
        """Count of all pins.
        """
        return self.define.get('NUM_DIGITAL_PINS')

    @property
    def names(self):
        """List of all pin names."""
        return self.names_digital + self.names_analog

    @property
    def names_digital(self):
        """List of digital pin names."""
        A0 = self.A0
        return ['D%s' % x for x in range(0, A0)]

    @property
    def names_analog(self):
        """List of analog pin names."""
        A0 = self.A0
        return (
            ['A%s' % (x - A0) for x in range(A0, self.count)]
        )
