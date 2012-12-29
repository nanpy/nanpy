#include <Arduino.h>
#include <CapacitiveSensor.h>
#include "CapacitiveSensorClass.h"
#include "MethodDescriptor.h"

void CapacitiveSensorClass::elaborate( MethodDescriptor* m ) {
    if (strcmp(m->getClass(), "CapacitiveSensor") == 0) {

        ObjectsManager::elaborate(m);

        if (strcmp(m->getName(), "new") == 0) {       
            v.insert(new CapacitiveSensor(m->getInt(0), m->getInt(1)));
            m->returns(v.getLastIndex());
        }

        if (strcmp(m->getName(), "capacitiveSensor") == 0) {
            m->returns(v[m->getObjectId()]->capacitiveSensor(m->getInt(0)));
        }

        if (strcmp(m->getName(), "capacitiveSensorRaw") == 0) {
            m->returns(v[m->getObjectId()]->capacitiveSensorRaw(m->getInt(0)));
        }

    }
};
