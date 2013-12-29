#ifndef DHT_CLASS
#define DHT_CLASS

#include "BaseClass.h"
#include "MethodDescriptor.h"

class DHT;

namespace nanpy {
    class DHTClass: public ObjectsManager<DHT> {

        public:
            void elaborate( nanpy::MethodDescriptor* m );
            const char* get_firmware_id();

    };
}

#endif
