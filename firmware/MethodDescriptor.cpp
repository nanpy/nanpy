#include "MethodDescriptor.h"
#include "Utilities.h"
#include <stdlib.h>
#include <math.h>

MethodDescriptor::MethodDescriptor() {

    this->classname = readStringFromSerial();
    char* buff = readStringFromSerial();
    this->objid = atoi(buff);
    free(buff);

    buff = readStringFromSerial();
    this->n_args = atoi(buff);
    free(buff);
    this->name = readStringFromSerial();

    this->stack = (char**)malloc(sizeof(char*) * this->n_args);

    for(int n = 0; n < this->n_args; n++)
    {
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

MethodDescriptor::~MethodDescriptor() {
    delete(name);
    delete(classname);

    for(int n = 0; n < this->n_args; n++)
    {
        delete(this->stack[n]);
    }

    delete(this->stack);
}
