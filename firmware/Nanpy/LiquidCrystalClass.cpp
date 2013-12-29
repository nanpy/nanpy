#include "cfg.h"

#if USE_LiquidCrystal

#include <Arduino.h>
#include <LiquidCrystal.h>
#include "LiquidCrystalClass.h"
#include <stdlib.h>
#include <math.h>

const char* nanpy::LiquidCrystalClass::get_firmware_id()
{
    return "Lcd";
}

void nanpy::LiquidCrystalClass::elaborate( nanpy::MethodDescriptor* m ) {
        ObjectsManager<LiquidCrystal>::elaborate(m);

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
};
#endif
