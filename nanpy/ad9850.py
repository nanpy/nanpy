from __future__ import division
from nanpy.arduinotree import ArduinoTree
from nanpy.memo import memoized
from nanpy.shiftout import ShiftOut


LOW, HIGH = 0, 1
OUTPUT = 1


class AD9850(object):

    """controllling the AD9850 DDS module.

    code is based on this info: http://nr8o.dhlpilotcentral.com/?p=83

    """
    clock = 125000000  # note 125 MHz clock on 9850
    _frequency = 0

    def __init__(self, pin_names, connection=None):
        '''
        :param pin_names: [W_CLK, FQ_UD, DATA, RESET]
        W_CLK      // Pin 8 - connect to AD9850 module word load clock pin (CLK)
        FQ_UD        // Pin 9 - connect to freq update pin (FQ)
        DATA        // Pin 10 - connect to serial data load pin (DATA)
        RESET       // Pin 11 - connect to reset pin (RST).
        '''
        self.connection = connection
        self.pin_names = dict(
            W_CLK=pin_names[0],
            FQ_UD=pin_names[1],
            DATA=pin_names[2],
            RESET=pin_names[3])

    @property
    @memoized
    def arduino(self):
        return ArduinoTree(connection=self.connection)

    def create_pin_object(self, name):
        return self.arduino.pin.get(self.pin_names[name])

    @property
    @memoized
    def W_CLK(self):
        return self.create_pin_object('W_CLK')

    @property
    @memoized
    def FQ_UD(self):
        return self.create_pin_object('FQ_UD')

    @property
    @memoized
    def DATA(self):
        return self.create_pin_object('DATA')

    @property
    @memoized
    def RESET(self):
        return self.create_pin_object('RESET')

    @property
    @memoized
    def shift(self):
        return ShiftOut(self.DATA, self.W_CLK, 0, connection=self.connection)

    def pulse_high(self, pin):
        pin.write_digital_value(HIGH)
        pin.write_digital_value(LOW)

    def setup(self):
        self.FQ_UD.write_mode(OUTPUT)
        self.W_CLK.write_mode(OUTPUT)
        self.DATA.write_mode(OUTPUT)
        self.RESET.write_mode(OUTPUT)

        self.pulse_high(self.RESET)
        self.pulse_high(self.W_CLK)
        # this pulse enables serial mode - Datasheet page 12 figure 10
        self.pulse_high(self.FQ_UD)

    def tfr_byte(self, value):
        self.shift.write_data(value)

    def write_frequency(self, frequency):
        # frequency calc from datasheet page 8 =
        # <sys clock> * <frequency tuning word>/2^32
        CONST = 4294967295  # 2^32 - 1
        freq = frequency * CONST / self.clock
        freq = int(freq)
        for b in range(4):
            self.tfr_byte((freq >> (8 * b)) & 0xFF)

        self.tfr_byte(0x000)  # Final control byte, all 0 for 9850 chip
        self.pulse_high(self.FQ_UD)  # Done!  Should see output
        self._frequency = frequency

    # frequency read is not implemented
    frequency = property(lambda self: self._frequency, write_frequency)
