from nanpy.servo import Servo
from nose.tools import eq_, ok_

from nanpy.mock.mockconnection import MockConnection


def test():
    mock = MockConnection()
    x = Servo(pin=3, connection=mock)
    
    ok_(x.attached())
    x.write(42)
    eq_(x.read(), 42)
    

def test_more():
    mock = MockConnection()
    
    def objs():
        return mock.objects['Servo'].objects
    
    eq_(len(objs()), 0)

    x1 = Servo(pin=5, connection=mock)

    eq_(len(objs()), 1)
    
    x2 = Servo(pin=6, connection=mock)
    
    eq_(len(objs()), 2)
    
 