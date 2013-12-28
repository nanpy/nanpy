#include <Arduino.h>
#include <DHT.h>
#include "DHTClass.h"
#include <stdlib.h>

void nanpy::DHTClass::elaborate( MethodDescriptor* m ) {
    if (strcmp(m->getClass(), "DHT") == 0) {

        ObjectsManager<DHT>::elaborate(m);

        if (strcmp(m->getName(),"new") == 0) {
	  v.insert(new DHT (m->getInt(0), m->getInt(1), m->getInt(2)));
            m->returns(v.getLastIndex());
        }

        if (strcmp(m->getName(), "begin") == 0) {
            v[m->getObjectId()]->begin();
            m->returns(0);
        }

        if (strcmp(m->getName(), "readHumidity") == 0) {
	  m->returns(v[m->getObjectId()]->readHumidity());
        }

        if (strcmp(m->getName(), "readTemperature") == 0) {
	  m->returns(v[m->getObjectId()]->readTemperature(m->getBool(0)));
        }
    }
};
