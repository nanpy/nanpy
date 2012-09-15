#include <Arduino.h>
#include <LiquidCrystal.h>
#include "LiquidCrystalClass.h"
#include "MethodDescriptor.h"
#include <stdlib.h>

lcds lcd1;

PyLiquidCrystal::PyLiquidCrystal() {

};

void PyLiquidCrystal::elaborate( MethodDescriptor* m ) {
    if (strcmp(m->getClass(), "Lcd") == 0) {

        if (strcmp(m->getName(),"new") == 0) {       
            int prm = 0;
            lcd1.obj = new LiquidCrystal (m->getInt(prm++), m->getInt(prm++), 
                            m->getInt(prm++), m->getInt(prm++), m->getInt(prm++), m->getInt(prm++));
            lcd1.obj->begin(m->getInt(prm++), m->getInt(prm++));
        }

        if (strcmp(m->getName(), "print") == 0) {
            lcd1.obj->print(m->getString(0));
            Serial.println("0");
        }

        if (strcmp(m->getName(), "setCursor") == 0) {
            lcd1.obj->setCursor(m->getInt(0), m->getInt(1));
            Serial.println("0");
        }

    }
};
