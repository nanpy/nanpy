import logging
from nanpy.i2c import I2C_Master


log = logging.getLogger(__name__)


class PCF8574_Error(Exception):
    pass


class PCF8574(object):

    def __init__(self, wire, address):
        self._address = address
        self.master = I2C_Master(wire)

    def read8(self):
        ls = self.master.request(self._address, 1)

        # HACK: without beginTransmission all second read is empty
        self.master.wire.beginTransmission(self._address)
        error_code = self.master.wire.endTransmission()

        if len(ls) >= 1:
            return ls[0]
        else:
            raise PCF8574_Error('no data received from PCF8574')

    def write8(self, value):
        self.master.send(self._address, [value])

    def readPin(self, pin):
        d = self.read8()
        return (d & (1 << pin)) > 0

    def writePin(self, pin, value):
        d = self.read8()
        if value:
            d |= (1 << pin)
        else:
            d &= ~(1 << pin)
        self.write8(d)
