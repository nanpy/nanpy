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

bool ComChannel::available() {
    if (Serial.available() > 0)
        return true;
    else
        return false;
}

void ComChannel::connect() {
    Serial.begin(BAUDRATE);
}

void ComChannel::println(String& val) {
    Serial.println(val);
}

void ComChannel::println(const char* val) {
    Serial.println(val);
}

void ComChannel::println(int val) {
    Serial.println(val);
}

void ComChannel::println(float val) {
    Serial.println(val);
}

void ComChannel::println(double val) {
    Serial.println(val);
}

void ComChannel::println(long val) {
    Serial.println(val);
}

char* ComChannel::readLine() {
    return readLineFromSerial();
}

