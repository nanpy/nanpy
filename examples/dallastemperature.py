#!/usr/bin/env python

# Author: Andrea Stagi <stagi.andrea@gmail.com>
# Description: just a test for DallasTemperature
# Dependencies: None

from nanpy import DallasTemperature

sensors = DallasTemperature(5)

while True:
    sensors.requestTemperatures()
    temp = sensors.getTempCByIndex(0)
    print "The temperature, in Celsius degrees is %0.2f" % temp
    print "Let's convert it in Fahrenheit degrees: %0.2f" % DallasTemperature.toFahrenheit(temp)

