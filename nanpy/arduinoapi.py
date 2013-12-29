from nanpy.arduinoboard import arduinomethod, returns, FirmwareClass
from nanpy.classinfo import check4firmware


@check4firmware
class ArduinoApi(FirmwareClass):

    """access to Arduino public API functions."""
    firmware_id = 'A'

    LOW, HIGH = 0, 1
    INPUT, OUTPUT = 0, 1

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
