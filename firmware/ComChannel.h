#ifndef COM_CH
#define COM_CH

#ifndef BAUDRATE
    #define BAUDRATE 9600
#endif

#include <HardwareSerial.h>
#include <Arduino.h>

class ComChannel {

    public:

        static bool available() {
            #if BOARD == 2
            if (Serial1.available() > 0)
            #else
            if (Serial.available() > 0)
            #endif
                return true;
            else
                return false;
        }

        static void connect() {
            #if BOARD == 2
            Serial1.begin(BAUDRATE);
            #else
            Serial.begin(BAUDRATE);
            #endif
        }

        static void println(String& val) {
            #if BOARD == 2
            Serial1.println(val);
            #else
            Serial.println(val);
            #endif
        }

        static void println(const char* val) {
            #if BOARD == 2
            Serial1.println(val);
            #else
            Serial.println(val);
            #endif
        }

        static void println(int val) {
            #if BOARD == 2
            Serial1.println(val);
            #else
            Serial.println(val);
            #endif
        }

        static void println(float val) {
            #if BOARD == 2
            Serial1.println(val);
            #else
            Serial.println(val);
            #endif
        }

        static void println(double val) {
            #if BOARD == 2
            Serial1.println(val);
            #else
            Serial.println(val);
            #endif
        }

};

#endif

