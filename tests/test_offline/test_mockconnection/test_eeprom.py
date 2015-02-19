from nose.tools import eq_, ok_

from nanpy.mock.mockconnection import MockConnection
from nanpy.eeprom import EEPROM


def test():
    mock = MockConnection()
    x = EEPROM(connection=mock)

    mock.objects['EEPROM'].memory = [1, 2, 3]
    eq_(x.size, 3)
    eq_(x.read(0), 1)
    eq_(x.read(1), 2)
    eq_(x.read(2), 3)

