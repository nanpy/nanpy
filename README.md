Nanpy
=====

Program your Arduino prototypes using Python.

Description
-----------

Use Python for developing prototypes for your Arduino board!

	lcd = Lcd([7, 8, 9, 10, 11, 12], [16, 2])
	lcd.printString("Loc. London")

really straightforward now, isn't it? :)

How to use
----------

Nanpy is composed by a Python part, that provide a set of client classes and functions to use Arduino via Python and a server firmware that you can build just typing

	./buildfirware

for your Arduino UNO (we are developing Nanpy on it, open the script and change the board if you need).

License
-------

This software is released under MIT License. Copyright (c) 2012 Octan (https://github.com/Octan)
