from __future__ import with_statement
from config import config
from nanpy.arduinotree import ArduinoTree
from nanpy.shiftout import ShiftOut
from nose.tools import ok_
from nose.tools import eq_
import common


A0 = config['A0']


def setup():
    common.setup()


def test_shift1():
    s = ShiftOut('D13', 'D12', 0, A0=A0)
    s.write_data(0b01010101)


def test_shift2():
    s = ShiftOut(13, 'A1', 0, A0=A0)
    s.write_data(0b01010101)


def test_shift3():
    a = ArduinoTree()
    p = a.pin.get(13)
    s = ShiftOut(p, 12, 0, A0=A0)
    s.write_data(0b01010101)
