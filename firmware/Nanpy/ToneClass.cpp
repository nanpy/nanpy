#include "cfg.h"

#if USE_Tone

#include <Arduino.h>
#include "ToneClass.h"
#include <stdlib.h>

const char* nanpy::ToneClass::get_firmware_id()
{
    return "Tone";
}

void nanpy::ToneClass::elaborate( nanpy::MethodDescriptor* m ) {
        ObjectsManager<Tone>::elaborate(m);

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
};
#endif
