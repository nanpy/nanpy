#ifndef ARDUINO_CLASS
#define ARDUINO_CLASS

#include "BaseClass.h"
#include "MethodDescriptor.h"

namespace nanpy {
    class ArduinoClass : public BaseClass {

        public:
            void elaborate( nanpy::MethodDescriptor* m );

    };
};

#endif
