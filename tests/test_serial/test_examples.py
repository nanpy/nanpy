from nanpy.examples.boottime import boot_time
from nanpy.examples.checkspeed import checkspeed
from nanpy.examples.counterdemo import counterdemo
from nanpy.examples.dds import dds
from nanpy.examples.dump import dumpall
from nanpy.examples.highfreqpwm import highfreqpwm
from nanpy.examples.ramdump import ramdump
from nanpy.examples.reset import reset_demo
import common


def setup():
    common.setup()


def test_dump():
    dumpall()


def test_boot_time():
    boot_time()


def test_reset_demo():
    reset_demo()


def test_highfreqpwm():
    highfreqpwm()


def test_counter():
    counterdemo()


def test_dds():
    dds()


def test_checkspeed():
    checkspeed(n=1)


def test_ramdump():
    ramdump()
