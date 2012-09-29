#include <Arduino.h>
#include <Stepper.h>
#include "StepperClass.h"
#include "MethodDescriptor.h"
#include <stdlib.h>

StepperClass::StepperClass():v(2) {

};

void StepperClass::elaborate( MethodDescriptor* m ) {
    if (strcmp(m->getClass(), "Stepper") == 0) {

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

        if (strcmp(m->getName(), "remove") == 0) {
            delete(v[m->getObjectId()]);
            v.remove(m->getObjectId());
            Serial.println("0");
        }

    }
};
