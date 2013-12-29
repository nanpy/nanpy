#ifndef STEPPER_CLASS
#define STEPPER_CLASS

#include "BaseClass.h"
#include "MethodDescriptor.h"

class Stepper;

namespace nanpy {
    class StepperClass: public ObjectsManager<Stepper> {

        public:
            void elaborate( nanpy::MethodDescriptor* m );
            const char* get_firmware_id();

    };
}

#endif
