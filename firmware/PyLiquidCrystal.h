#ifndef PY_LIQUID_CRYSTAL
#define PY_LIQUID_CRYSTAL
#include <stdlib.h>

class LiquidCrystal;
class MethodDescriptor;

char* readStringFromSerial();

struct lcds
{
    char* name;
    LiquidCrystal* obj;
};

class PyLiquidCrystal {

    public:

        PyLiquidCrystal();

        void elaborate( MethodDescriptor* m );

        //void getObjectByName()
        //...

};

#endif
