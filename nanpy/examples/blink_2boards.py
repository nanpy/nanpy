#!/usr/bin/env python

# Author: Andrea Stagi <stagi.andrea@gmail.com>
# Description: keeps your led blinking on 2 boards
# Dependencies: None

from nanpy import (ArduinoApi, SerialManager)
from time import sleep


device_1 = '/dev/tty.usbmodem1411'
device_2 = '/dev/tty.usbmodem1431'

connection_1 = SerialManager(device=device_1)
connection_2 = SerialManager(device=device_2)

a1 = ArduinoApi(connection=connection_1)
a1.pinMode(13, a1.OUTPUT)

a2 = ArduinoApi(connection=connection_2)
a2.pinMode(13, a2.OUTPUT)

for i in range(10000):
    a1.digitalWrite(13, (i + 1) % 2)
    sleep(1)
    a2.digitalWrite(13, (i + 1) % 2)
    sleep(1)

