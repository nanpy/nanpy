"""power read demo."""

from nanpy.arduinotree import ArduinoTree
from nanpy.serialmanager import SerialManager


def power_demo():
    connection = SerialManager()
    a = ArduinoTree(connection=connection)
    Vcc = a.vcc.read()
    msg = 'Power supply= %0.2f V' % Vcc
    print(msg)

if __name__ == '__main__':
    power_demo()
