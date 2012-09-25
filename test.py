#!/usr/bin/env python

from nanpy.Arduino import Arduino
from nanpy.Lcd import Lcd
from DallasTemperature import DallasTemperature

arduino = Arduino()

arduino.pinMode(13, 1)

for i in range(4):
    arduino.digitalWrite(13, (i + 1) % 2)
    arduino.delay(10)

lcd = Lcd([7, 8, 9, 10, 11, 12], [16, 2])
lcd.printString("Loc. London")

temp_int = DallasTemperature(5)
temp_ext = DallasTemperature(6)

while(1):
    lcd.setCursor(0, 1)
    lcd.printString("Ex.%0.0f\xDFC  In.%0.0f\xDFC" % (temp_int.getCelsius(), temp_ext.getCelsius()))

