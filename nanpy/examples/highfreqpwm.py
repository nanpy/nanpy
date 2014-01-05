"""High frequency PWM mode demo."""

from nanpy.arduinotree import ArduinoTree
from nanpy.serialmanager import SerialManager

FREQ = 10007


def highfreqpwm():
    connection = SerialManager()
    a = ArduinoTree(connection=connection)
    pin9 = a.pin.get(9)
    pin9.mode = 1
    pin9.write_digital_value(1)
    pwm = pin9.pwm
    print ('set  frequency=%s Hz' % FREQ)
    pwm.set_high_freq_around(FREQ)
    print ('real frequency=%s Hz' % pwm.read_frequency())


if __name__ == '__main__':
    highfreqpwm()
