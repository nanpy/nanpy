#ifndef LIQUID_CRYSTAL_CLASS
#define LIQUID_CRYSTAL_CLASS
#include <stdlib.h>
#include "ArduinoClass.h"

class LiquidCrystal;
class MethodDescriptor;

char* readStringFromSerial();

struct lcds
{
    char* name;
    LiquidCrystal* obj;
};

class LiquidCrystalClass: public ArduinoClass {

    public:

        LiquidCrystalClass();

        void elaborate( MethodDescriptor* m );

};

#endif
