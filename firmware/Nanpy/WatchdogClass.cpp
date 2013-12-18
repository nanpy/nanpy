#include <Arduino.h>
#include "WatchdogClass.h"
#include <stdlib.h>
#include <avr/wdt.h>

void nanpy::WatchdogClass::elaborate(nanpy::MethodDescriptor* m)
{
    if (strcmp(m->getClass(), "Watchdog") == 0)
    {
        if (strcmp(m->getName(), "wdt_reset") == 0)
        {
            wdt_reset();
            m->returns(0);
        }
        if (strcmp(m->getName(), "wdt_enable") == 0)
        {
            wdt_enable(m->getInt(0));
            m->returns(0);
        }
        if (strcmp(m->getName(), "wdt_disable") == 0)
        {
            wdt_disable();
            m->returns(0);
        }
    }
}
;
