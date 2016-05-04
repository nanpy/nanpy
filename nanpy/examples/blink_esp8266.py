#!/usr/bin/env python

from nanpy import ArduinoApi
from time import sleep
from nanpy.sockconnection import SocketManager
# import logging
# logging.basicConfig(level=logging.DEBUG)

PIN=2

connection = SocketManager()
a = ArduinoApi(connection=connection)

a.pinMode(PIN, a.OUTPUT)

for i in range(10000):
    a.digitalWrite(PIN, (i + 1) % 2)
    sleep(0.2)

