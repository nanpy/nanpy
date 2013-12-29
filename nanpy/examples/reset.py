"""soft reset demo."""

from nanpy.arduinotree import ArduinoTree


def print_millis(a):
    print ('uptime: %s sec' % (a.api.millis() / 1000.0))


def reset_demo():
    a = ArduinoTree()
    print_millis(a)
    print ('soft reset')
    a.soft_reset()
    print_millis(a)

if __name__ == '__main__':
    reset_demo()
