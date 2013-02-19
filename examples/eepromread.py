#!/usr/bin/env python

# Author: Kevin Ng 
# Description: read from EEPROM
# Dependencies: None

from nanpy import EEPROM
import sys

EEPROM_SIZE = 1024//4  #only read first 256 bytes 


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
    print("Reading first 256 bytes of eeprom...")
    display(read_eeprom())
