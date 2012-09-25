#ifndef ONE_WIRE_CLASS
#define ONE_WIRE_CLASS

#include "SlimArray.h"
#include "ArduinoClass.h"

class OneWire;
class MethodDescriptor;

char* readStringFromSerial();

class OneWireClass: public ArduinoClass {

    private:

        SlimArray <OneWire*> v;

    public:

        OneWireClass();
        void elaborate( MethodDescriptor* m );

};

#endif
