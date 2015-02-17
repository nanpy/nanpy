from nanpy.ram import RAM
from nose.tools import eq_, ok_

from nanpy.mock.mockconnection import MockConnection


def test():
    mock = MockConnection()
    x = RAM(connection=mock)
    
    mock.objects['RAM'].memory = [1, 2, 3]
    mock.objects['RAM'].free = 2
    eq_(x.size, 3)
    eq_(x.free(), 2)
    eq_(x.read(0), 1)
    eq_(x.read(1), 2)
    eq_(x.read(2), 3)
    
