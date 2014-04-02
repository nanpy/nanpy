from nanpy.ad9850 import AD9850
from nanpy.arduinotree import ArduinoTree
import time
from nanpy.serialmanager import SerialManager


def measure(a, n, f, root='a'):
    start = time.time()
    for x in range(n):
        cmd = root + '.' + f
        try:
            locals()[root] = a
            exec (cmd)
        except:
            print (cmd)
            raise
    dt = time.time() - start
    print (
        '%-35s %8.2f ms per call, %5.0f call per second' %
        (f, 1000.0 * dt / n, 1.0 / dt * n))


def checkspeed(n):
    connection = SerialManager()
    connection.open()
    a = ArduinoTree(connection=connection)

    print ('performance test for ArduinoTree()')
    print ('n=%s' % n)
    print('')

    measure(a, n, 'api.digitalRead(0)')
    measure(a, n, 'api.digitalWrite(0,0)')
    measure(a, n, 'api.analogRead(0)')
    measure(a, n, 'api.analogWrite(0,0)')
    measure(a, n, 'api.pinMode(0,0)')
    measure(a, n, 'api.millis()')
    measure(a, n, 'api.shiftOut(0, 1, 0, 15)')

    a.define.get('__TIME__')  # init cache
    measure(a, n, 'define.get("__TIME__")')

    a.register.get('DDRB')  # init cache
    measure(a, n, 'register.get("DDRB").read_value()')
    measure(a, n, 'register.get("DDRB").address')
    measure(a, n, 'register.get("DDRB").size')

    a.vcc.read()  # init cache
    measure(a, n, 'vcc.read()')

    measure(a, n, 'pin.get(0).read_digital_value()')
    measure(a, n, 'pin.get(0).read_mode()')

    a.eeprom.size  # init cache
    measure(a, n, 'eeprom.size')
    measure(a, n, 'eeprom.read(0)')

    print('')
    print ('performance test for AD9850()')
    print('')

    ad9850 = AD9850([0, 1, 2, 3])
    measure(ad9850, n, 'setup()', root='ad9850')
    measure(ad9850, n, 'write_frequency(400)', root='ad9850')


if __name__ == '__main__':
    checkspeed(n=100)
