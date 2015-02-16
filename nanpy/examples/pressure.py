"""Pressure sensor demo.

Connect the BMP180 to the I2C bus.

"""
from __future__ import division

from nanpy.arduinotree import ArduinoTree
from nanpy.serialmanager import SerialManager

from nanpy.bmp180 import Bmp180


def main():
    connection = SerialManager(sleep_after_connect=2)
    connection.open()
    a = ArduinoTree(connection=connection)
    bmp = Bmp180(a.wire)
    p, t = bmp.read()
    print ('pressure: %s kPa' % (p / 1000))
    print ('temperature: %s C' % t)

if __name__ == '__main__':
    main()
