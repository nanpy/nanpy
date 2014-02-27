#include "cfg.h"

#if USE_RAM

#include "RAMClass.h"
#include <stdlib.h>
#include "freeram.h"


const char* nanpy::RAMClass::get_firmware_id()
{
    return "RAM";
}

void nanpy::RAMClass::elaborate( nanpy::MethodDescriptor* m ) {
        if (strcmp(m->getName(), "write") == 0) {
            uint8_t* p = (uint8_t*)(m->getInt(0));
            *p = m->getInt(1);
            m->returns(0);
        }
        if (strcmp(m->getName(), "read") == 0) {
            uint8_t* p = (uint8_t*)(m->getInt(0));
            m->returns(*p);
        }

        if (strcmp(m->getName(), "size") == 0) {
            m->returns(RAMEND+1);
        }

        if (strcmp(m->getName(), "free") == 0) {
            m->returns(free_ram2());
        }
};

#endif
