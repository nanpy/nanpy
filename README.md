Nanpy
=====

Program your Arduino prototypes using Python.

Description
-----------

Use Python for developing prototypes for your Arduino board!
Let's start with a classic example, turn on a led place in 13th pin..

	Arduino.pinMode(13, 1)
	Arduino.digitalWrite(13, 1)

There are a lot of projects able to do that. Nanpy can do more! 
Nanpy is easily extensible and can theoretically use every library, allowing you to create how many objects you want.
We started supporting OneWire, Lcd and Servo library and they're still incomplete.
Let's try to connect our 16x2 lcd screen on pins 7, 8, 9, 10, 11, 12 and print something!

	lcd = Lcd([7, 8, 9, 10, 11, 12], [16, 2])
	lcd.printString("Hello World!")

really straightforward now, isn't it? :)

How to use
----------

Nanpy is composed by a Python part, that provide a set of client classes and functions to use Arduino via Python 
and a server firmware that you can build just typing

	./buildfirware

for your Arduino UNO (we are developing Nanpy on it, open the script and change the board if you need).

License
-------

This software is released under MIT License. Copyright (c) 2012 Andrea Stagi <stagi.andrea@gmail.com>
