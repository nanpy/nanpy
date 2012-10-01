#include "BaseClass.h"

#include "ArduinoClass.h"
#include "OneWireClass.h"
#include "StepperClass.h"
#include "ServoClass.h"
#include "DallasTemperatureClass.h"
#include "LiquidCrystalClass.h"
#include "ToneClass.h"
#include "MethodDescriptor.h"

#ifndef BAUDRATE
    #define BAUDRATE 9600
#endif

MethodDescriptor *m = NULL;

void setup() {

    REGISTER_CLASS(ArduinoClass);
    REGISTER_CLASS(LiquidCrystalClass);
    REGISTER_CLASS(OneWireClass);
    REGISTER_CLASS(DallasTemperatureClass);
    REGISTER_CLASS(StepperClass);
    REGISTER_CLASS(ServoClass);
    REGISTER_CLASS(ToneClass);

    Serial.begin(BAUDRATE);

    while (Serial.available() <= 0) {
        delay(300);
    }
}

void loop() {
    if (Serial.available() > 0) {
        m = new MethodDescriptor();
        Register::elaborate(m);
    }
}

