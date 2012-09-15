#include <stdlib.h>

#include "ArduinoClass.h"
#include "PyOneWire.h"
#include "PyLiquidCrystal.h"
#include "MethodDescriptor.h"
#include "Utilities.h"
#include "SlimArray.h"

SlimArray <ArduinoClass*> classes(2);

int pin, value;

MethodDescriptor *m = NULL;

void elaborate()
{

    // send data only when you receive data
    if(m != NULL) {
        delete(m);
        m = NULL;
    }

    if (Serial.available() > 0) {

        m = new MethodDescriptor();

        if (strcmp(m->getName(), "digitalWrite") == 0) {
            digitalWrite(m->getInt(0), m->getInt(1));
            Serial.println("0");
        }

        if (strcmp(m->getName(), "digitalRead") == 0) {
            digitalRead(m->getInt(0));
            Serial.println("0");
        }

        if (strcmp(m->getName(), "delay") == 0) {
            delay(m->getInt(0));
            Serial.println("0");
        }

        for(int i = 0 ; i < classes.getSize() ; i++)
            classes[i]->elaborate(m);

    }

}

void setup() {
    classes.insert(new PyOneWire());
    classes.insert(new PyLiquidCrystal());
    pinMode(13, OUTPUT);
    pinMode(12, INPUT); 
    Serial.begin(9600);
    while (Serial.available() <= 0) {
        delay(300);
    }
}

void loop(){
    elaborate();
}


