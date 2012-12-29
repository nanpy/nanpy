#include "MethodDescriptor.h"
#include <stdlib.h>
#include <math.h>
#include "ComChannel.h"
#include <Arduino.h>

MethodDescriptor::MethodDescriptor() {

    this->classname = ComChannel::readLine();

    char* buff;

    buff = ComChannel::readLine();
    this->objid = atoi(buff);
    free(buff);

    buff = ComChannel::readLine();
    this->n_args = atoi(buff);
    free(buff);

    this->name = ComChannel::readLine();

    this->stack = (char**)malloc(sizeof(char*) * this->n_args);

    for(int n = 0; n < this->n_args; n++) {
        this->stack[n] = ComChannel::readLine();
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

void MethodDescriptor::returns(long val) {
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
