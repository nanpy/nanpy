#include "cfg.h"

#if USE_Stepper

#include <Arduino.h>
#include <Stepper.h>
#include "StepperClass.h"
#include <stdlib.h>

const char* nanpy::StepperClass::get_firmware_id()
{
    return "Stepper";
}

void nanpy::StepperClass::elaborate( MethodDescriptor* m ) {
        ObjectsManager<Stepper>::elaborate(m);

        if (strcmp(m->getName(),"new") == 0) {       
            int prm = 0;
            v.insert(new Stepper (m->getInt(prm++), m->getInt(prm++), m->getInt(prm++)));
            m->returns(v.getLastIndex());
        }

        if (strcmp(m->getName(), "setSpeed") == 0) {
            v[m->getObjectId()]->setSpeed(m->getInt(0));
            m->returns(0);
        }

        if (strcmp(m->getName(), "step") == 0) {
            v[m->getObjectId()]->step(m->getInt(0));
            m->returns(0);
        }
}


#endif

