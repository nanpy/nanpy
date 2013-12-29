import time


class Vcc(object):

    def __init__(self, register):
        self.register = register

    def read(self):
        """VCC in Volt. This works on Arduinos with a 328 or 168 only.

        Source: http://code.google.com/p/tinkerit/wiki/SecretVoltmeter

        How it works

        The Arduino 328 and 168 have a built in precision voltage reference of 1.1V.
        This is used sometimes for precision measurement,
        although for Arduino it usually makes more sense to measure against Vcc,
        the positive power rail.
        The chip has an internal switch that selects which pin the analogue to digital converter reads.
        That switch has a few leftover connections, so the chip designers wired them up to useful signals.
        One of those signals is that 1.1V reference.
        So if you measure how large the known 1.1V reference is in comparison to Vcc,
        you can back-calculate what Vcc is with a little algebra. That is how this works.

        """

        reg = self.register.proxy
        # 0b01001110 = _BV(REFS0) | _BV(MUX3) | _BV(MUX2) | _BV(MUX1)
        reg.ADMUX = 0x4E
        # Wait for Vref to settle
        time.sleep(0.002)
        # Convert
        reg.ADCSRA |= 0x40  # 0b01000000 = _BV(ADSC)
        while reg.ADCSRA & 0x40:  # bit_is_set(ADCSRA, ADSC)
            time.sleep(0.001)
        result = reg.ADCL | (reg.ADCH << 8)
        bandgap_voltage = 1.1  # Volt
        result = (bandgap_voltage * 1023) / result
        return result
