#ifndef LIQUID_CRYSTAL_CLASS
#define LIQUID_CRYSTAL_CLASS

#include "BaseClass.h"

class LiquidCrystal;
class MethodDescriptor;

class LiquidCrystalClass : public ObjectsManager<LiquidCrystal> {

    public:
        void elaborate( MethodDescriptor* m );

};



#endif
