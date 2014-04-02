from nanpy.fwinfo import libc_version, arduino_version, avr_name, libc_date, \
    compile_datetime, firmware_info
from nose.tools import eq_
import datetime


def test():
    eq_(libc_version(10604), '1.6.4')
    eq_(libc_version('10604'), '1.6.4')
    eq_(libc_version(11111), '1.11.11')

    eq_(libc_date(20081106), datetime.date(2008, 11, 6))
    eq_(libc_date('20081106'), datetime.date(2008, 11, 6))

    eq_(arduino_version(105), '1.0.5')
    eq_(arduino_version('105'), '1.0.5')

    eq_(avr_name('__AVR_ATmega328P__'), 'ATmega328P')

    eq_(compile_datetime('Mar 28 2008', '17:40:12'),
        datetime.datetime(2008, 3, 28, 17, 40, 12))

    eq_(firmware_info(dict(
                      MCU='__AVR_ATmega328P__',
                      ARDUINO='105',
                      __DATE__='Mar 28 2014',
                      __TIME__='17:40:12',
                      __VERSION__='4.3.2',
                      __AVR_LIBC_DATE_='20081106',
                      __AVR_LIBC_VERSION__='10604',

                      )),
        {'gcc_version': '4.3.2',
         'libc_version': '1.6.4',
                         'libc_date': datetime.date(2008, 11, 6),
                         'arduino_version': '1.0.5',
                         'avr_name': 'ATmega328P',
                         'compile_datetime':
         datetime.datetime(2014, 3, 28, 17, 40, 12),
         }
        )
