#ifndef STEPPER_CLASS
#define STEPPER_CLASS

#include <stdlib.h>
#include "SlimArray.h"
#include "ArduinoClass.h"

class Stepper;
class MethodDescriptor;

char* readStringFromSerial();

class StepperClass: public ArduinoClass {

    private:

        SlimArray <Stepper*> v;

    public:

        StepperClass();
        void elaborate( MethodDescriptor* m );

};

#endif
