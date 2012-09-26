#!/usr/bin/env python

from nanpy import Arduino

Arduino.pinMode(13, 1)

for i in range(4):
    Arduino.digitalWrite(13, (i + 1) % 2)
    Arduino.delay(1000)

