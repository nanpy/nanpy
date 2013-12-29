#ifndef CAPACITIVE_SENSOR_CLASS
#define CAPACITIVE_SENSOR_CLASS

#include "BaseClass.h"
#include "MethodDescriptor.h"

class CapacitiveSensor;

namespace nanpy {
    class CapacitiveSensorClass : public ObjectsManager<CapacitiveSensor> {

        public:
            void elaborate( nanpy::MethodDescriptor* m );
            const char* get_firmware_id();

    };
}

#endif
