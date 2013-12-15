#include <EEPROM.h>
#include "EEPROMClass.h"
#include <stdlib.h>

void nanpy::EEPROMClass::elaborate( nanpy::MethodDescriptor* m ) {
    if (strcmp(m->getClass(), "EEPROM") == 0) {
        if (strcmp(m->getName(), "write") == 0) {
            EEPROM.write(m->getInt(0), m->getInt(1));
            m->returns(0);
        }

        if (strcmp(m->getName(), "read") == 0) {
            m->returns(EEPROM.read(m->getInt(0)));
        }
    }
};
