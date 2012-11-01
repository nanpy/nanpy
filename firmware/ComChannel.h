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
            if (Serial.available() > 0)
                return true;
            else
                return false;
        }

        static void connect() {
            Serial.begin(BAUDRATE);
            while (Serial.available() <= 0) {
                delay(300);
            }
        }

        static void println(String& val) {
            Serial.println(val);
        }

        static void println(const char* val) {
            Serial.println(val);
        }

        static void println(int val) {
            Serial.println(val);
        }

        static void println(float val) {
            Serial.println(val);
        }

        static void println(double val) {
            Serial.println(val);
        }

};

#endif

