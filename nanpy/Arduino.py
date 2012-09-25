from ArduinoObject import ArduinoSingleObject
import Singleton

class Arduino(ArduinoSingleObject):

    def __init__(self):
        ArduinoSingleObject.__init__(self, "Arduino")

    def digitalWrite(self, pin, value):
        self.call('digitalWrite', pin, value)
        return self._return_value()

    def digitalRead(self, pin):
        self.call('digitalRead', pin)
        return self._return_value()

    def analogWrite(self, pin, value):
        self.call('analogWrite', pin, value)
        return self._return_value()

    def analogRead(self, pin):
        self.call('analogRead', pin)
        return self._return_value()

    def pinMode(self, pin, mode):
        self.call('pinMode', pin, mode)
        return self._return_value()

    def delay(self, value):
        self.call('delay', value)
        return self._return_value()

