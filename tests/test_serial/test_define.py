from config import config
from nose.tools import eq_, ok_
from tests.util import soft_reset
from nanpy.arduinotree import ArduinoTree
from nanpy.define import DefineFeature


def setup():
    soft_reset()


def test_defs():
    a = ArduinoTree()
    d = a.define.as_dict
    print (d)

    eq_(a.define.get('ARDUINO'), config['ARDUINO'])
    eq_(d['ARDUINO'], config['ARDUINO'])

    eq_(d['A0'], config['A0'])
    eq_(d['F_CPU'], config['F_CPU'])
    eq_(d['MCU'], config['MCU'])
    ok_('xx' not in d)
    ok_(len(d.keys()) > 15, len(d.keys()))

    for x in d:
        assert x.strip(), 'empty define:-->%s<--' % x


def test_defs2():
    a = ArduinoTree()
    define = DefineFeature()
    eq_(define.as_dict, a.define.as_dict)
