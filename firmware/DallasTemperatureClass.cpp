#include <Arduino.h>
#include <DallasTemperature.h>
#include <OneWire.h>
#include "DallasTemperatureClass.h"
#include "MethodDescriptor.h"
#include <stdlib.h>

void DallasTemperatureClass::elaborate( MethodDescriptor* m ) {

    if (strcmp(m->getClass(), "DallasTemperature") == 0) {

        ObjectsManager::elaborate(m);

        if (strcmp(m->getName(),"new") == 0) {       
            int prm = 0;
            OneWire* wr = new OneWire(m->getInt(0));
            DallasTemperature* dt = new DallasTemperature(&(*wr));
            v.insert(dt);
            dt->begin();
            m->returns(v.getLastIndex());
        }

        if (strcmp(m->getName(), "requestTemperatures") == 0) {
            v[m->getObjectId()]->requestTemperatures();
            m->returns("0");
        }

        if (strcmp(m->getName(), "getTempCByIndex") == 0) {
            m->returns(v[m->getObjectId()]->getTempCByIndex(m->getInt(0)));
        }

        if (strcmp(m->getName(), "getTempFByIndex") == 0) {
            m->returns(v[m->getObjectId()]->getTempFByIndex(m->getInt(0)));
        }

        if (strcmp(m->getName(), "toFahrenheit") == 0) {
            m->returns(DallasTemperature::toFahrenheit(m->getFloat(0)));
        }

        if (strcmp(m->getName(), "toCelsius") == 0) {
            m->returns(DallasTemperature::toCelsius(m->getFloat(0)));
        }

    }
};
