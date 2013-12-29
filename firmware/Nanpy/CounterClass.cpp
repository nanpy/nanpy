#include "cfg.h"

#if USE_Counter

#include "CounterClass.h"
#include "FreqCount.h"

const char* nanpy::CounterClass::get_firmware_id()
{
    return "Counter";
}

void nanpy::CounterClass::elaborate(nanpy::MethodDescriptor* m)
{
    if (strcmp(m->getName(), "begin") == 0)
    {
        FreqCount.begin(m->getInt(0));
        m->returns(0);
    }
    if (strcmp(m->getName(), "available") == 0)
    {
        m->returns(FreqCount.available());
    }
    if (strcmp(m->getName(), "read") == 0)
    {
        m->returns(FreqCount.read());
    }
    if (strcmp(m->getName(), "end") == 0)
    {
        FreqCount.end();
        m->returns(0);
    }
}

#endif
