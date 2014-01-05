from nanpy.arduinoboard import arduinomethod, returns, FirmwareClass
from nanpy.classinfo import check4firmware


@check4firmware
class ArduinoApi(FirmwareClass):

    """access to Arduino public API functions."""
    firmware_id = 'A'

    LOW, HIGH = 0, 1
    INPUT, OUTPUT = 0, 1
    LSBFIRST, MSBFIRST = 0, 1

    @arduinomethod('dw')
    def digitalWrite(self, pin, value):
        pass

    @returns(int)
    @arduinomethod('r')
    def digitalRead(self, pin):
        pass

    @arduinomethod('aw')
    def analogWrite(self, pin, value):
        pass

    @returns(int)
    @arduinomethod('a')
    def analogRead(self, pin):
        pass

    @arduinomethod('pm')
    def pinMode(self, pin, mode):
        pass

    @returns(int)
    @arduinomethod('m')
    def millis(self):
        pass

    @returns(int)
    @arduinomethod('s')
    def shiftOut(self, dataPin, clockPin, bitOrder, value):
        """Shifts out a byte of data one bit at a time.

        :param dataPin: the pin on which to output each bit (int)
        :param clockPin: the pin to toggle once the dataPin has been set to the correct value (int)
        :param bitOrder: which order to shift out the bits; either MSBFIRST or LSBFIRST.
        :param value: the data to shift out. (byte)

        http://arduino.cc/en/Reference/shiftOut

        """
