Nanpy
=====

Use your Arduino board with Python.

Description
-----------

The main purpose of Nanpy is making programmers' life easier, giving them something to create prototypes faster and use Arduino in a simpler way, thanks to a simple and powerful language like Python. Also Nanpy can run on RaspberryPi (tested with Raspbian http://www.raspbian.org/) so you can use it for communicating with Arduino :)

Let's start with a classic example, turn on a led placed in the 13th pin..

	Arduino.pinMode(13, Arduino.OUTPUT)
	Arduino.digitalWrite(13, Arduino.HIGH)

There are a lot of projects able to do that. Nanpy can do more! 
Nanpy is easily extensible and can theoretically use every library, allowing you to create how many objects you want.
We started supporting OneWire, Lcd, Stepper and Servo library and they're still incomplete.
Let's try to connect our 16x2 lcd screen on pins 7, 8, 9, 10, 11, 12 and print something!

	lcd = Lcd([7, 8, 9, 10, 11, 12], [16, 2])
	lcd.printString("Hello World!")

really straightforward now, isn't it? :)

Dependencies
------------

#### Python (2.2 or later)
- python-setuptools
- python-serial

How to build and install
------------------------

Nanpy is composed by a Python part, that provides a library to use Arduino via Python and a server firmware. You can install Nanpy on a Raspberry too :)

To install Nanpy just type (as root, requires python-setuptools):

	python setup.py install

To build the firmware type:

	cd firmware
	export BOARD=uno (in case you use UNO board. Type 'make boards' for a complete list)
	make

and then upload it on your board:

	make upload

Optionally you can also set the baud rate:

	export BAUDRATE=115200 (default value is 9600)

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

How to contribute
-----------------

Nanpy needs a lot of work to be a great instrument. You can contribute with patches (bugfixing, writing improvements, creating support for a new library not included in Nanpy yet, writing examples and so on), writing documentation, reporting bugs or simply spreading Nanpy through the web if you like it :) If you have any doubt or problem, please contact me at <stagi.andrea@gmail.com>

License
-------

This software is released under MIT License. Copyright (c) 2012 Andrea Stagi <stagi.andrea@gmail.com>
