from nanpy.arduinoboard import arduinomethod, returns, FirmwareClass
from nanpy.classinfo import check4firmware


@check4firmware
class Wire(FirmwareClass):

    """access to Wire library
    http://arduino.cc/en/reference/wire
    """
    firmware_id = 'Wire'

    @arduinomethod
    def begin(self, address=None):
        """Initiate the Wire library and join the I2C bus as a master or slave.
        This should normally be called only once.

        :param address: the 7-bit slave address (optional); if not specified,
            join the bus as a master.
        :returns: None

        http://arduino.cc/en/Reference/WireBegin

        """

    @returns(int)
    @arduinomethod
    def requestFrom(self, address, quantity, stop=True):
        """Used by the master to request bytes from a slave device. The bytes
        may then be retrieved with the available() and read() functions.

        :param address: the 7-bit address of the device to request bytes from
        :param quantity: the number of bytes to request
        :param stop: boolean. true will send a stop message after the request,
            releasing the bus. false will continually send a restart after the request,
            keeping the connection active.
        :returns: byte : the number of bytes returned from the slave device

        http://arduino.cc/en/Reference/WireRequestFrom

        """

    @arduinomethod
    def beginTransmission(self, address):
        """Begin a transmission to the I2C slave device with the given address.
        Subsequently, queue bytes for transmission with the write() function
        and transmit them by calling endTransmission().

        :param address: the 7-bit address of the device to transmit to
        :returns: None

        http://arduino.cc/en/Reference/WireBeginTransmission

        """

    @returns(int)
    @arduinomethod
    def endTransmission(self, stop=True):
        """Ends a transmission to a slave device that was begun by
        beginTransmission() and transmits the bytes that were queued by
        write().

        :param stop: boolean. true will send a stop message,
            releasing the bus after transmission. false will send a restart,
            keeping the connection active.
        :returns: byte, which indicates the status of the transmission:
            0:success
            1:data too long to fit in transmit buffer
            2:received NACK on transmit of address
            3:received NACK on transmit of data
            4:other error

        http://arduino.cc/en/Reference/WireEndTransmission

        """

    @returns(int)
    @arduinomethod
    def write(self, value):
        """Writes data from a slave device in response to a request from a
        master, or queues bytes for transmission from a master to slave device.

        (in-between calls to beginTransmission() and endTransmission()).

        :param value: a value to send as a single byte
        :returns: byte: write() will return the number of bytes written

        http://arduino.cc/en/Reference/WireWrite

        """

    @returns(int)
    @arduinomethod
    def available(self, pin, value):
        """Returns the number of bytes available for retrieval with read().
        This should be called on a master device after a call to requestFrom()
        or on a slave inside the onReceive() handler.

        :returns: The number of bytes available for reading.

        http://arduino.cc/en/Reference/WireAvailable

        """

    @returns(int)
    @arduinomethod
    def read(self, pin, value):
        """Reads a byte that was transmitted from a slave device to a master
        after a call to requestFrom() or was transmitted from a master to a
        slave.

        :returns: The next byte received

        http://arduino.cc/en/Reference/WireRead

        """
