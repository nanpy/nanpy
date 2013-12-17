from nanpy.arduinoboard import arduinoclassmethod
import time


class Watchdog(object):
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
        pass

    @classmethod
    @arduinoclassmethod
    def wdt_enable(cls, value):
        pass

    @classmethod
    @arduinoclassmethod
    def wdt_disable(cls):
        pass

    @classmethod
    def soft_reset(cls):
        '''http://www.nongnu.org/avr-libc/user-manual/FAQ.html#faq_softreset'''
        cls.wdt_enable(cls.WDTO_15MS)
        time.sleep(0.1)
