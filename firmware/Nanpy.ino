#include "BaseClass.h"
#include "ArduinoClass.h"
#include "OneWireClass.h"
#include "StepperClass.h"
#include "ServoClass.h"
#include "DallasTemperatureClass.h"
#include "LiquidCrystalClass.h"
#include "CapacitiveSensorClass.h"
#include "ToneClass.h"
#include "MethodDescriptor.h"
#include "ComChannel.h"

MethodDescriptor *m = NULL;

void setup() {

    REGISTER_CLASS(ArduinoClass);
    REGISTER_CLASS(LiquidCrystalClass);
    REGISTER_CLASS(OneWireClass);
    REGISTER_CLASS(DallasTemperatureClass);
    REGISTER_CLASS(StepperClass);
    REGISTER_CLASS(ServoClass);
    REGISTER_CLASS(ToneClass);
    REGISTER_CLASS(CapacitiveSensorClass);

    ComChannel::connect();
}

void loop() {
    if(ComChannel::available()) {
        m = new MethodDescriptor();
        Register::elaborate(m);
    }
}

