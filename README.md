Nanpy
=====

Program your Arduino prototypes using Python, also using a Raspberry!!

Description
-----------

Use Python for developing prototypes for your Arduino board!
Let's start with a classic example, turn on a led placed in the 13th pin..

	Arduino.pinMode(13, Arduino.OUTPUT)
	Arduino.digitalWrite(13, Arduino.HIGH)

There are a lot of projects able to do that. Nanpy can do more! 
Nanpy is easily extensible and can theoretically use every library, allowing you to create how many objects you want.
We started supporting OneWire, Lcd and Servo library and they're still incomplete.
Let's try to connect our 16x2 lcd screen on pins 7, 8, 9, 10, 11, 12 and print something!

	lcd = Lcd([7, 8, 9, 10, 11, 12], [16, 2])
	lcd.printString("Hello World!")

really straightforward now, isn't it? :)

How to build and install
------------------------

Nanpy is composed by a Python part, that provides a library to use Arduino via Python and a server firmware.

To install Nanpy just type (as root):

	python setup.py install

To build the firmware type:

	cd firmware
	export BOARD=uno (in case you use UNO board. Type 'make boards' for a complete list)
	make

and then upload it on your board:

	make upload

How to use
----------

### Serial communication

Nanpy autodetects the serial port for you, anyway you can specify another serial port and baudrate manually:

	from nanpy import serial_manager
	serial_manager.connect('/dev/ttyACM1', 9600)

### Import modules

Import all the modules you need :)

	from nanpy import Arduino
	from nanpy import (OneWire, Lcd)
	...

License
-------

This software is released under MIT License. Copyright (c) 2012 Andrea Stagi <stagi.andrea@gmail.com>
