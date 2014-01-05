from nanpy.arduinotree import ArduinoTree
import time
from nanpy.serialmanager import SerialManager


GATE_TIME = 0.7  # sec
F = 9765  # Hz


def counterdemo():
    connection = SerialManager()
    a = ArduinoTree(connection=connection)
    p = a.pin.get(5)
    a.soft_reset()
    print ('PWM frequencies_available: %s' % p.pwm.frequencies_available)
    p.write_mode(1)
    p.pwm.write_value(128)
    p.pwm.frequency = F
    print ('frequency set: %s' % p.pwm.frequency)
    t1 = time.time()
    fread = a.counter.read_frequency(GATE_TIME)
    t2 = time.time()
    print ('frequency read: %s' % fread)
    print ('gate time: %s sec' % (GATE_TIME))
    print ('time elapsed: %s sec' % (t2 - t1))

if __name__ == '__main__':
    counterdemo()
