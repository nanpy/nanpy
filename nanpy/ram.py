from nanpy.arduinoboard import arduinomethod, returns, FirmwareClass
from nanpy.classinfo import check4firmware
from nanpy.memo import memoized


@check4firmware
class RAM(FirmwareClass):
    firmware_id = 'RAM'

    @arduinomethod
    def write(self, address, value):
        pass

    @returns(int)
    @arduinomethod
    def read(self, address):
        pass

    @property
    @memoized
    @returns(int)
    @arduinomethod
    def size(self):
        pass

    @returns(int)
    @arduinomethod
    def free(self):
        pass
