#ifndef COM_CHANNEL
#define COM_CHANNEL

#define BAUDRATE 9600

#include <Arduino.h>

class ComChannel {

    public:
        static bool available();
        static void connect();
        static void println(String& val);
        static void println(const char* val);
        static void println(int val);
        static void println(float val);
        static void println(double val);
        static void println(long val);
        static char* readLine();
};

#endif

