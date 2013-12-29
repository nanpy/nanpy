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
