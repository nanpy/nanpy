#ifndef EEPROM_CLASS
#define EEPROM_CLASS

#include "BaseClass.h"

class MethodDescriptor;

namespace nanpy {
    class EEPROMClass : public BaseClass {

        public:
            void elaborate( MethodDescriptor* m );

    };
}

#endif
