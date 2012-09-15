#ifndef PY_LIQUID_CRYSTAL
#define PY_LIQUID_CRYSTAL
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
