from nanpy.arduinoboard import arduinomethod, returns, FirmwareClass
from nanpy.classinfo import check4firmware
from nanpy.memo import memoized


@check4firmware
class ArduinoCore(FirmwareClass):

    """Access to Arduino functions which are not part of the public API."""

    firmware_id = 'Core'

    @memoized
    @returns(int)
    @arduinomethod
    def digitalPinToBitMask(self, pin):
        """nonpublic Arduino function."""

    @memoized
    @returns(int)
    @arduinomethod
    def digitalPinToPort(self, pin):
        """nonpublic Arduino function."""

    @memoized
    @returns(int)
    @arduinomethod
    def digitalPinToTimer(self, pin):
        """nonpublic Arduino function."""

    @memoized
    @returns(int)
    @arduinomethod
    def analogInPinToBit(self, pin):
        """nonpublic Arduino function."""

    @memoized
    @returns(int)
    @arduinomethod
    def portOutputRegister(self, port):
        """nonpublic Arduino function.

        @return: RAM address

        """

    @memoized
    @returns(int)
    @arduinomethod
    def portInputRegister(self, port):
        """nonpublic Arduino function.

        @return: RAM address

        """

    @memoized
    @returns(int)
    @arduinomethod
    def portModeRegister(self, port):
        """nonpublic Arduino function.

        @return: RAM address

        """
