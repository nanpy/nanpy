"""This demo sets a PWM frequency on pin 5, then measures it using a counter.

For measuring external frequency the PWM should be disabled.

"""

from nanpy.arduinotree import ArduinoTree
from nanpy.serialmanager import SerialManager
import time


EXTERNAL_FREQUENCY = False
GATE_TIME = 0.7  # sec

INPUT, OUTPUT = 0, 1


def counterdemo():
    connection = SerialManager()
    a = ArduinoTree(connection=connection)
    p = a.pin.get(5)

    if not EXTERNAL_FREQUENCY:
        p.write_mode(OUTPUT)
        p.pwm.write_value(128)
        p.pwm.frequency = p.pwm.frequencies_available[-2]
        print ('PWM frequencies_available: %s' % p.pwm.frequencies_available)
        print ('frequency set: %s' % p.pwm.frequency)

    t1 = time.time()
    fread = a.counter.read_frequency(GATE_TIME)
    t2 = time.time()

    print ('frequency read: %s' % fread)
    print ('gate time: %s sec' % (GATE_TIME))
    print ('time elapsed: %s sec' % (t2 - t1))

if __name__ == '__main__':
    counterdemo()
