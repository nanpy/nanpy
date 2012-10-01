#ifndef ONE_WIRE_CLASS
#define ONE_WIRE_CLASS

#include "BaseClass.h"

class OneWire;
class MethodDescriptor;

class OneWireClass: public ObjectsManager<OneWire> {

    public:
        void elaborate( MethodDescriptor* m );

};

#endif
