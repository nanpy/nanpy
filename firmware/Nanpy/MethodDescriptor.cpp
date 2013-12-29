#include "MethodDescriptor.h"
#include <stdlib.h>
#include <math.h>
#include "ComChannel.h"
#include <Arduino.h>

nanpy::MethodDescriptor::MethodDescriptor() {

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

int nanpy::MethodDescriptor::getNArgs() {
    return this->n_args;
};

bool nanpy::MethodDescriptor::getBool(int n) {
  return strcmp(this->stack[n], "True") == 0 ? true : false;
};

int nanpy::MethodDescriptor::getInt(int n) {
    return atoi(this->stack[n]);
};

float nanpy::MethodDescriptor::getFloat(int n) {
    return atof(this->stack[n]);
};

double nanpy::MethodDescriptor::getDouble(int n) {
    return atof(this->stack[n]);
};

char* nanpy::MethodDescriptor::getString(int n) {
    return this->stack[n];
};

char* nanpy::MethodDescriptor::getClass() {
    return this->classname;
};

int nanpy::MethodDescriptor::getObjectId() {
    return this->objid;
};

char* nanpy::MethodDescriptor::getName() {
    return this->name;
};

void nanpy::MethodDescriptor::returns(String& val) {
    ComChannel::println(val);
}

void nanpy::MethodDescriptor::returns(const char* val) {
    ComChannel::println(val);
}

void nanpy::MethodDescriptor::returns(int val) {
    ComChannel::println(val);
}

void nanpy::MethodDescriptor::returns(unsigned int val) {
    ComChannel::println(val);
}

void nanpy::MethodDescriptor::returns(float val) {
    ComChannel::println(val);
}

void nanpy::MethodDescriptor::returns(double val) {
    ComChannel::println(val);
}

void nanpy::MethodDescriptor::returns(long val) {
    ComChannel::println(val);
}

void nanpy::MethodDescriptor::returns(unsigned long val) {
    ComChannel::println(val);
}

nanpy::MethodDescriptor::~MethodDescriptor() {
    delete(name);
    delete(classname);

    for(int n = 0; n < this->n_args; n++) {
        delete(this->stack[n]);
    }

    delete(this->stack);
}
