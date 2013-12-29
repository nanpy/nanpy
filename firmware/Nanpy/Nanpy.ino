#include "cfg.h"

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
#include "CounterClass.h"
#include "InfoClass.h"

#include <avr/wdt.h>

using namespace nanpy;

MethodDescriptor *m = NULL;

void setup() {
    
    // disable watchdog (http://www.nongnu.org/avr-libc/user-manual/group__avr__watchdog.html)
    MCUSR = 0;
    wdt_disable();
   
    REGISTER_CLASS(ArduinoClass);                                                   // 0.8 k

    REGISTER_CLASS_CONDITIONAL(nanpy::EEPROMClass, USE_EEPROM);                     // 0.3 k
    REGISTER_CLASS_CONDITIONAL(LiquidCrystalClass, USE_LiquidCrystal);              //  2.3 k
    REGISTER_CLASS_CONDITIONAL(OneWireClass, USE_OneWire);                          // 1.7 k
    REGISTER_CLASS_CONDITIONAL(DallasTemperatureClass, USE_DallasTemperature);      // 6.1 k
    REGISTER_CLASS_CONDITIONAL(StepperClass, USE_Stepper);                          // 0.8 k
    REGISTER_CLASS_CONDITIONAL(ServoClass, USE_Servo);                              // 2.5 k
    REGISTER_CLASS_CONDITIONAL(ToneClass, USE_Tone);                                // 2.2 k
    REGISTER_CLASS_CONDITIONAL(CapacitiveSensorClass, USE_CapacitiveSensor);        // 2.2 k
    REGISTER_CLASS_CONDITIONAL(DefineClass, USE_Define);                            // 0.6 k
    REGISTER_CLASS_CONDITIONAL(ArduinoCoreClass, USE_ArduinoCore);                  // 
    REGISTER_CLASS_CONDITIONAL(WatchdogClass, USE_Watchdog);                        // 0.2 k
    REGISTER_CLASS_CONDITIONAL(RegisterClass, USE_Register);                        // 1.5 k

    REGISTER_CLASS_CONDITIONAL(CounterClass, USE_Counter);                          // 
    REGISTER_CLASS_CONDITIONAL(InfoClass, USE_Info);                          // 
    REGISTER_CLASS_CONDITIONAL(DHTClass, USE_DHT);

    ComChannel::connect();
}

void loop() {
    if(ComChannel::available()) {
        m = new MethodDescriptor();
        Register::elaborate(m);
    }
}
