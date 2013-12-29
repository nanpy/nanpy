#ifndef LIQUID_CRYSTAL_CLASS
#define LIQUID_CRYSTAL_CLASS

#include "BaseClass.h"
#include "MethodDescriptor.h"

class LiquidCrystal;

namespace nanpy {
    class LiquidCrystalClass : public ObjectsManager<LiquidCrystal> {

        public:
            void elaborate( nanpy::MethodDescriptor* m );
            const char* get_firmware_id();

    };
}


#endif
