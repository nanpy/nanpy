#!/usr/bin/env python

# Author: Kevin Ng
# Description: read from EEPROM
# Dependencies: None

from nanpy import (EepromLib, SerialManager)
import sys

connection = SerialManager()
e = EepromLib(connection=connection)


def display(a_list):
    for i in range(0, e.size // 16 - 1):
        for j in range(16):
            sys.stdout.write("%02x:" % a_list[j + i * 16])
        print


def read_eeprom():
    data_list = []
    for i in range(0, e.size):
        s = e.read(i)
        data_list.append(s)
    return data_list


if __name__ == "__main__":
    print("Reading eeprom (%s bytes)..." % e.size)
    display(read_eeprom())
