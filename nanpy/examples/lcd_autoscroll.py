#!/usr/bin/env python

import time

from nanpy import SerialManager
from nanpy.lcd import Lcd


if __name__ == '__main__':

    connection = SerialManager(sleep_after_connect=2)

    cols, rows = 16, 2

    pins = [7, 8, 9, 10, 11, 12]
    lcd = Lcd(pins, [cols, rows], connection=connection)

    while True:

        lcd.setCursor(0, 0);

        for char in range(10):
            lcd.printString(char)
            time.sleep(0.5)

        lcd.setCursor(16, 1)
        lcd.autoscroll()

        for char in range(10):
            lcd.printString(char)
            time.sleep(0.5)

        lcd.noAutoscroll()
        lcd.clear()