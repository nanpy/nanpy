import time

MUX0=1 << 0
MUX1=1 << 1
MUX2=1 << 2
MUX3=1 << 3
MUX4=1 << 4
MUX5=1 << 5
REFS0=1 << 6
REFS1=1 << 7

class Vcc(object):
    bandgap_voltage = 1.1  # Volt
    def __init__(self, register, MCU=None):
        self.register = register
        self.MCU = MCU

    def read(self):
        """VCC in Volt. Bandgap voltage precision: +-10%

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
        
        
        if self.MCU in ['__AVR_ATmega32U4__' , '__AVR_ATmega1280__' , '__AVR_ATmega2560__']:
            cfg = REFS0 | MUX4 | MUX3 | MUX2 | MUX1
        elif self.MCU in ['__AVR_ATtiny24__' , '__AVR_ATtiny44__' , '__AVR_ATtiny84__']:
            cfg = MUX5 | MUX0
        elif self.MCU in ['__AVR_ATtiny25__' , '__AVR_ATtiny45__' , '__AVR_ATtiny85__']:
            cfg = MUX3 | MUX2
        else:
            cfg = REFS0 | MUX3 | MUX2 | MUX1
        
        reg.ADMUX = cfg
        # Wait for Vref to settle
        time.sleep(0.002)
        # Convert
        reg.ADCSRA |= 0x40  # 0b01000000 = _BV(ADSC)
        while reg.ADCSRA & 0x40:  # bit_is_set(ADCSRA, ADSC)
            time.sleep(0.001)
        result = reg.ADCL | (reg.ADCH << 8)
        
        result = (self.bandgap_voltage * 1024) / result
        return result
