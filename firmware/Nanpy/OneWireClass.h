#ifndef ONE_WIRE_CLASS
#define ONE_WIRE_CLASS

#include "BaseClass.h"
#include "MethodDescriptor.h"

class OneWire;

namespace nanpy {
    class OneWireClass: public ObjectsManager<OneWire> {

        public:
            void elaborate( nanpy::MethodDescriptor* m );

    };
}

#endif
