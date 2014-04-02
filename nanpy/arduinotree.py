from __future__ import division
from nanpy.arduinoapi import ArduinoApi
from nanpy.arduinocore import ArduinoCore
from nanpy.arduinopin import PinFeature
from nanpy.classinfo import ClassInfo
from nanpy.counter import Counter
from nanpy.define import DefineFeature
from nanpy.eepromobj import EepromLib
from nanpy.fwinfo import firmware_info
from nanpy.memo import memoized
from nanpy.ram import RAM
from nanpy.register import RegisterFeature
from nanpy.serialmanager import SerialManager, serial_manager
from nanpy.vcc import Vcc
from nanpy.watchdog import Watchdog
from nanpy.wire import Wire
import time


class ArduinoTree(object):

    """Object tree model of an Arduino.

    Examples:

        a=ArduinoTree()
        a.pin.get(9).read_digital_value()

    """

    def __init__(self, connection=None):
        ''
        self.connection = connection
        if not connection:
            self.connection = serial_manager
        if not hasattr(self.connection, 'classinfo'):
            self.connection.classinfo = ClassInfo(self.connection)

    @property
    @memoized
    def api(self):
        """Access to Arduino API."""
        return ArduinoApi(self.connection)

    @property
    @memoized
    def pin(self):
        """Object-oriented representation of an Arduino pin"""
        return PinFeature(self.define, self.register, self.core, self.ram, self.api)

    @property
    @memoized
    def define(self):
        """Access to firmware constants."""
        return DefineFeature(self.connection)

    @property
    @memoized
    def register(self):
        """Direct access to AVR registers."""
        return RegisterFeature(self.connection)

    @property
    @memoized
    def watchdog(self):
        """Direct access to watchdog timer."""
        return Watchdog(self.connection)

    @property
    @memoized
    def eeprom(self):
        """Access to EEPROM."""
        return EepromLib(self.connection)

    @property
    @memoized
    def ram(self):
        """Access to RAM."""
        return RAM(self.connection)

    @property
    @memoized
    def counter(self):
        """Access to counter."""
        return Counter(self.connection, F_CPU=self.define.get('F_CPU'))

    @property
    @memoized
    def core(self):
        """Access to Arduino functions which are not part of the public API."""
        return ArduinoCore(self.connection)

    @property
    @memoized
    def vcc(self):
        """Access to VCC."""
        return Vcc(self.register)

    def soft_reset(self):
        """Resets the AVR, the registers will be reset to their known, default
        settings.

        Details: http://www.nongnu.org/avr-libc/user-manual/FAQ.html#faq_softreset

        """
        self.watchdog.enable(self.watchdog.WDTO_60MS)
        time.sleep(0.2)

        # TODO: after restart the first read is not correct (why?)
        # This command helps cleaning the read buffer
        self.connection.flush_input()

    @property
    @memoized
    def wire(self):
        """Access to Wire."""
        return Wire(self.connection)

    @property
    @memoized
    def firmware_info(self):
        """"""
        return firmware_info(self.define.as_dict)
