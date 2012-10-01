#ifndef STEPPER_CLASS
#define STEPPER_CLASS

#include "BaseClass.h"

class Stepper;
class MethodDescriptor;

class StepperClass: public ObjectsManager<Stepper> {

    public:
        void elaborate( MethodDescriptor* m );

};

#endif
