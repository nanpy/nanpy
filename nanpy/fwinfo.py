import datetime


def avr_name(MCU):
    """The name of the AVR.

    Example: __AVR_ATmega328P__ -> ATmega328P

    """
    return MCU.strip('_').split('_')[-1]


def arduino_version(ARDUINO):
    """
    Example: 105  -> 1.0.5
    10608 -> 1.6.8
    """
    s = str(ARDUINO)
    if len(s) == 5:
        return '%s.%s.%s' % (s[0], int(s[1:3]), int(s[3:5]))
    else:
        return '.'.join(s)


def parse_month(s):
    '''gcc month
    Jan -> 1
    ...
    '''
    if s == 'Jan':
        return 1
    if s == 'Feb':
        return 2
    if s == 'Mar':
        return 3
    if s == 'Apr':
        return 4
    if s == 'May':
        return 5
    if s == 'Jun':
        return 6
    if s == 'Jul':
        return 7
    if s == 'Aug':
        return 8
    if s == 'Sep':
        return 9
    if s == 'Oct':
        return 10
    if s == 'Nov':
        return 11
    if s == 'Dec':
        return 12
    raise ValueError('invalid month: %s' % s)


def compile_datetime(DATE, TIME):
    '''
    Example: Mar 28 2014, 17:40:12
    -> datetime.datetime(2008, 3, 28, 17, 40, 12)
    '''
    dls = DATE.strip().split()
    d = datetime.date(int(dls[2]), parse_month(dls[0]), int(dls[1]))
    t = datetime.datetime.strptime(TIME, '%H:%M:%S')
    dt = datetime.datetime.combine(d, t.time())
#     dt = datetime.datetime.strptime(
#         DATE + ' ' + TIME,
#         '%b %d %Y %H:%M:%S')
    return dt


def libc_version(AVR_LIBC_VERSION):
    """
    Example: 10604  -> 1.6.4

    """
    s = str(AVR_LIBC_VERSION)
    ls = [s[0], s[1:3], s[3:5]]
    ls = map(int, ls)
    ls = map(str, ls)
    return '.'.join(ls)


def libc_date(AVR_LIBC_DATE):
    """
    Example: 20081106  -> 2008.11.06

    """
    s = str(AVR_LIBC_DATE)
    ls = [s[0:4], s[4:6], s[6:8]]
    ls = map(int, ls)
    d = datetime.date(*ls)
    return d


def firmware_info(define_dict):
    d = dict()
    d['avr_name'] = avr_name(define_dict['MCU'])
    d['arduino_version'] = arduino_version(define_dict['ARDUINO'])
    d['compile_datetime'] = compile_datetime(define_dict['__DATE__'],
                                             define_dict['__TIME__'],
                                             )
    d['gcc_version'] = define_dict['__VERSION__']
    d['libc_version'] = libc_version(define_dict['__AVR_LIBC_VERSION__'])
    d['libc_date'] = libc_date(define_dict['__AVR_LIBC_DATE_'])

    return d
