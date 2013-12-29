from nanpy.arduinotree import ArduinoTree
from nanpy.serialmanager import serial_manager
from nose.tools import ok_
import tempfile


def exc_(excClass, callableObj, *args, **kwargs):
    """Fail unless an exception of class excClass is thrown by callableObj when
    invoked with arguments args and keyword arguments kwargs.

    If a different type of exception is thrown, it will not be caught,
    and the test case will be deemed to have suffered an error, exactly
    as for an unexpected exception.

    """
    try:
        callableObj(*args, **kwargs)
    except excClass:
        return
    else:
        if hasattr(excClass, '__name__'):
            excName = excClass.__name__
        else:
            excName = str(excClass)
        raise Exception('%s not raised' % excName)


def ok_an(x, pullup=False):
    print (x)
    ok_(x in range(1024))


def ok_vcc(vcc):
    print ('vcc=', vcc)
    ok_(vcc < 5.5)
    ok_(vcc > 3)


def tmpdir(dir=None, suffix=''):
    x = tempfile.mkdtemp(suffix=suffix, prefix='nanpy_test_', dir=dir)
    return x
