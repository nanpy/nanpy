#ifndef RAM_CLASS
#define RAM_CLASS

#include "BaseClass.h"
#include "MethodDescriptor.h"

namespace nanpy {
    class RAMClass : public BaseClass {

        public:
            void elaborate( nanpy::MethodDescriptor* m );
            const char* get_firmware_id();

    };
}

#endif
