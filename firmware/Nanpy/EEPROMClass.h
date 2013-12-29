#ifndef EEPROM_CLASS
#define EEPROM_CLASS

#include "BaseClass.h"
#include "MethodDescriptor.h"

namespace nanpy {
    class EEPROMClass : public BaseClass {

        public:
            void elaborate( nanpy::MethodDescriptor* m );
            const char* get_firmware_id();

    };
}

#endif
