#!/usr/bin/env python

# Author: Kevin Ng 
# Description: read from EEPROM
# Dependencies: None

from nanpy import EEPROM
import sys

EEPROM_SIZE = EEPROM.size()


def display(a_list):
    for i in range(0, EEPROM_SIZE//16-1):
        for j in range(0, 15):
            sys.stdout.write( "%x : " % a_list[j+i*16])
        print


def read_eeprom():
    data_list = []
    for i in range(0, EEPROM_SIZE):
        s = EEPROM.read(i)
        data_list.append(s)
    return data_list


if __name__ == "__main__":
    print("Reading eeprom (%s bytes)..." % EEPROM_SIZE)
    display(read_eeprom())
