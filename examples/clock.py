#!/usr/bin/env python

# Author: Andrea Stagi <stagi.andrea@gmail.com>
# Description: get the current time from a ntp server and show it on a lcd
# Dependencies: ntplib (http://pypi.python.org/pypi/ntplib/)

import ntplib
from nanpy import Arduino
from nanpy import Lcd
from time import ctime
from datetime import datetime

ntp_client = ntplib.NTPClient()
response = ntp_client.request('europe.pool.ntp.org', version=3)

time = response.tx_time

lcd = Lcd([7, 8, 9, 10, 11, 12], [16, 2])

while (1):
    lcd.setCursor(0, 0)
    lcd.printString((datetime.fromtimestamp(time)).strftime('%Y-%m-%d'))
    lcd.setCursor(0, 1)
    lcd.printString((datetime.fromtimestamp(time)).strftime('%H:%M'))
    Arduino.delay(1000)
    time += 1
