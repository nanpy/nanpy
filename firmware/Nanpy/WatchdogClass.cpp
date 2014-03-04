#include "cfg.h"

#if USE_Watchdog

#include <Arduino.h>
#include "WatchdogClass.h"
#include <stdlib.h>
#include <avr/wdt.h>

const char* nanpy::WatchdogClass::get_firmware_id()
{
    return "Watchdog";
}

void nanpy::WatchdogClass::elaborate(nanpy::MethodDescriptor* m)
{
    if (strcmp(m->getName(), "reset") == 0)
    {
        wdt_reset();
        m->returns(0);
    }
    if (strcmp(m->getName(), "enable") == 0)
    {
        wdt_enable(m->getInt(0));
        m->returns(0);
    }
    if (strcmp(m->getName(), "disable") == 0)
    {
        wdt_disable();
        m->returns(0);
    }
}

#endif

void disable_watchdog_at_startup()
{
    // disable watchdog at startup
    // http://www.nongnu.org/avr-libc/user-manual/group__avr__watchdog.html
    // "the watchdog timer remains active even after a system reset (except a power-on condition),
    // using the fastest prescaler value (approximately 15 ms).
    // It is therefore required to turn off the watchdog early during program startup,.."
    // "..clearing the watchdog reset flag before disabling the watchdog is required, according to the datasheet."
#ifdef MCUSR
    MCUSR = 0;
    wdt_disable();
#endif
}
