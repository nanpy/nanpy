#include <Arduino.h>
#include <Stepper.h>
#include "ToneClass.h"
#include "MethodDescriptor.h"
#include <stdlib.h>

ToneClass::ToneClass():v(0) {

};

void ToneClass::elaborate( MethodDescriptor* m ) {
    if (strcmp(m->getClass(), "Tone") == 0) {

        if (strcmp(m->getName(),"new") == 0) {
            v.insert(new Tone (m->getInt(0)));
            Serial.println(v.getLastIndex());
        }

        if (strcmp(m->getName(), "play") == 0) {
            v[m->getObjectId()]->play(m->getInt(0), m->getInt(0));
            Serial.println("0");
        }

        if (strcmp(m->getName(), "stop") == 0) {
            v[m->getObjectId()]->stop();
            Serial.println("0");
        }

        if (strcmp(m->getName(), "remove") == 0) {
            delete(v[m->getObjectId()]);
            v.remove(m->getObjectId());
            Serial.println("0");
        }

    }
};
