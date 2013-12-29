#ifndef DALLAS_TEMP_CLASS
#define DALLAS_TEMP_CLASS

#include "BaseClass.h"
#include "MethodDescriptor.h"

class DallasTemperature;

namespace nanpy {
    class DallasTemperatureClass: public ObjectsManager<DallasTemperature> {

        public:
            void elaborate( nanpy::MethodDescriptor* m );
            const char* get_firmware_id();

    };
}

#endif
