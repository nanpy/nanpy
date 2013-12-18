from config import config
from nanpy.define import Define
from nanpy.watchdog import Watchdog
from nose.tools import eq_, ok_
from util import exc_


def setup():
    Watchdog.soft_reset()

def teardown():
    pass


def test_defs():
    d = Define.asDict()
    print (d)
    eq_(d['A0'], config['A0'])
    eq_(d['ARDUINO'], config['ARDUINO'])
    eq_(d['F_CPU'], config['F_CPU'])
    eq_(d['MCU'], config['MCU'])
    ok_('xx' not in d)
    ok_(len(d.keys()) > 15, len(d.keys()))

    for x in d:
        assert x.strip(), 'empty define:-->%s<--' % x


