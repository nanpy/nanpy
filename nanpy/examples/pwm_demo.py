from nanpy.arduinotree import ArduinoTree
from nanpy.serialmanager import SerialManager

PIN = 5

# 0-255
VALUE = 128
DUTY_CYCLE = VALUE / 256.0

INPUT, OUTPUT = 0, 1


def pwm_demo():
    connection = SerialManager()
    a = ArduinoTree(connection=connection)
    p = a.pin.get(PIN)
    print ('PWM frequencies_available: %s' % p.pwm.frequencies_available)
    p.write_mode(OUTPUT)
    p.pwm.write_value(VALUE)

    # set frequency here
    p.pwm.frequency = 61

    print ('PWM frequency: %s' % p.pwm.frequency)
    print ('PWM duty cycle: %s %% ' % (DUTY_CYCLE * 100))


if __name__ == '__main__':
    pwm_demo()
