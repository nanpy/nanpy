from nanpy.arduinotree import ArduinoTree
from nanpy.watchdog import Watchdog
import common


def setup():
    common.setup()


def test():
    a = ArduinoTree(connection=None)
    a.watchdog.reset()
    a.watchdog.enable(a.watchdog.WDTO_1S)
    a.watchdog.disable()


def test2():
    watchdog = Watchdog(connection=None)
    watchdog.reset()
    watchdog.enable(watchdog.WDTO_1S)
    watchdog.disable()
