Nanpy
=====

|Travis| |Latest Version| |Supported Python versions| |Downloads|

Use your Arduino board with Python. http://pypi.python.org/pypi/nanpy

Overview
--------

Nanpy is a library that use your Arduino as a slave, controlled by a master device where you run your scripts, such as a PC, a Raspberry Pi etc.

The main purpose of Nanpy is making programmers' life easier, providing them a powerful library to create prototypes faster and make Arduino programming a game for kids.

::

    from nanpy import ArduinoApi

    a = ArduinoApi()
    a.pinMode(13, a.OUTPUT)
    a.digitalWrite(13, a.HIGH)

I know, there are a lot of projects able to do that, but hey, Nanpy can do more!

Nanpy is easily extensible and can theoretically use every library,
allowing you to create how many objects you want. We support OneWire, Lcd, Stepper, Servo, DallasTemperature and many
more...
  
Let's try to connect our 16x2 lcd screen on pins 7, 8, 9, 10, 11, 12 and show your first "Hello world"!

::

    from nanpy import Lcd

    lcd = Lcd([7, 8, 9, 10, 11, 12], [16, 2])
    lcd.printString('Hello World!')

really straightforward now, isn't it? :)

Serial communication
~~~~~~~~~~~~~~~~~~~~

Nanpy autodetects the serial port for you, anyway you can manually
specify another serial port:

::

    from nanpy import SerialManager
    connection = SerialManager(device='/dev/ttyACM1')

and use it with your objects

::

    from nanpy import ArduinoApi
    a = ArduinoApi(connection=connection)
    a.pinMode(13, a.OUTPUT)
    a.digitalWrite(13, a.HIGH)

You can specify how many SerialManager objects you want and control more
than one Arduino board within the same script.

How to build and install
------------------------

First of all, you need to build the firmware and upload it on your
Arduino, to do that clone the `nanpy-firmware repository on
Github <https://github.com/nanpy/firmware>`__ or `download it from
PyPi <https://pypi.python.org/pypi/nanpy>`__.

::

    git clone https://github.com/nanpy/nanpy-firmware.git
    cd nanpy-firmware
    ./configure.sh

| You can now edit Nanpy/cfg.h generated file to configure your Nanpy
  firmware, selecting the features you want to include and the baud
  rate.
| To build and install Nanpy firmware, copy Nanpy directory under your
  "sketchbook" directory, start your Arduino IDE, open Sketchbook ->
  Nanpy and click on "Upload".

To install Nanpy Python library on your master device just type:

::

    pip install nanpy

How to contribute
-----------------

Nanpy still needs a lot of work. You can contribute with patches
(bugfixing, improvements, adding support for a new library not included
in Nanpy yet, writing examples and so on), writing documentation,
reporting bugs, creating packages or simply spreading Nanpy through the
web if you like it :) If you have any doubt or problem, please contact
me at stagi.andrea@gmail.com

Do you want to support us with a coffee? We need a lot of caffeine to
code all night long! if you like this project and you want to support
us, `please donate using
Paypal <https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=TDTPP5JHVJK8J>`__

Supported hardware
------------------

board:
 - ATmega boards (ATtiny has not enough RAM) 
 - ESP8266 (communication over serial or WiFi connection)

external hardware:
 - BMP180 Digital pressure sensor
 - AD9850 Direct Digital Synthesizer
 - TLC5947 LED Driver
 - DHT11, DHT22, DHT21, AM2301 humidity sensors
 - HD44780 LCD controller
 - PCF8574 8-Bit I/O Expander for I2C
 - X9C1xxx (xxx = 102,103,104,503) digital potentiometers

License
-------

This software is released under MIT License. Copyright (c) 2012-2016
Andrea Stagi stagi.andrea@gmail.com

.. |Travis| image:: http://img.shields.io/travis/nanpy/nanpy.svg
   :target: https://travis-ci.org/nanpy/nanpy/
.. |Latest Version| image:: https://img.shields.io/pypi/v/nanpy.svg
   :target: https://pypi.python.org/pypi/nanpy/
.. |Supported Python versions| image:: https://img.shields.io/badge/python-2.7%2C%203.3%2C%203.4%2C%203.5-blue.svg
   :target: https://pypi.python.org/pypi/nanpy/
.. |Downloads| image:: https://img.shields.io/pypi/dm/nanpy.svg
   :target: https://pypi.python.org/pypi/nanpy/
