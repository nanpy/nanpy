#!/usr/bin/env python

# Author: Andrea Stagi <stagi.andrea@gmail.com>
# Description: a fake DallasTemperature library written in Python
# Dependencies: None

from nanpy import (Arduino, OneWire)
import time

class FakeDallasTemperature():

    def __init__(self, pin):
        self.__ds = OneWire(pin)
        self.__data = 0

    def __fetchAddress(self):
        ds_address = self.__ds.search()

        if ds_address == "1":
            return False

        self.__ds.reset()
        self.__ds.select(ds_address)
        self.__ds.write(0x44, 1)
        Arduino.delay(700)
        present = self.__ds.reset()
        self.__ds.select(ds_address)
        self.__ds.write(0xBE)
        return True

    def __fetchData(self):

        data = []

        for i in range(9):
            val = self.__ds.read()
            data.append(val)

        raw = (data[1] << 8) | data[0]

        type = 1

        if type == 0:

            raw = raw << 3;
            if data[7] == 0x10:
                raw = (raw & 0xFFF0) + 12 - data[6]

        else:
            cfg = (data[4] & 0x60)

            if cfg == 0x00:
                raw = raw << 3
            elif cfg == 0x20:
                raw = raw << 2
            elif cfg == 0x40:
                raw = raw << 1
            else:
                pass

        self.__data = raw

    def getCelsius(self):
        if self.__fetchAddress():
            self.__fetchData()
        return self.__data / 16.0

    def getFahrenheit(self):
        if self.__fetchAddress():
            self.__fetchData()
        return self.getCelsius() * 1.8 + 32.0


from nanpy import Lcd

if __name__ == "__main__":

    lcd = Lcd([7, 8, 9, 10, 11, 12], [16, 2])
    lcd.printString("Loc. London")

    temp_int = FakeDallasTemperature(6)
    temp_ext = FakeDallasTemperature(5)

    while(1):
        lcd.setCursor(0, 1)
        lcd.printString("Ex.%0.0f\xDFC  In.%0.0f\xDFC" % (temp_int.getCelsius(), temp_ext.getCelsius()))

