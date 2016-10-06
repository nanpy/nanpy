"""soft reset demo.

https://github.com/nanpy/nanpy/issues/72

watchdog doesn't work with some bootloaders.
Soft_reset() is based on watchdog.

More information:
http://arduino.stackexchange.com/questions/2922/watchdog-timer-stuck-in-restart-loop-green-led-flashing
"The OP is using an Adriuni Pro Mini clone. 
The included bootloader on the Arduino Pro Mini 
does not support system restarts by the WDT. 
Essentially, on a device with a bootloader 
that does not support WDT restarts, 
the board will restart but the timer / reset will not causing 
the board to continuously reset on reboot. 
There are alternative bootloaders for arduino boards 
that may resolve this issue."

"""

from nanpy.arduinotree import ArduinoTree
from nanpy.serialmanager import SerialManager


def print_millis(a):
    print ('uptime: %s sec' % (a.api.millis() / 1000.0))


def reset_demo():
    connection = SerialManager()
    a = ArduinoTree(connection=connection)
    print_millis(a)
    print ('soft reset')
    a.soft_reset()
    print_millis(a)

if __name__ == '__main__':
    reset_demo()
