from nanpy.arduinotree import ArduinoTree
from nanpy.serialmanager import SerialManager
from nanpy.PCF8574 import PCF8574


I2C_ADDRESS = 0x27


def main():
    print ('PCF8574 demo')
    print ('address: 0x%X' % I2C_ADDRESS)
    connection = SerialManager(sleep_after_connect=2)
    connection.open()
    a = ArduinoTree(connection=connection)
    pcf = PCF8574(a.wire, I2C_ADDRESS)

    def write(d):
        print ('write: %s' % bin(d))
        pcf.write8(d)

    def read():
        d = pcf.read8()
        print ('read:  %s' % bin(d))

    read()

    d = pcf.readPin(0)
    print ('read  pin 0: %s' % d)
    print ('write pin 0: %s' % 1)
    pcf.writePin(0, 1)
    d = pcf.readPin(0)
    print ('read  pin 0: %s' % d)

    read()

    write(0b11111111)
    read()

    write(0b10101010)
    read()

    write(0b01010101)
    read()

    write(0b00000000)
    read()


if __name__ == '__main__':
    main()
