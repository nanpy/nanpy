#include <EEPROM.h>
#include <Servo.h>
#include <LiquidCrystal.h>
#include <Stepper.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <CapacitiveSensor.h>
#include <DHT.h>

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
#include "EEPROMClass.h"
#include "DHTClass.h"

#include "DefineClass.h"
#include "ArduinoCoreClass.h"
#include "WatchdogClass.h"
#include "RegisterClass.h"

#include <avr/wdt.h>

using namespace nanpy;

MethodDescriptor *m = NULL;

void setup() {
    
    // disable watchdog (http://www.nongnu.org/avr-libc/user-manual/group__avr__watchdog.html)
    MCUSR = 0;
    wdt_disable();
   
    REGISTER_CLASS(nanpy::EEPROMClass);         // 0.3 k
    REGISTER_CLASS(ArduinoClass);               // 0.8 k
    REGISTER_CLASS(LiquidCrystalClass);         // 2.3 k
    REGISTER_CLASS(OneWireClass);               // 1.7 k
//    REGISTER_CLASS(DallasTemperatureClass);     // 6.1 k
    REGISTER_CLASS(StepperClass);               // 0.8 k
    REGISTER_CLASS(ServoClass);                 // 2.5 k
    REGISTER_CLASS(ToneClass);                  // 2.2 k
    REGISTER_CLASS(CapacitiveSensorClass);      // 2.2 k
    
    // new classes
    REGISTER_CLASS(DefineClass);                // 0.6 k
    REGISTER_CLASS(ArduinoCoreClass);           // 0.7 k
    REGISTER_CLASS(WatchdogClass);              // 0.2 k
    REGISTER_CLASS(RegisterClass);              // 1.5 k
    REGISTER_CLASS(DHTClass);

    ComChannel::connect();
}

void loop() {
    if(ComChannel::available()) {
        m = new MethodDescriptor();
        Register::elaborate(m);
    }
}
