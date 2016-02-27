#!/usr/bin/env python

from nanpy.lcd import Lcd


if __name__ == '__main__':

    pins = [7, 8, 9, 10, 11, 12]
    cols, rows = 16, 2
    lcd = Lcd(pins, [cols, rows])
    
    smiley = [
        0b00000,
        0b10001,
        0b00000,
        0b00000,
        0b10001,
        0b01110,
        0b00000,
        0b00000
    ]

    lcd.createChar(0,smiley)
    lcd.setCursor(0,0)
    lcd.write(0)
