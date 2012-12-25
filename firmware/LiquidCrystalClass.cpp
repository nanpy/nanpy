#include <Arduino.h>
#include <LiquidCrystal.h>
#include "LiquidCrystalClass.h"
#include "MethodDescriptor.h"
#include <stdlib.h>
#include <math.h>

void LiquidCrystalClass::elaborate( MethodDescriptor* m ) {
    if (strcmp(m->getClass(), "Lcd") == 0) {

        ObjectsManager::elaborate(m);

        if (strcmp(m->getName(), "new") == 0) {       
            int prm = 0;
            v.insert(new LiquidCrystal (m->getInt(prm++), m->getInt(prm++), 
                            m->getInt(prm++), m->getInt(prm++), m->getInt(prm++), m->getInt(prm++)));
            v[m->getObjectId()]->begin(m->getInt(prm++), m->getInt(prm++));
            m->returns(v.getLastIndex());
        }

        if (strcmp(m->getName(), "printString") == 0) {
            if(m->getNArgs() == 3) {
                v[m->getObjectId()]->setCursor(m->getInt(1), m->getInt(2));
                v[m->getObjectId()]->print(m->getString(0));
            }
            else
                v[m->getObjectId()]->print(m->getString(0));
            m->returns(0);
        }

        if (strcmp(m->getName(), "setCursor") == 0) {
            v[m->getObjectId()]->setCursor(m->getInt(0), m->getInt(1));
            m->returns(0);
        }

    }
};
