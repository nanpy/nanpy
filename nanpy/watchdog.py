from nanpy.arduinoboard import arduinomethod, FirmwareClass
from nanpy.classinfo import check4firmware


@check4firmware
class Watchdog(FirmwareClass):

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

    @arduinomethod
    def reset(self):
        """Reset the watchdog timer. (wdt_reset)

        When the watchdog timer is enabled,
        a call to this instruction is required before the timer expires,
        otherwise a watchdog-initiated device reset will occur.

        """

    @arduinomethod
    def enable(self, timeout):
        """Enable the watchdog timer, configuring it for expiry after
        timeout. (wdt_enable)"""

    @arduinomethod
    def disable(self):
        """Disable the watchdog timer, if possible. (wdt_disable)"""
