#ifndef ARDUINO_CLASS
#define ARDUINO_CLASS

#include "BaseClass.h"

class MethodDescriptor;

class ArduinoClass : public BaseClass {

    public:
        void elaborate( MethodDescriptor* m );

};

#endif
