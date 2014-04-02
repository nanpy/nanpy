from config import config
from nanpy.arduinotree import ArduinoTree
from nanpy.register import RegisterFeature
from nanpy.vcc import Vcc
from nose.tools import eq_, ok_
from tests.util import ok_vcc
import common


def setup():
    common.setup()


def test_vcc():
    a = ArduinoTree()
    ok_vcc(a.vcc.read())


def test_vcc2():
    vcc = Vcc(RegisterFeature())
    ok_vcc(vcc.read())
