#include "MethodDescriptor.h"
#include <stdlib.h>
#include <math.h>
#include "ComChannel.h"

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

MethodDescriptor::MethodDescriptor() {

    this->classname = readStringFromSerial();

    char* buff;

    buff = readStringFromSerial();
    this->objid = atoi(buff);
    free(buff);

    buff = readStringFromSerial();
    this->n_args = atoi(buff);
    free(buff);

    this->name = readStringFromSerial();

    this->stack = (char**)malloc(sizeof(char*) * this->n_args);

    for(int n = 0; n < this->n_args; n++) {
        this->stack[n] = readStringFromSerial();
    }

};

int MethodDescriptor::getNArgs() {
    return this->n_args;
};

int MethodDescriptor::getInt(int n) {
    return atoi(this->stack[n]);
};

float MethodDescriptor::getFloat(int n) {
    return atof(this->stack[n]);
};

double MethodDescriptor::getDouble(int n) {
    return atof(this->stack[n]);
};

char* MethodDescriptor::getString(int n) {
    return this->stack[n];
};

char* MethodDescriptor::getClass() {
    return this->classname;
};

int MethodDescriptor::getObjectId() {
    return this->objid;
};

char* MethodDescriptor::getName() {
    return this->name;
};

void MethodDescriptor::returns(String& val) {
    ComChannel::println(val);
}

void MethodDescriptor::returns(const char* val) {
    ComChannel::println(val);
}

void MethodDescriptor::returns(int val) {
    ComChannel::println(val);
}

void MethodDescriptor::returns(float val) {
    ComChannel::println(val);
}

void MethodDescriptor::returns(double val) {
    ComChannel::println(val);
}

MethodDescriptor::~MethodDescriptor() {
    delete(name);
    delete(classname);

    for(int n = 0; n < this->n_args; n++) {
        delete(this->stack[n]);
    }

    delete(this->stack);
}
