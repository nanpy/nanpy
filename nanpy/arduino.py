from nanpy.arduinoobject import (call_in_arduino, return_value)

class Arduino():

    @staticmethod
    def digitalWrite(pin, value):
        call_in_arduino('Arduino', 'digitalWrite', pin, value)
        return return_value()

    @staticmethod
    def digitalRead(pin):
        call_in_arduino('Arduino', 'digitalRead', pin)
        return return_value()

    @staticmethod
    def analogWrite(pin, value):
        call_in_arduino('Arduino', 'analogWrite', pin, value)
        return return_value()

    @staticmethod
    def analogRead(pin):
        call_in_arduino('Arduino', 'analogRead', pin)
        return return_value()

    @staticmethod
    def pinMode(pin, mode):
        call_in_arduino('Arduino', 'pinMode', pin, mode)
        return return_value()

    @staticmethod
    def delay(value):
        call_in_arduino('Arduino', 'delay', value)
        return return_value()

