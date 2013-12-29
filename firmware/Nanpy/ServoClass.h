#ifndef SERVO_CLASS
#define SERVO_CLASS

#include "BaseClass.h"
#include "MethodDescriptor.h"

class Servo;

namespace nanpy {
    class ServoClass: public ObjectsManager<Servo> {

        public:
            void elaborate( nanpy::MethodDescriptor* m );
            const char* get_firmware_id();

    };
}

#endif
