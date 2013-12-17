from __future__ import division
from nanpy.memo import memoized
from nanpy.arduino import Arduino
from nanpy.arduinocore import ArduinoCore
from nanpy.define import Define
from nanpy.resgister import Register
import logging

log = logging.getLogger(__name__)


class PwmError(Exception):
    pass


class BiDict():

    def __init__(self, dic):
        self.norm = dic
        self.inv = dict([(v, k) for k, v in dic.items()])

base_divisor = {
    3: 512,
    5: 256,
    6: 256,
    9: 512,
    10: 512,
    11: 512,
}


_div1 = BiDict({
               #                0: None,
               1: 1,
               2: 8,
               3: 64,
               4: 256,
               5: 1024,
               #                6: None,
               #                7: None,
               })
_div2 = BiDict({
               #                0: None,
               1: 1,
               2: 8,
               3: 32,
               4: 64,
               5: 128,
               6: 256,
               7: 1024,
               })
divisor_mapping = {
    3: _div2,
    5: _div1,
    6: _div1,
    9: _div1,
    10: _div1,
    11: _div2,
}

TIMERS_A = ['NOT_ON_TIMER',
            'TCCR0A',
            'TCCR0A',
            'TCCR1A',
            'TCCR1A',
            None,  # TODO: atmega8
            'TCCR2A',
            'TCCR2A',
            ]

TIMERS_B = ['NOT_ON_TIMER',
            'TCCR0B',
            'TCCR0B',
            'TCCR1B',
            'TCCR1B',
            'TCCR2',
            'TCCR2B',
            'TCCR2B',
            ]

timer_mask = 7  # 0b111

# TODO: pwm_mode  read/write
# TODO: read mappings


class ArduinoPwmPin(object):
    DEFAULT_DIVISOR = 64

    def __init__(self, nr):
        self.nr = nr
        self.F_CPU = Define().asDict().get('F_CPU')

    def reset(self):
        if not self.available:
            return
        self.write_divisor(self.DEFAULT_DIVISOR)

    @property
    def available(self):
        timer_id = self._timer_id()
        return timer_id > 0 and timer_id < len(TIMERS_B)
#        return self.nr in timer_register

    def _check(self):
        if not self.available:
            raise PwmError('pwm not available for pin: %s' % self.nr)

    def write_value(self, value):
        self._check()
#         assert self.mcu.pins.read_mode(self.nr) == OUTPUT
        Arduino.analogWrite(self.nr, value)

    @property
    def divisors_available(self):
        try:
            return list(divisor_mapping[self.nr].norm.values())
        except KeyError:
            return []

    def read_divisor(self):
        self._check()
        d = divisor_mapping[self.nr]
        return d.norm[self.read_timer_mode()]

    def write_divisor(self, value):
        self._check()
        d = divisor_mapping[self.nr]
        self.write_timer_mode(d.inv[value])
    divisor = property(read_divisor, write_divisor)

    def _timer_id(self):
        return ArduinoCore.digitalPinToTimer(self.nr)

    def _timer_register_name(self, variant='B'):
        self._check()
        i = self._timer_id()
        return dict(A=TIMERS_A, B=TIMERS_B)[variant][i]

    @property
    def timer_register_name_a(self):
        return self._timer_register_name(variant='A')

    @property
    def timer_register_name_b(self):
        return self._timer_register_name(variant='B')

    def read_timer_mode(self):
        reg_name = self.timer_register_name_b
        return Register(reg_name).read_value() & timer_mask

    def write_timer_mode(self, value):
        assert value <= 7
        reg_name = self.timer_register_name_b
        reg = Register(reg_name)
        old = reg.value & ~timer_mask
        reg.value = (old | value)

    timer_mode = property(read_timer_mode, write_timer_mode)

    @property
    def base_divisor(self):
        self._check()
        return base_divisor[self.nr]

    def calculate_frequency(self, divisor):
        return 1.0 * self.F_CPU / self.base_divisor / divisor

    @property
    def frequencies_available(self):
        ls = sorted([self.calculate_frequency(x)
                    for x in self.divisors_available])
        return ls

    def read_frequency(self):
        self._check()
        wgm = self.read_wgm()
        if wgm == 14:
            # high freq mode
            return self.F_CPU / Register('ICR1').value
        else:
            return self.calculate_frequency(self.read_divisor())

    def write_frequency(self, value):
        self._check()
        d = divisor_mapping[self.nr]
        for x in self.divisors_available:
            f = self.calculate_frequency(x)
            if abs(f - value) <= 1:
                self.write_timer_mode(d.inv[x])
                return
    frequency = property(read_frequency, write_frequency)

    def read_wgm(self):
        """Waveform generation mode."""
        self._check()
        rega = self.timer_register_name_a
        regb = self.timer_register_name_b
        if regb == 'TCCR1B':
            maskb = 24  # 0b00011000
        else:
            maskb = 8  # 0b00001000
        maska = 3  # 0b00000011
        a = Register(rega).value & maska
        b = Register(regb).value & maskb
        return a + (b >> 1)

    wgm = property(read_wgm, None)

    def _check_high_freq(self):
        # TODO: read config
        if self.nr not in [9, 10]:
            raise PwmError('high freq pwm not available for pin: %s' % self.nr)

    def set_high_freq_around_pwm(self, top, fill):
        'F_CPU/divisor'
        # TODO:
        d = top
        self._check_high_freq()
        assert d >= 2

        self.write_divisor(1)
        self.write_value(128)

        TCCR1A = Register('TCCR1A')
        TCCR1B = Register('TCCR1B')
        TCNT1 = Register('TCNT1')
        ICR1 = Register('ICR1')
        OCR1A = Register('OCR1A')
        OCR1B = Register('OCR1B')

        TCCR1A.value = 2 + \
            (240 & TCCR1A.value)  # 0b00000010 + (0b11110000 & reg.TCCR1A)
        TCCR1B.value = 25  # 0b00011001

        TCNT1.value = 0
        ICR1.value = d
        OCR1A.value = fill
        OCR1B.value = fill

    def set_high_freq_around(self, freq):
        top = int(self.F_CPU / freq + 0.5)
        assert 1 < top < (1 << 16)
        self.set_high_freq_around_pwm(top, int(top / 2))
