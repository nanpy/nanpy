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

class PyLiquidCrystal: public ArduinoClass {

    public:

        PyLiquidCrystal();

        void elaborate( MethodDescriptor* m );

};

#endif
