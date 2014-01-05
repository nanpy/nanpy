#include <Arduino.h>
#include "ArduinoClass.h"
#include <stdlib.h>


const char* nanpy::ArduinoClass::get_firmware_id()
{
    return "A";
}

void nanpy::ArduinoClass::elaborate( nanpy::MethodDescriptor* m ) {
        if (strcmp(m->getName(), "dw") == 0) { // digitalWrite
            digitalWrite(m->getInt(0), m->getInt(1));
            m->returns(0);
        }

        if (strcmp(m->getName(), "r") == 0) {  // digitalRead
            m->returns(digitalRead(m->getInt(0)));
        }

        if (strcmp(m->getName(), "aw") == 0) { // analogWrite
            analogWrite(m->getInt(0), m->getInt(1));
            m->returns(0);
        }

        if (strcmp(m->getName(), "a") == 0) {  // analogRead
            m->returns(analogRead(m->getInt(0)));
        }

        if (strcmp(m->getName(), "pm") == 0) {  // pinMode
            pinMode(m->getInt(0), m->getInt(1));
            m->returns(0);
        }

        if (strcmp(m->getName(), "delay") == 0) {
            m->returns(0);
        }

        if (strcmp(m->getName(), "m") == 0) {  // millis
            m->returns(millis());
        }

        if (strcmp(m->getName(), "s") == 0) {  // shiftOut
            // shiftOut(dataPin, clockPin, bitOrder, value)
            shiftOut(m->getInt(0), m->getInt(1), m->getInt(2), m->getInt(3));
            m->returns(0);
        }
};
