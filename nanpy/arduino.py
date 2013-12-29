from nanpy.arduinoboard import arduinoclassmethod, returns, FirmwareClass
import time


class Arduino(FirmwareClass):
    firmware_id = 'A'

    LOW, HIGH = 0, 1
    INPUT, OUTPUT = 0, 1

    @classmethod
    @arduinoclassmethod('dw')
    def digitalWrite(cls, pin, value):
        pass

    @classmethod
    @returns(int)
    @arduinoclassmethod('r')
    def digitalRead(cls, pin):
        pass

    @classmethod
    @arduinoclassmethod('aw')
    def analogWrite(cls, pin, value):
        pass

    @classmethod
    @returns(int)
    @arduinoclassmethod('a')
    def analogRead(cls, pin):
        pass

    @classmethod
    @arduinoclassmethod('pm')
    def pinMode(cls, pin, mode):
        pass

    @classmethod
    def delay(cls, value):
        time.sleep(float(value)/1000)
        
    @classmethod
    @returns(int)
    @arduinoclassmethod('m')
    def millis(cls):
        pass

    @classmethod
    def map(cls, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

