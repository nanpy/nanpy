"""soft reset demo."""

from nanpy.watchdog import Watchdog
from nanpy.arduino import Arduino


def print_millis():
    print ('uptime: %s sec' % (Arduino.millis() / 1000.0))

print_millis()
print ('soft reset')
Watchdog.soft_reset()
print_millis()
