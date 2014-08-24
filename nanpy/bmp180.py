from __future__ import division

import logging
from nanpy.i2c import I2C_Master
from nanpy.memo import memoized
import time


log = logging.getLogger(__name__)


def to_s16(n):
    return (n + 2 ** 15) % 2 ** 16 - 2 ** 15


class Bmp180(object):
    """Control of BMP180 Digital pressure sensor (I2C)

    calculation is based on Bosch datasheet."""

    def __init__(self, wire, address=0x77, oss=3):
        self.i2c = I2C_Master(wire)
        self.address = address
        self.oss = oss

    def read_bytes(self, address, count):
        self.i2c.send(self.address, [address])
        x = self.i2c.request(self.address, count)
        return x

    def write_byte(self, address, data):
        self.i2c.send(self.address, [address, data])

    @property
    @memoized
    def eeprom(self):
        return self.read_bytes(0xaa, 22)

    def read_temperature_raw(self):
        self.write_byte(0xf4, 0x2e)
        time.sleep(0.005)

        MSB, LSB = self.read_bytes(0xf6, 2)

        UT = (MSB << 8) + LSB
        return UT

    def read_pressure_raw(self):
        self.write_byte(0xf4, 0x34 + (self.oss << 6))
        time.sleep(0.005)
        MSB, LSB, XLSB = self.read_bytes(0xf6, 3)

        UP = ((MSB << 16) + (LSB << 8) + XLSB) >> (8 - self.oss)
        return UP

    @classmethod
    def calculate(cls, pressure_raw, temperature_raw, oss, eeprom):
        '''
        return: Pascal, Celsius
        '''
        UT = temperature_raw
        UP = pressure_raw

        def ushort(i):
            return (eeprom[2 * i] << 8) + eeprom[2 * i + 1]

        def short(i):
            return to_s16(ushort(i))

        AC1 = short(0)
        AC2 = short(1)
        AC3 = short(2)
        AC4 = ushort(3)
        AC5 = ushort(4)
        AC6 = ushort(5)
        B1 = short(6)
        B2 = short(7)
#         MB = short(8)
        MC = short(9)
        MD = short(10)

        X1 = ((UT - AC6) * AC5) >> 15
        X2 = (MC << 11) // (X1 + MD)
        B5 = X1 + X2
        T = (B5 + 8) >> 4

        B6 = B5 - 4000
        X1 = (B2 * ((B6 * B6) >> 12)) >> 11
        X2 = (AC2 * B6) >> 11
        X3 = X1 + X2
        B3 = (((AC1 * 4 + X3) << oss) + 2) // 4
        X1 = (AC3 * B6) >> 13
        X2 = (B1 * ((B6 * B6) >> 12)) >> 16
        X3 = ((X1 + X2) + 2) // 4
        B4 = (AC4 * (X3 + 32768)) >> 15
        B7 = (UP - B3) * (50000 >> oss)
        p = (B7 * 2) // B4 if B7 < 0x80000000 else (B7 // B4) * 2
        X1 = (p >> 8) * (p >> 8)
        X1 = (X1 * 3038) >> 16
        X2 = (-7357 * p) >> 16
        p += (X1 + X2 + 3791) >> 4

        return p, T / 10

    def read(self):
        '''
        return: Pascal, Celsius
        '''
        temperature_raw = self.read_temperature_raw()
        pressure_raw = self.read_pressure_raw()

        return self.calculate(
            pressure_raw,
            temperature_raw,
            self.oss,
            self.eeprom,
        )
