#!/usr/bin/env python

# Author: Andrea Stagi <stagi.andrea@gmail.com>
# Description: get the current time from a ntp server and show it on a lcd
# Dependencies: ntplib (http://pypi.python.org/pypi/ntplib/)

import ntplib
from nanpy import (SerialManager, Lcd)
from datetime import datetime
from time import sleep

connection = SerialManager()

ntp_client = ntplib.NTPClient()
response = ntp_client.request('europe.pool.ntp.org', version=3)

time = int(response.tx_time)

pins = [7, 8, 9, 10, 11, 12]
cols, rows = 16, 2
lcd = Lcd(pins, [cols, rows], connection=connection)

while (1):
    lcd.setCursor(0, 0)
    lcd.printString((datetime.fromtimestamp(time)).strftime('%Y-%m-%d'))
    if time % 2:
        time_format = '%H:%M'
    else:
        time_format = '%H %M'
    lcd.setCursor(0, 1) 
    lcd.printString((datetime.fromtimestamp(time)).strftime(time_format))
    sleep(1)
    time += 1
