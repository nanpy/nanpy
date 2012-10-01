#!/usr/bin/env python

# Author: Andrea Stagi <stagi.andrea@gmail.com>
# Description: just a test for Stepper module
# Dependencies: None

from nanpy import Stepper
from nanpy import Arduino

motor = Stepper(100, 9 , 10, 1000)

while True:
    motor.step(-10)
    Arduino.delay(1000)

