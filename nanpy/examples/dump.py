"""Dump all possible values from the AVR."""

from nanpy.arduinotree import ArduinoTree
from nanpy.serialmanager import SerialManager
from pprint import pprint
import inspect
from nanpy.serialmanager import SerialManager

FORMAT = '%-20s = %20s'


def dump(obj, selected_names=None):
    if selected_names:
        ls = selected_names
    else:
        ls = dir(obj)
    for attr in ls:
        if not attr.startswith('__'):
            if not inspect.ismethod(getattr(obj, attr)):
                    print(FORMAT % (attr, getattr(obj, attr)))


def dump_dict(d):
    for defname in sorted(d.keys()):
        defvalue = d[defname]
        print(FORMAT % (defname, defvalue))


def dumpall():
    connection = SerialManager()
    a = ArduinoTree(connection=connection)

    print((FORMAT + ' V') % ('read_vcc', a.vcc.read()))
    print((FORMAT + ' sec') % ('millis', a.api.millis() / 1000.0))

    print('')
    print('================================')
    print('firmware classes:')
    print('================================')
    print('status:')
    pprint(a.connection.classinfo.firmware_class_status)
    print('unknown ids:')
    pprint(a.connection.classinfo.unknown_firmware_ids)

    print('')
    print('================================')
    print('pins:')
    print('================================')

    print(FORMAT % ('total_pin_count', a.pin.count))
    print(FORMAT % ('digital_names', a.pin.names_digital))
    print(FORMAT % ('analog_names', a.pin.names_analog))

    for pin_number in range(a.pin.count):
        print('---------- pin_number=%s ---------------' % pin_number)
        pin = a.pin.get(pin_number)
        dump(
            pin,
            'name pin_number pin_number_analog is_digital is_analog avr_pin mode digital_value analog_value programming_function'.split())
        if pin.pwm.available:
            print('--- pwm ---')
            dump(pin.pwm, '''frequency frequencies_available base_divisor divisor divisors_available
                                timer_mode
                                timer_register_name_a
                                timer_register_name_b
                                wgm
            '''.split())

    print('')
    print('================================')
    print('defines:')
    print('================================')
    dump_dict(a.define.as_dict)

    print('')
    print('================================')
    print('registers:')
    print('================================')
    for x in a.register.names:
        r = a.register.get(x)
        if r.size == 2:
            v = '0x%04X' % (r.value)
        else:
            v = '  0x%02X' % (r.value)

        print('%-20s = %s @0x%2X (size:%s)' % (r.name, v, r.address, r.size))


if __name__ == '__main__':
    dumpall()
