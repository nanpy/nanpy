#!/usr/bin/env python

# Author: Andrea Stagi <stagi.andrea@gmail.com>
# Description: just a test for DallasTemperature
# Dependencies: None

from nanpy import DallasTemperature

sensors = DallasTemperature(5)

while True:
    sensors.requestTemperatures()
    print sensors.getTempCByIndex(0)

