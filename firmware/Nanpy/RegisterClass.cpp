#include "cfg.h"

#if USE_Register

#include <Arduino.h>
#include "RegisterClass.h"
#include <stdlib.h>

// http://www.nongnu.org/avr-libc/user-manual/pgmspace.html

#define MISSING(x)

// example:
// char string_OCR2A[] PROGMEM = "OCR2A";
#define DEFINE(x)    const char string_##x[] PROGMEM = #x;
#include "generated_avr_registers.h"
#undef DEFINE

const char * const name_table[] PROGMEM =
{
// example:
// string_OCR2A,
#define DEFINE(x)    string_##x,
#include "generated_avr_registers.h"
#undef DEFINE
};

#define DEFINE(x) (uint16_t)(&x),
const uint16_t reg_list[] PROGMEM =
{
#include "generated_avr_registers.h"
};
#undef DEFINE

#define DEFINE(x)    sizeof(x),
const uint16_t sizeof_list[] PROGMEM =
{
#include "generated_avr_registers.h"
};
#undef DEFINE

const int REG_COUNT = sizeof(sizeof_list) / sizeof(sizeof_list[0]);

#define LONGEST_REGISTER_NAME  21

const char* nanpy::RegisterClass::get_firmware_id()
{
    return "R";
}

void nanpy::RegisterClass::elaborate(nanpy::MethodDescriptor* m)
{
    if (strcmp(m->getName(), "c") == 0) // count
    {
        m->returns(REG_COUNT);
    }
    else if (strcmp(m->getName(), "n") == 0) // name
    {
        word regindex = m->getInt(0);
        char buffer[LONGEST_REGISTER_NAME];
        strcpy_P(buffer, (PGM_P) pgm_read_word(&(name_table[regindex])));
        m->returns(buffer);
    }
    else
    {
        word regindex = m->getInt(0);
        word regvalue = m->getInt(1);

        word regaddr = pgm_read_word(&reg_list[regindex]);
        byte regsize = pgm_read_byte(&sizeof_list[regindex]);

        volatile byte* preg8 = (volatile byte*) regaddr;
        volatile word* preg16 = (volatile word*) regaddr;

        if (strcmp(m->getName(), "r") == 0) // read
        {
            switch (regsize)
            {
            case 1:
                m->returns(*preg8);
                break;
            case 2:
                m->returns(*preg16);
                break;
            }
        }
        else if (strcmp(m->getName(), "w") == 0) // write
        {
            switch (regsize)
            {
            case 1:
                *preg8 = (byte) regvalue;
                break;
            case 2:
                *preg16 = regvalue;
                break;
            }
            m->returns(0);
        }
        else if (strcmp(m->getName(), "a") == 0) // address
        {
            m->returns(regaddr);
        }
        else if (strcmp(m->getName(), "s") == 0) // size
        {
            m->returns(regsize);
        }

    }
}

#endif

