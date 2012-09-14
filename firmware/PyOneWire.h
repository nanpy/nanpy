
#ifndef PY_ONE_WIRE
#define PY_ONE_WIRE
#include "Vector.h"

class OneWire;
class MethodDescriptor;

char* readStringFromSerial();

struct onewire
{
    char* name;
    OneWire* obj;
};



class PyOneWire {

    public:

        PyOneWire();

        void elaborate( MethodDescriptor* m );

        //void getObjectByName()
        //...

};

#endif
