from nanpy.stepper import Stepper
from nose.tools import eq_, ok_

from nanpy.mock.mockconnection import MockConnection


def test():
    mock = MockConnection()
    x = Stepper(revsteps=100, pin1=3, pin2=4, connection=mock)
    x.step(3)
    x.setSpeed(3)
    
