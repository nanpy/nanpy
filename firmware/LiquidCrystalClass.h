#ifndef LIQUID_CRYSTAL_CLASS
#define LIQUID_CRYSTAL_CLASS

#include <stdlib.h>
#include "SlimArray.h"
#include "ArduinoClass.h"

class LiquidCrystal;
class MethodDescriptor;

char* readStringFromSerial();

class LiquidCrystalClass: public ArduinoClass {

    private:

        SlimArray <LiquidCrystal*> v;

    public:

        LiquidCrystalClass();
        void elaborate( MethodDescriptor* m );

};

#endif
