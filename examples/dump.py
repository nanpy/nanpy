'''Dump all possible values from the AVR
'''

from dicts.sorteddict import SortedDict
from entrypoint2 import entrypoint
from nanpy.arduino import Arduino
from nanpy.arduinocore import ArduinoCore
from nanpy.arduinopin import ArduinoPin
from nanpy.define import Define
from nanpy.resgister import Register
from nanpy.serialmanager import serial_manager
import inspect

FORMAT = '%-20s = %20s'


def dump(obj, selected_names=None):
    if selected_names:
        ls = selected_names
    else:
        ls = dir(obj)
    for attr in ls:
        if not attr.startswith('__'):
            if not inspect.ismethod(getattr(obj, attr)):
                    print FORMAT % (attr, getattr(obj, attr))


def dump_dict(d):
    for defname in sorted(d.keys()):
        defvalue = d[defname]
        print FORMAT % (defname, defvalue)


@entrypoint
def usbdump():
    serial_manager.connect('/dev/ttyS0')

    print FORMAT % ('totalPinCount', ArduinoCore.totalPinCount())
    print FORMAT % ('readVcc', ArduinoCore.readVcc()), 'V'
    print FORMAT % ('millis', Arduino.millis() / 1000.0), 'sec'

    print
    print '================================'
    print 'pins:'
    print '================================'

    print FORMAT % ('digital_names', ArduinoPin.digital_names())
    print FORMAT % ('analog_names', ArduinoPin.analog_names())

    for nr in range(ArduinoCore.totalPinCount()):
        print '---------- nr=%s ---------------' % nr
        pin = ArduinoPin(nr)
        dump(
            pin,
            'name nr nr_analog is_digital is_analog avr_pin mode digital_value analog_value programming_function'.split())
        if pin.pwm.available:
            print '--- pwm ---'
            dump(pin.pwm, '''frequency frequencies_available base_divisor divisor divisors_available
                                timer_mode
                                timer_register_name_a
                                timer_register_name_b
                                wgm
            '''.split())

    print
    print '================================'
    print 'defines:'
    print '================================'
    dump_dict(Define.asDict())

    print
    print '================================'
    print 'registers:'
    print '================================'
    for x in Register.names():
        r = Register(x)
        if r.size == 2:
            v = '0x%04X' % (r.value)
        else:
            v = '  0x%02X' % (r.value)

        print '%-20s = %s @0x%2X (size:%s)' % (r.name, v, r.address, r.size)
