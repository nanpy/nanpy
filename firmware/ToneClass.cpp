#include <Arduino.h>
#include "ToneClass.h"
#include "MethodDescriptor.h"
#include <stdlib.h>

void ToneClass::elaborate( MethodDescriptor* m ) {
    if (strcmp(m->getClass(), "Tone") == 0) {

        ObjectsManager::elaborate(m);

        if (strcmp(m->getName(),"new") == 0) {
            v.insert(new Tone (m->getInt(0)));
            m->returns(v.getLastIndex());
        }

        if (strcmp(m->getName(), "play") == 0) {
            v[m->getObjectId()]->play(m->getInt(0), m->getInt(0));
            m->returns(0);
        }

        if (strcmp(m->getName(), "stop") == 0) {
            v[m->getObjectId()]->stop();
            m->returns(0);
        }

    }
};
