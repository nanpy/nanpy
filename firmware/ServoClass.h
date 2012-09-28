#ifndef SERVO_CLASS
#define SERVO_CLASS

#include <stdlib.h>
#include "SlimArray.h"
#include "ArduinoClass.h"

class Servo;
class MethodDescriptor;

char* readStringFromSerial();

class ServoClass: public ArduinoClass {

    private:

        SlimArray <Servo*> v;

    public:

        ServoClass();
        void elaborate( MethodDescriptor* m );

};

#endif
