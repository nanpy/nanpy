#!/usr/bin/env python

# Description:

from nanpy.arduinotree import ArduinoTree
from nanpy.i2c import I2C_Master
from nanpy.serialmanager import SerialManager
import logging
log = logging.getLogger(__name__)


def main():
    connection = SerialManager(sleep_after_connect=2)
    connection.open()
    print connection.device
    a = ArduinoTree(connection=connection)
    master = I2C_Master(a.wire)
    master.send(0x27, [0b00001000])


if __name__ == '__main__':
    main()
