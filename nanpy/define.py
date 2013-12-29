from nanpy.arduinoboard import arduinoclassmethod, returns
from nanpy.memo import memoized


def auto_convert(x):
    try:
        return int(x)
    except ValueError:
        return x


class Define(object):

    """Access to firmware constants.

    Examples:

        Define.asDict().get('F_CPU') # AVR frequency
        Define.asDict().get('__DATE__') # firmware upload date

    """

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
        """return all constants and their values in a dictionary."""
        d = dict()
        for i in range(cls.count()):
            d[cls.name(i)] = cls.value(i)
        return d
