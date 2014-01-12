from __future__ import division
from nanpy.arduinoboard import arduinomethod, returns, FirmwareClass
from nanpy.classinfo import check4firmware
import time


@check4firmware
class CounterLib(FirmwareClass):
    firmware_id = 'Counter'

    @arduinomethod
    def begin(self, gate_time_ms):
        pass

    @arduinomethod
    def end(self):
        pass

    @returns(bool)
    @arduinomethod
    def available(self):
        pass

    @returns(int)
    @arduinomethod
    def read(self):
        pass


class Counter(object):

    """Access to counter.

    Examples:

        Counter.read()

    original lib: http://www.pjrc.com/teensy/td_libs_FreqCount.html

    """
    def __init__(self, connection=None, F_CPU=None):
        self.connection = connection
        self.lib = CounterLib(connection)
        self.multiplier = 1
        if F_CPU:
            self.multiplier = self.calculate_multiplier(F_CPU)

    @classmethod
    def calculate_multiplier(cls, F_CPU):
        multiplier = 1
        # calculate multiplier for non supported frequencies
        if F_CPU >= 16000000:
            multiplier = F_CPU / 16000000
        elif F_CPU >= 8000000:
            multiplier = F_CPU / 8000000
        elif F_CPU >= 4000000:
            multiplier = F_CPU / 4000000
        elif F_CPU >= 2000000:
            multiplier = F_CPU / 2000000
        elif F_CPU >= 1000000:
            multiplier = F_CPU / 1000000
        else:
            multiplier = 1000000 / F_CPU
        return multiplier

    def read(self, gate_time=1):
        """read pulse count under ``gate_time`` seconds."""
        gate_time_ms = int(1000 * gate_time)
        self.lib.begin(gate_time_ms)
        try:
            time.sleep(gate_time * 1.1)
            n = self.lib.read()
        finally:
            self.lib.end()
        return n * self.multiplier

    def read_frequency(self, gate_time=1):
        """read frequency in hertz using ``gate_time`` in seconds."""
        return self.read(gate_time) / gate_time

    def error(self, gate_time=1):
        """frequency measurement error in hertz using ``gate_time`` in
        seconds."""
        return self.multiplier / gate_time
