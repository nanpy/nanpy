#ifndef DALLAS_TEMP_CLASS
#define DALLAS_TEMP_CLASS

#include <stdlib.h>
#include "SlimArray.h"
#include "ArduinoClass.h"

class DallasTemperature;
class MethodDescriptor;

char* readStringFromSerial();

class DallasTemperatureClass: public ArduinoClass {

    private:

        SlimArray <DallasTemperature*> v;

    public:

        DallasTemperatureClass();
        void elaborate( MethodDescriptor* m );

};

#endif
