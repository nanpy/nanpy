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

Multithreading
--------------
What happens if you call methods in an async context? Nothing bad, all works! every call is mutually exclusive.. For example, suppose that two threads need to write on the same Lcd and in different positions at the same time... well, just call printString on the Lcd object specifying the position (row and column)

	#Thread_1
	...
	lcd.printString("Hello First Row!", 0, 0)
	...
	
	#Thread_2
	....
	lcd.printString("Hello Second Row!", 0, 1)
	...

How to build and install
------------------------
You need to build the firmware for your Arduino first, copy firmware/Nanpy directory under your "sketchbook" directory, start Arduino program, open Sketchbook/Nanpy, select "Upload".

To install Nanpy Python library just type (as root):

	python setup.py install

How to use
----------
### Serial communication

Nanpy autodetects the serial port for you, anyway you can specify another serial port manually:

	from nanpy import serial_manager
	serial_manager.connect('/dev/ttyACM1')

### Import modules

Import all the modules you need :)

	from nanpy import Arduino
	from nanpy import (OneWire, Lcd)
	...

How to contribute
-----------------
Nanpy needs a lot of work to be a great instrument. You can contribute with patches (bugfixing, writing improvements, creating support for a new library not included in Nanpy yet, writing examples and so on), writing documentation, reporting bugs, creating packages or simply spreading Nanpy through the web if you like it :) If you have any doubt or problem, please contact me at <stagi.andrea@gmail.com>

Donate
------
Do you want to support us with a coffee? We need it to code all night long! if you like this project and you want to support it with some cents, please donate :) https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=TDTPP5JHVJK8J

License
-------
This software is released under MIT License. Copyright (c) 2012-2013 Andrea Stagi <stagi.andrea@gmail.com>
