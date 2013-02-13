#!/usr/bin/env python

# Author: Andrea Stagi <stagi.andrea@gmail.com>
# Description: write and read from EEPROM
# Dependencies: None

from nanpy import EEPROM

print("Write 33 on the EEPROM at address 100")
EEPROM.write(100, 33)
print("The value at address 100 is %d" % EEPROM.read(100))

