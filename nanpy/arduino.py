from nanpy.arduinoboard import (call_static_method, return_value)

class Arduino():

    @staticmethod
    def digitalWrite(pin, value):
        return call_static_method('Arduino', 'digitalWrite', pin, value)

    @staticmethod
    def digitalRead(pin):
        return call_static_method('Arduino', 'digitalRead', pin)

    @staticmethod
    def analogWrite(pin, value):
        return call_static_method('Arduino', 'analogWrite', pin, value)

    @staticmethod
    def analogRead(pin):
        return call_static_method('Arduino', 'analogRead', pin)

    @staticmethod
    def pinMode(pin, mode):
        return call_static_method('Arduino', 'pinMode', pin, mode)

    @staticmethod
    def delay(value):
        return call_static_method('Arduino', 'delay', value)

