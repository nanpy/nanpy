#
# DigiPot.pde - Example sketch for Arduino library for managing digital potentiometers X9C1xxx (xxx = 102,103,104,503).
# By Timo Fager, Jul 29, 2011.
# Released to public domain.
#
# For this example, connect your X9C103P (or the like) as follows:
# 1 - INC - Arduino pin 2
# 2 - U/D - Arduino pin 3
# 3 - VH  - 5V
# 4 - VSS - GND
# 5 - VW  - Output: A0 and 150 Ohm resistor -> LED -> GND
# 6 - VL  - GND
# 7 - CS  - Arduino pin 4
# 8 - VCC - 5V
#

from nanpy import SerialManager
from nanpy.arduinotree import ArduinoTree
from time import sleep

from nanpy.DigiPotX9Cxxx import DigiPot


connection = SerialManager()
a = ArduinoTree(connection=connection)
incPin = a.pin.get(2)
udPin = a.pin.get(3)
csPin = a.pin.get(4)

anPin = a.pin.get('A0')

pot = DigiPot(incPin, udPin, csPin)

for i in range(100) + list(reversed(range(100))):
    pot.set(i)
    an = anPin.read_analog_value()
    print('set pot to %s, read analog: %s' % (i, an))
    sleep(0.1)


