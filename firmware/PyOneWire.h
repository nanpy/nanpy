#ifndef PY_ONE_WIRE
#define PY_ONE_WIRE

#include "SlimArray.h"
#include "ArduinoClass.h"

class OneWire;
class MethodDescriptor;

char* readStringFromSerial();

struct onewire
{
    char* name;
    OneWire* obj;
};



class PyOneWire: public ArduinoClass {

    public:

        PyOneWire();
        void elaborate( MethodDescriptor* m );

};

#endif
