#ifndef PY_ARDUINO_CLASS
#define PY_ARDUINO_CLASS

class MethodDescriptor;

class ArduinoClass {

    public:
        virtual void elaborate( MethodDescriptor* m ) = 0;

};

#endif
