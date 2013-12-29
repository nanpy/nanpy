#pragma once

#include "BaseClass.h"
#include "MethodDescriptor.h"

namespace nanpy {
    class ArduinoCoreClass : public BaseClass {

        public:
            void elaborate( nanpy::MethodDescriptor* m );
            const char* get_firmware_id();

    };
};

