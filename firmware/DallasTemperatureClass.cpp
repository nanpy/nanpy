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
            Serial.println(v.getLastIndex());
        }

        if (strcmp(m->getName(), "requestTemperatures") == 0) {
            v[m->getObjectId()]->requestTemperatures();
            Serial.println("0");
        }

        if (strcmp(m->getName(), "getTempCByIndex") == 0) {
            Serial.println(v[m->getObjectId()]->getTempCByIndex(m->getInt(0)));
        }

        if (strcmp(m->getName(), "getTempFByIndex") == 0) {
            Serial.println(v[m->getObjectId()]->getTempFByIndex(m->getInt(0)));
        }

        if (strcmp(m->getName(), "toFahrenheit") == 0) {
            Serial.println(DallasTemperature::toFahrenheit(m->getFloat(0)));
        }

        if (strcmp(m->getName(), "toCelsius") == 0) {
            Serial.println(DallasTemperature::toCelsius(m->getFloat(0)));
        }

    }
};
