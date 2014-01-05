from nanpy.arduinoboard import arduinomethod, returns, FirmwareClass
from nanpy.classinfo import check4firmware
from nanpy.memo import memoized


@check4firmware
class RegisterArray(FirmwareClass):
    firmware_id = 'R'

    @memoized
    @returns(int)
    @arduinomethod('c')
    def count(self):
        pass

    @returns(int)
    @arduinomethod('r')
    def read(self, index):
        pass

    @arduinomethod('w')
    def write(self, index, value):
        pass

    @memoized
    @returns(int)
    @arduinomethod('a')
    def address(self, index):
        pass

    @memoized
    @returns(int)
    @arduinomethod('s')
    def size(self, index):
        pass

    @memoized
    @arduinomethod('n')
    def name(self, index):
        pass


class Register(object):

    """Representation of an AVR register."""

    def __init__(self, index, arr):
        """"""
        self._arr = arr
        self.index = index

    def read_value(self):
        """Read register value.

        Examples:

            a=ArduinoTree()
            a.register.get('DDRB').read_value()

        """
        return self._arr.read(self.index)

    def write_value(self, value):
        """Write register value.

        Examples:

            a=ArduinoTree()
            a.register.get('DDRB').write_value(1)

        """
        return self._arr.write(self.index, value)

    value = property(read_value, write_value)

    @property
    def name(self):
        """Register name.
        """
        return self._arr.name(self.index)

    @property
    def address(self):
        """Register address.

        Examples:

            a=ArduinoTree()
            a.register.get('DDRB').address

        """
        return self._arr.address(self.index)

    @property
    def size(self):
        """Register size in bytes. 1 or 2.

        Examples:

            a=ArduinoTree()
            a.register.get('DDRB').size

        """
        return self._arr.size(self.index)


class RegisterProxy(object):

    """Proxy object to allow easy register access.

        Examples:

            a=ArduinoTree()
            a.register.proxy.DDRB = 1
            print( a.register.proxy.DDRB )

    """

    def __init__(self, arr, name_index_dict):
        self._name_index_dict = name_index_dict
        self._arr = arr

    def __getattr__(self, name):
        if name in ['_name_index_dict', '_arr']:
            return object.__getattribute__(self, name)

        index = self._name_index_dict[name]
        return self._arr.read(index)

    def __setattr__(self, name, value):
        if name in ['_name_index_dict', '_arr']:
            self.__dict__[name] = value
            return

        index = self._name_index_dict[name]
        return self._arr.write(index, value)


class RegisterFeature(object):

    def __init__(self, connection=None):
        self._arr = RegisterArray(connection)

    @property
    @memoized
    def name_index_dict(self):
        d = dict()
        for i in range(self._arr.count()):
            d[self._arr.name(i)] = i
        assert len(d)
        return d

    @property
    def names(self):
        """Get all register names as a sorted list."""
        return sorted(self.name_index_dict.keys())

    @property
    @memoized
    def count(self):
        """Get register count."""
        return len(self.name_index_dict.keys())

    @memoized
    def get(self, name):
        try:
            index = self.name_index_dict[name]
        except KeyError:
            raise ValueError('Unknown register: %s' % name)
        return Register(index, self._arr)

    @property
    @memoized
    def proxy(self):
        return RegisterProxy(self._arr, self.name_index_dict)
