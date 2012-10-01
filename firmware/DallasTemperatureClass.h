#ifndef DALLAS_TEMP_CLASS
#define DALLAS_TEMP_CLASS

#include "BaseClass.h"

class DallasTemperature;
class MethodDescriptor;

class DallasTemperatureClass: public ObjectsManager<DallasTemperature> {

    public:
        void elaborate( MethodDescriptor* m );

};

#endif
