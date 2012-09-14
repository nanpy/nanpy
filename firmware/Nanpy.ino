#include <stdlib.h>

#include "PyOneWire.h"
#include "PyLiquidCrystal.h"
#include "MethodDescriptor.h"
#include "Utilities.h"
#include <LiquidCrystal.h>

PyLiquidCrystal* lcd_class;
PyOneWire* onewire_class;

int pin, value;

MethodDescriptor *m = NULL;

void elaborate()
{




    // send data only when you receive data
    if(m != NULL)
    {

        delete(m);

        m = NULL;
    }

    if (Serial.available() > 0)
    {

        m = new MethodDescriptor();

        if (strcmp(m->getName(), "digitalWrite") == 0)
        {
            digitalWrite(m->getInt(0), m->getInt(1));
            Serial.println("0");
        }

        if (strcmp(m->getName(), "digitalRead") == 0)
        {
            digitalRead(m->getInt(0));
            Serial.println("0");
        }

        if (strcmp(m->getName(), "delay") == 0)
        {
            delay(m->getInt(0));
            Serial.println("0");
        }

        

        lcd_class->elaborate(m);
        onewire_class->elaborate(m);

        /*if (strcmp(buffz, "digitalRead") == 0)
        {
            pin = atoi(readStringFromSerial());
            Serial.println(digitalRead(pin));
        }

        if (strcmp(buffz,"delay") == 0)
        {
            value = atoi(readStringFromSerial());
            delay(value);
            Serial.println("0");
        }

        lcd_class->elaborate(buffz);*/

    }

}

void setup() {
    onewire_class = new PyOneWire();
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


