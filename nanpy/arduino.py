from nanpy.arduinoboard import (call_static_method, return_value)

class Arduino():

    @staticmethod
    def digitalWrite(pin, value):
        call_static_method('Arduino', 'digitalWrite', pin, value)
        return return_value()

    @staticmethod
    def digitalRead(pin):
        call_static_method('Arduino', 'digitalRead', pin)
        return return_value()

    @staticmethod
    def analogWrite(pin, value):
        call_static_method('Arduino', 'analogWrite', pin, value)
        return return_value()

    @staticmethod
    def analogRead(pin):
        call_static_method('Arduino', 'analogRead', pin)
        return return_value()

    @staticmethod
    def pinMode(pin, mode):
        call_static_method('Arduino', 'pinMode', pin, mode)
        return return_value()

    @staticmethod
    def delay(value):
        call_static_method('Arduino', 'delay', value)
        return return_value()

