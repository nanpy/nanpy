from easyprocess import EasyProcess
from nose.tools import eq_
from path import path
from util import tmpdir


FIRMWARE = path(__file__).parent.parent.abspath() / 'firmware' / 'Nanpy'


def test_make():
    dest = path(tmpdir()) / 'Nanpy'
    FIRMWARE.copytree(dest)

    p = EasyProcess('make size BOARD=uno', cwd=dest).call()
    eq_(p.return_code, 0)
