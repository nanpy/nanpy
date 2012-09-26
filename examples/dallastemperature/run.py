#!/usr/bin/env python

from nanpy import Lcd
from dallastemperature import DallasTemperature

lcd = Lcd([7, 8, 9, 10, 11, 12], [16, 2])
lcd.printString("Loc. London")

temp_int = DallasTemperature(5)
temp_ext = DallasTemperature(6)

while(1):
    lcd.setCursor(0, 1)
    lcd.printString("Ex.%0.0f\xDFC  In.%0.0f\xDFC" % (temp_int.getCelsius(), temp_ext.getCelsius()))

