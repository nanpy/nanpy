#!/usr/bin/env python

from nanpy.Arduino import Arduino
from nanpy.Lcd import Lcd
from nanpy.DallasTemperature import DallasTemperature

arduino = Arduino()

for i in range(4):
    arduino.digitalWrite(13, (i + 1) % 2)
    arduino.delay(10)

print "From the pin 13 I read %s" % arduino.digitalRead(13)

lcd = Lcd([7, 8, 9, 10, 11, 12], [16, 2])
lcd.printString("Loc. London")

temp = DallasTemperature(5)

while(1):
    lcd.setCursor(0, 1)
    lcd.printString("Ex.%0.0f\xDFC  In.%0.0f\xDFC" % (temp.getCelsius(), temp.getCelsius()))
    print temp.getCelsius()

