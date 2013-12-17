from nanpy.arduinoboard import arduinoclassmethod, returns
from nanpy.memo import memoized


def auto_convert(x):
    try:
        return int(x)
    except ValueError:
        return x


class Define(object):

    @classmethod
    @memoized
    @returns(int)
    @arduinoclassmethod
    def count(cls):
        pass

    @classmethod
    @memoized
    @arduinoclassmethod
    def name(cls, index):
        pass

    @classmethod
    @memoized
    @returns(auto_convert)
    @arduinoclassmethod
    def value(cls, index):
        pass

    @classmethod
    @memoized
    def asDict(cls):
        d = dict()
        for i in range(cls.count()):
            d[cls.name(i)] = cls.value(i)
        return d
