from nanpy.memo import memoized
from nose.tools import eq_


class TestClass(object):
    i = 1

    @memoized
    def met(self, x):
        TestClass.i += 1
        return TestClass.i


def test1():
    o = TestClass()
    eq_(o.i, 1)
    o.met(3)
    eq_(o.i, 2)
    o.met(3)
    eq_(o.i, 2)
    o.met(4)
    eq_(o.i, 3)
    o.met(4)
    o.met(4)
    o.met(3)
    o.met(3)
    o.met(4)
    eq_(o.i, 3)

    o2 = TestClass()
    eq_(o.i, 3)
    o2.met(4)
    o2.met(4)
    o2.met(4)
    o2.met(4)
    eq_(o.i, 4)
