from nanpy.arduinoboard import arduinoclassmethod
import time


class Watchdog(object):

    """Direct access to watchdog timer.

    Details: http://www.nongnu.org/avr-libc/user-manual/group__avr__watchdog.html

    """
    WDTO_15MS = 0
    WDTO_30MS = 1
    WDTO_60MS = 2
    WDTO_120MS = 3
    WDTO_250MS = 4
    WDTO_500MS = 5
    WDTO_1S = 6
    WDTO_2S = 7
    WDTO_4S = 8
    WDTO_8S = 9

    @classmethod
    @arduinoclassmethod
    def wdt_reset(cls):
        """Reset the watchdog timer.

        When the watchdog timer is enabled,
        a call to this instruction is required before the timer expires,
        otherwise a watchdog-initiated device reset will occur.

        """

    @classmethod
    @arduinoclassmethod
    def wdt_enable(cls, timeout):
        """Enable the watchdog timer, configuring it for expiry after
        timeout."""

    @classmethod
    @arduinoclassmethod
    def wdt_disable(cls):
        """Disable the watchdog timer, if possible."""

    @classmethod
    def soft_reset(cls):
        """Resets the AVR, the registers will be reset to their known, default
        settings.

        Details: http://www.nongnu.org/avr-libc/user-manual/FAQ.html#faq_softreset

        """
        cls.wdt_enable(cls.WDTO_15MS)
        time.sleep(0.1)
