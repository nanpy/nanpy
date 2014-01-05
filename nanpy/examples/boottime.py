from nanpy.arduinotree import ArduinoTree
from nanpy.serialmanager import SerialManager
import time


def boot_time():
    connection = SerialManager()
    a = ArduinoTree(connection=connection)
    a.watchdog.enable(a.watchdog.WDTO_500MS)
    time.sleep(1)
    a.connection.flush_input()
    x = a.api.millis()
    return 1000 - 500 - x


if __name__ == '__main__':
    print ('boot_time %s ms' % boot_time())
