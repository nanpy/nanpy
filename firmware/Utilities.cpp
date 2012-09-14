#include "Utilities.h"
#include <stdlib.h>
#include <HardwareSerial.h>

char* readStringFromSerial()
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
