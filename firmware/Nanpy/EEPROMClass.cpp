#include "cfg.h"

#if USE_EEPROM

#include <EEPROM.h>
#include "EEPROMClass.h"
#include <stdlib.h>

const char* nanpy::EEPROMClass::get_firmware_id()
{
    return "EEPROM";
}

void nanpy::EEPROMClass::elaborate( nanpy::MethodDescriptor* m ) {
        if (strcmp(m->getName(), "write") == 0) {
            EEPROM.write(m->getInt(0), m->getInt(1));
            m->returns(0);
        }
        if (strcmp(m->getName(), "read") == 0) {
            m->returns(EEPROM.read(m->getInt(0)));
        }

        if (strcmp(m->getName(), "size") == 0) {
            m->returns(E2END+1);
        }
};

#endif
