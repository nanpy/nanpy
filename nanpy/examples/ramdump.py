#!/usr/bin/env python

# Description: read all RAM

from nanpy.arduinotree import ArduinoTree
from nanpy.serialmanager import SerialManager
import sys


def display(a_list, size):
    for i in range(0, size // 16 - 1):
        for j in range(16):
            sys.stdout.write('%02x:' % a_list[j + i * 16])
        print


def ramdump():
    connection = SerialManager()
    a = ArduinoTree(connection=connection)
    size = a.ram.size
    free = a.ram.free()
    print('Reading RAM (%s bytes, %s bytes free)...' % (size, free))

    data_list = []
    for i in range(0, size):
        s = a.ram.read(i)
        data_list.append(s)

    display(data_list, size)


if __name__ == '__main__':
    ramdump()
