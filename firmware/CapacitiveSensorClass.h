#ifndef CAPACITIVE_SENSOR_CLASS
#define CAPACITIVE_SENSOR_CLASS

#include "BaseClass.h"

class CapacitiveSensor;
class MethodDescriptor;

class CapacitiveSensorClass : public ObjectsManager<CapacitiveSensor> {

    public:
        void elaborate( MethodDescriptor* m );

};

#endif
