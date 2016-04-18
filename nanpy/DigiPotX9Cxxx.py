# based on https:#sites.google.com/site/tfagerscode/home/digipotx9cxxx
from nanpy.util import constrain


DIGIPOT_MAX_AMOUNT = 99

LOW, HIGH = 0, 1
INPUT, OUTPUT = 0, 1


class DigiPot():
    _udLastValue = None
    _currentValue = None
    range = (0, DIGIPOT_MAX_AMOUNT)

    def __init__(self, incPin, udPin, csPin):
        self._incPin = incPin
        self._udPin = udPin
        self._csPin = csPin

        self._incPin.write_mode(OUTPUT)
        self._incPin.write_digital_value(HIGH)

        self._udPin.write_mode(OUTPUT)

        self._csPin.write_mode(OUTPUT)
        self._csPin.write_digital_value(LOW)

        self.set(0)

    def reset(self):
        # change down maximum number of times to ensure the value is 0
        self.decrease(DIGIPOT_MAX_AMOUNT)
        self._currentValue = 0

    def set(self, value):
        value = constrain(value, 0, DIGIPOT_MAX_AMOUNT)
        if self._currentValue is None:
            self.reset()
        if self._currentValue > value:
            self.change(-1, self._currentValue - value)
        elif self._currentValue < value:
            self.change(1, value - self._currentValue)

    def get(self):
        return self._currentValue

    def increase(self, amount):
        amount = constrain(amount, 0, DIGIPOT_MAX_AMOUNT)
        self.change(1, amount)

    def decrease(self, amount):
        amount = constrain(amount, 0, DIGIPOT_MAX_AMOUNT)
        self.change(-1, amount)

    def change(self, direction, amount):
        if direction == 1:
            ud = HIGH
        elif direction == -1:
            ud = LOW
        else:
            raise ValueError('invalid direction: %s', direction)

        amount = constrain(amount, 0, DIGIPOT_MAX_AMOUNT)
        if amount == 0:
            return

        if self._udLastValue != ud:
            self._udPin.write_digital_value(ud)

        for _ in range(amount):
            self._incPin.write_digital_value(LOW)
            self._incPin.write_digital_value(HIGH)
            if self._currentValue is not None:
                self._currentValue += direction
                self._currentValue = constrain(
                    self._currentValue,
                    0,
                    DIGIPOT_MAX_AMOUNT)
