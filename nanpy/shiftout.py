from nanpy.arduinoapi import ArduinoApi
from nanpy.arduinopin import to_pin_number


class ShiftOut(object):
    LSBFIRST, MSBFIRST = 0, 1

    def __init__(self, data_pin, clock_pin,
                 bit_order=0, connection=None, A0=None):
        """Shifts out a byte of data one bit at a time.

        :param data_pin: the pin on which to output each bit (int or string)
        :param clock_pin: the pin to toggle once the dataPin has been set to the correct value (int or string)
        :param bit_order: which order to shift out the bits; either MSBFIRST or LSBFIRST.

        """
        if connection and hasattr(connection, 'shiftOut'):
            self._shiftOut_func = connection.shiftOut
        else:
            api = ArduinoApi(connection=connection)
            self._shiftOut_func = api.shiftOut
        self.bit_order = bit_order
        self.data_pin_number = to_pin_number(data_pin, A0)
        self.clock_pin_number = to_pin_number(clock_pin, A0)

    def write_data(self, data):
        """Shifts out a byte of data one bit at a time.

        :param data: the data to shift out. (byte)

        """
        self._shiftOut_func(
            self.data_pin_number,
            self.clock_pin_number,
            self.bit_order,
            data)
