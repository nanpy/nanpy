#pragma once

#define BAUDRATE 115200

#define USE_Servo                                   1
#define USE_Tone                                    0
#define USE_LiquidCrystal                           1
#define USE_Stepper                                 1
#define USE_EEPROM                                  1
#define USE_RAM                                     1
#define USE_Define                                  1
#define USE_ArduinoCore                             1
#define USE_Watchdog                                1
#define USE_Register                                1
#define USE_Info                                    1

// conflicts Tone
#define USE_Counter                                 1


// external libraries should be installed for the following features:
#define USE_OneWire                                 0
#define USE_DallasTemperature                       0
#define USE_CapacitiveSensor                        0
#define USE_DHT                                     0




#if USE_Tone
# if USE_Counter
#  error "USE_Tone conflicts with USE_Counter!"
# endif
#endif
