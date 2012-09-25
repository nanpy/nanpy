import ArduinoObject

class Arduino():

    @staticmethod
    def digitalWrite(pin, value):
        ArduinoObject.call_in_arduino('Arduino', 'digitalWrite', pin, value)
        return ArduinoObject.return_value()

    @staticmethod
    def digitalRead(pin):
        ArduinoObject.call_in_arduino('Arduino', 'digitalRead', pin)
        return ArduinoObject.return_value()

    @staticmethod
    def analogWrite(pin, value):
        ArduinoObject.call_in_arduino('Arduino', 'analogWrite', pin, value)
        return ArduinoObject.return_value()

    @staticmethod
    def analogRead(pin):
        ArduinoObject.call_in_arduino('Arduino', 'analogRead', pin)
        return ArduinoObject.return_value()

    @staticmethod
    def pinMode(pin, mode):
        ArduinoObject.call_in_arduino('Arduino', 'pinMode', pin, mode)
        return ArduinoObject.return_value()

    @staticmethod
    def delay(value):
        ArduinoObject.call_in_arduino('Arduino', 'delay', value)
        return ArduinoObject.return_value()

