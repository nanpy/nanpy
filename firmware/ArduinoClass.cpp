#include <Arduino.h>
#include "ArduinoClass.h"
#include <stdlib.h>


byte pinModeRead(int pin)
{
        byte bitmask = digitalPinToBitMask(pin);
        word port = digitalPinToPort(pin);
        byte reg = *portModeRegister(port);
        byte mode = (reg & bitmask) ? 1 : 0;
        return mode;
}

void nanpy::ArduinoClass::elaborate( nanpy::MethodDescriptor* m ) {
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

        if (strcmp(m->getName(), "pinModeRead") == 0) {
            m->returns(pinModeRead(m->getInt(0)));
        }

        if (strcmp(m->getName(), "delay") == 0) {
            m->returns(0);
        }
    }
};
