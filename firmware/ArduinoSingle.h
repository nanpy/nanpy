#ifndef ARDUINO_SINGLE
#define ARDUINO_SINGLE

#include <stdlib.h>
#include "ArduinoClass.h"

class MethodDescriptor;

char* readStringFromSerial();

class ArduinoSingle : public ArduinoClass {

    private:

        static ArduinoSingle* instance;
        ArduinoSingle();

    public:

        void elaborate( MethodDescriptor* m );
        static ArduinoSingle* getInstance();

};

#endif
