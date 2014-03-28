import logging
log = logging.getLogger(__name__)


class I2C_CommunicationError(Exception):
    error_texts = {
        # 0: 'success',
        1: 'data too long to fit in transmit buffer',
        2: 'received NACK on transmit of address',
        3: 'received NACK on transmit of data',
        4: 'other error',
    }

    def __init__(self, error_code):
        self.error_code = error_code
        Exception.__init__(self, self.error_texts[error_code])


class I2C_Base(object):

    ''
    bus_initialised = False
    address = None

    def _begin(self):
        if not self.bus_initialised:
            self.wire.begin(self.address)
            self.bus_initialised = True


class I2C_Master(I2C_Base):

    """High level interface for I2C Master."""

    def __init__(self, wire):
        self.wire = wire

    def request(self, address, quantity):
        """Used by the master to request bytes from a slave device.

        :param address: the 7-bit address of the device to request bytes from
        :param quantity: the number of bytes to request
        :param stop: boolean. true will send a stop message after the request, releasing the bus. false will continually send a restart after the request, keeping the connection active.
        :returns: byte : the number of bytes returned from the slave device

        http://arduino.cc/en/Reference/WireRequestFrom

        """
        self._begin()
        n = self.wire.requestFrom(address, quantity, stop=True)
        if n < quantity:
            log.info('slave sent less bytes than requested')
        ls = n * [None]
        for i in range(n):
            ls[i] = self.wire.read()
        return ls

    def send(self, address, data):
        """"""
        self._begin()
        self.wire.beginTransmission(address)
        for b in data:
            self.wire.write(b)
        error_code = self.wire.endTransmission()
        if error_code != 0:
            raise I2C_CommunicationError(error_code)

    def scan(self):
        """The i2c_scanner uses the return value of the Write.endTransmisstion
        to see if a device did acknowledge to the address.

        original source: http://playground.arduino.cc/Main/I2cScanner#.Uxs4Wdt4iJM

        """
        self._begin()
        ls = []
        for address in range(128):
            try:
                self.send(address, [])
                ls.append(address)
            except I2C_CommunicationError:
                pass

        return ls


class I2C_Slave(I2C_Base):

    """High level interface for I2C Slave."""

    def __init__(self, wire, address):
        '''
        :param address: slave address
        '''
        self.wire = wire
        self.address = address

    def receive(self):
        self._begin()
        n = self.wire.available()
        ls = n * [None]
        for i in range(n):
            ls[i] = self.wire.read()
        return ls

    def send(self, data):
        """"""
        self._begin()
        for b in data:
            self.wire.write(b)
