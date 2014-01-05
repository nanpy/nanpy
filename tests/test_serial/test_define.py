from config import config
from nose.tools import eq_, ok_
import common
from nanpy.arduinotree import ArduinoTree
from nanpy.define import DefineFeature


def setup():
    common.setup()


def test_defs():
    a = ArduinoTree()

    eq_(a.define.get('A0'), config['A0'])

    d = a.define.as_dict
    print (d)

    eq_(a.define.get('ARDUINO'), config['ARDUINO'])
    eq_(d['ARDUINO'], config['ARDUINO'])

    eq_(d['A0'], config['A0'])
    eq_(d['F_CPU'], config['F_CPU'])
    eq_(d['MCU'], config['MCU'])
    ok_('xx' not in d)
    ok_(len(d.keys()) > 15, len(d.keys()))

    ARDUINO = a.define.get('ARDUINO')
    ok_(ARDUINO >= 100)
    ok_(ARDUINO < 200)

    NUM_DIGITAL_PINS = a.define.get('NUM_DIGITAL_PINS')
    ok_(NUM_DIGITAL_PINS >= 10)
    ok_(NUM_DIGITAL_PINS < 1000)

    for x in d:
        assert x.strip(), 'empty define:-->%s<--' % x


def test_defs2():
    a = ArduinoTree()
    define = DefineFeature()
    eq_(define.as_dict, a.define.as_dict)
