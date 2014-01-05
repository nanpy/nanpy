from nanpy.arduinoboard import arduinomethod, returns, FirmwareClass
from nanpy.classinfo import check4firmware
from nanpy.memo import memoized


def auto_convert(x):
    try:
        return int(x)
    except ValueError:
        return x


@check4firmware
class DefineArray(FirmwareClass):
    firmware_id = 'D'

    @property
    @memoized
    @returns(int)
    @arduinomethod('c')
    def count(self):
        pass

    @memoized
    @arduinomethod('n')
    def name(self, index):
        pass

    @memoized
    @returns(auto_convert)
    @arduinomethod('v')
    def value(self, index):
        pass


class DefineFeature(object):

    """Access to firmware constants.

    Examples:

        a=ArduinoTree()
        a.define.get('F_CPU') # AVR frequency
        a.define.get('__DATE__') # firmware upload date

    """

    def __init__(self, connection=None):
        self._arr = DefineArray(connection)

    @property
    @memoized
    def as_dict(self):
        """return all constants and their values in a dictionary."""
        d = dict()
        for i in range(self._arr.count):
            d[self._arr.name(i)] = self._arr.value(i)
        assert len(d)
        return d

    @property
    def names(self):
        return sorted(self.as_dict.keys())

    @property
    @memoized
    def count(self):
        return len(self.as_dict)

    def get(self, name):
        """get a constant.

        Examples:

            a=ArduinoTree()
            a.define.get('F_CPU') # AVR frequency

        """
        count = self._arr.count
        assert count
        for i in range(count):
            n = self._arr.name(i)
            if n == name:
                return self._arr.value(i)
        raise ValueError('% was not found!' % name)
