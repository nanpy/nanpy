#include <Arduino.h>
#include "ArduinoClass.h"
#include "MethodDescriptor.h"
#include <stdlib.h>

void ArduinoClass::elaborate( MethodDescriptor* m ) {
    if (strcmp(m->getClass(), "Arduino") == 0) {
        if (strcmp(m->getName(), "digitalWrite") == 0) {
            digitalWrite(m->getInt(0), m->getInt(1));
            m->returns(0);
        }

        if (strcmp(m->getName(), "digitalRead") == 0) {
            m->returns(digitalRead(m->getInt(0)));
        }

        if (strcmp(m->getName(), "analogWrite") == 0) {
            analogWrite(m->getInt(0), m->getInt(1));
            m->returns(0);
        }

        if (strcmp(m->getName(), "analogRead") == 0) {
            m->returns(analogRead(m->getInt(0)));
        }

        if (strcmp(m->getName(), "pinMode") == 0) {
            pinMode(m->getInt(0), m->getInt(1));
            m->returns(0);
        }

        if (strcmp(m->getName(), "delay") == 0) {
            m->returns(0);
        }
    }
};
