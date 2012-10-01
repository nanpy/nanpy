#ifndef SERVO_CLASS
#define SERVO_CLASS

#include "BaseClass.h"

class Servo;
class MethodDescriptor;

class ServoClass: public ObjectsManager<Servo> {

    public:
        void elaborate( MethodDescriptor* m );

};

#endif
