#include <Arduino.h>
#include <Servo.h>
#include "ServoClass.h"
#include "MethodDescriptor.h"
#include <stdlib.h>

void ServoClass::elaborate( MethodDescriptor* m ) {
    if (strcmp(m->getClass(), "Servo") == 0) {

        ObjectsManager::elaborate(m);

        if (strcmp(m->getName(),"new") == 0) {       
            v.insert(new Servo());
            v[v.getLastIndex()]->attach(m->getInt(0));
            m->returns(v.getLastIndex());
        }

        if (strcmp(m->getName(), "write") == 0) {
            v[m->getObjectId()]->write(m->getInt(0));
            m->returns(0);
        }

        if (strcmp(m->getName(), "read") == 0) {
            m->returns(v[m->getObjectId()]->read());
        }

        if (strcmp(m->getName(), "writeMicroseconds") == 0) {
            v[m->getObjectId()]->writeMicroseconds(m->getInt(0));
            m->returns(0);
        }

        if (strcmp(m->getName(), "readMicroseconds") == 0) {
            m->returns(v[m->getObjectId()]->readMicroseconds());
        }

        if (strcmp(m->getName(), "detach") == 0) {
            v[m->getObjectId()]->detach();
            m->returns(0);
        }

        if (strcmp(m->getName(), "attached") == 0) {
            m->returns(v[m->getObjectId()]->attached());
        }

    }
};
