#include <Arduino.h>
#include <Stepper.h>
#include "StepperClass.h"
#include "MethodDescriptor.h"
#include <stdlib.h>

void StepperClass::elaborate( MethodDescriptor* m ) {
    if (strcmp(m->getClass(), "Stepper") == 0) {

        ObjectsManager::elaborate(m);

        if (strcmp(m->getName(),"new") == 0) {       
            int prm = 0;
            v.insert(new Stepper (m->getInt(prm++), m->getInt(prm++), m->getInt(prm++)));
            Serial.println(v.getLastIndex());
        }

        if (strcmp(m->getName(), "setSpeed") == 0) {
            v[m->getObjectId()]->setSpeed(m->getInt(0));
            Serial.println("0");
        }

        if (strcmp(m->getName(), "step") == 0) {
            v[m->getObjectId()]->step(m->getInt(0));
            Serial.println("0");
        }

    }
};
