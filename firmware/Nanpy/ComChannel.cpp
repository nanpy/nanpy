#include "ComChannel.h"
#include <Arduino.h>

char* readLineFromSerial()
{
    char* buffer = (char*)malloc(30);
    int i=0;
    char ch = '0';
    do {
        ch = Serial.read();
        if(ch != '\0' && ch < 255 && ch >= 0) {
            buffer[i++] = ch;
        }
    } while(ch != '\0');
    char* buffer2 = (char*)malloc(i + 1);
    buffer[i] = '\0';
    strcpy(buffer2, buffer);
    free(buffer);
    return buffer2;
};

bool nanpy::ComChannel::available() {
    if (Serial.available() > 0)
        return true;
    else
        return false;
}

void nanpy::ComChannel::connect() {
    Serial.begin(BAUDRATE);
}

void nanpy::ComChannel::println(String& val) {
    Serial.println(val);
}

void nanpy::ComChannel::println(const char* val) {
    Serial.println(val);
}

void nanpy::ComChannel::println(int val) {
    Serial.println(val);
}

void nanpy::ComChannel::println(unsigned int val) {
    Serial.println(val);
}

void nanpy::ComChannel::println(float val) {
    Serial.println(val);
}

void nanpy::ComChannel::println(double val) {
    Serial.println(val);
}

void nanpy::ComChannel::println(long val) {
    Serial.println(val);
}

void nanpy::ComChannel::println(unsigned long val) {
    Serial.println(val);
}

char* nanpy::ComChannel::readLine() {
    return readLineFromSerial();
}

