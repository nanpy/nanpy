#!/usr/bin/env python

# Author: Andrea Stagi <stagi.andrea@gmail.com>
# Description: just a test for DallasTemperature
# Dependencies: None

from nanpy import DallasTemperature

sensors = DallasTemperature(5)

while True:
    sensors.requestTemperatures()
    temp = sensors.getTempCByIndex(0)
    print temp
    print DallasTemperature.toFahrenheit(temp)

