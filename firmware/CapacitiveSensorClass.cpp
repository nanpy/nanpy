#include <Arduino.h>
#include <CapacitiveSensor.h>
#include "CapacitiveSensorClass.h"
#include "MethodDescriptor.h"

void CapacitiveSensorClass::elaborate( MethodDescriptor* m ) {
    if (strcmp(m->getClass(), "CapacitiveSensor") == 0) {

        ObjectsManager::elaborate(m);

        if (strcmp(m->getName(), "new") == 0) {       
            //TODO
        }

    }
};
