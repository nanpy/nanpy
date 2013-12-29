from easyprocess import EasyProcess
from nose.tools import eq_
from util import tmpdir
import os
import shutil


FIRMWARE = os.path.dirname(__file__) + '/../firmware/Nanpy'


def test_make():
    dest = tmpdir() + '/Nanpy'
    shutil.copytree(FIRMWARE, dest)
    p = EasyProcess('make size BOARD=uno', cwd=dest).call()
    eq_(p.return_code, 0)
