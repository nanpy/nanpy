#include "cfg.h"

#if USE_Define

#include <Arduino.h>
#include "DefineClass.h"
#include <stdlib.h>
#include "generated_mcu.h"

// http://www.nongnu.org/avr-libc/user-manual/pgmspace.html

// example:
// char string_A0[] PROGMEM = "A0";
#define DEFINE(x)    const char string_##x[] PROGMEM = #x;
#include "intdefs.h"
#undef DEFINE

const char * const name_table[] PROGMEM =
{
// example:
// string_A0,
#define DEFINE(x)    string_##x,
#include "intdefs.h"
#undef DEFINE
};

const int32_t value_table[] PROGMEM =
{
// example:
// A0,
#define DEFINE(x)    x,
#include "intdefs.h"
#undef DEFINE
};

#define LONGEST_STRING_IN_INTDEFS_H  21

#define COUNT_INT_DEFS  sizeof(name_table)/sizeof(name_table[0])

#define COUNT_STR_DEFS  4
// __TIME__, __DATE__, __VERSION__, MCU

const char* nanpy::DefineClass::get_firmware_id()
{
    return "D";
}

void nanpy::DefineClass::elaborate(nanpy::MethodDescriptor* m)
{
    if (strcmp(m->getName(), "c") == 0) // count
    {
        m->returns(COUNT_INT_DEFS + COUNT_STR_DEFS);
    }
    if (strcmp(m->getName(), "n") == 0) // name
    {
        int index = m->getInt(0);
        switch (index)
        {
        case COUNT_INT_DEFS + 0:
            m->returns("__TIME__");
            break;
        case COUNT_INT_DEFS + 1:
            m->returns("__DATE__");
            break;
        case COUNT_INT_DEFS + 2:
            m->returns("__VERSION__");
            break;
        case COUNT_INT_DEFS + 3:
            m->returns("MCU");
            break;

        default:
//            index -= COUNT_STR_DEFS;
            char buffer[LONGEST_STRING_IN_INTDEFS_H];
            strcpy_P(buffer, (PGM_P) pgm_read_word(&(name_table[index])));
            m->returns(buffer);
        }
    }
    if (strcmp(m->getName(), "v") == 0) // value
    {
        int index = m->getInt(0);
        switch (index)
        {
        case COUNT_INT_DEFS + 0:
            m->returns(__TIME__);
            break;
        case COUNT_INT_DEFS + 1:
            m->returns(__DATE__);
            break;
        case COUNT_INT_DEFS + 2:
            m->returns(__VERSION__);
            break;
        case COUNT_INT_DEFS + 3:
            m->returns(MCU);
            break;

        default:
//            index -= COUNT_STR_DEFS;
            int32_t value = pgm_read_dword(&(value_table[index]));
            m->returns(value);
        }
    }

}

#endif
