#!/usr/bin/env python

from nanpy import SerialManager
from nanpy.lcd import Lcd
from nanpy.lcd_i2c import Lcd_I2C

I2C = True


def hello():
    connection = SerialManager(sleep_after_connect=2)

    cols, rows = 16, 2

    if I2C:
        pins = [0x27, 2, 1, 0, 4, 5, 6, 7, 3, 0]  # "ebay" version
        lcd = Lcd_I2C(pins, [cols, rows], connection=connection)
        lcd.setBacklight(0)
    else:
        pins = [7, 8, 9, 10, 11, 12]
        lcd = Lcd(pins, [cols, rows], connection=connection)

    lcd.setCursor(0, 0)
    lcd.printString('hello')

if __name__ == '__main__':
    hello()
