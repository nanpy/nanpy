#include <Arduino.h>
#include "ArduinoCoreClass.h"
#include <stdlib.h>

#define RETURN_GLOBAL_FUNC(x)         if (strcmp(m->getName(), #x) == 0) { m->returns(x()); }
#define RETURN_PIN_FUNC(x)         if (strcmp(m->getName(), #x) == 0) { m->returns(x(m->getInt(0))); }
#define RETURN_PORT_FUNC(x)        if (strcmp(m->getName(), #x) == 0) { m->returns(*x(m->getInt(0))); }

int totalPinCount()
{
    //    HACK!
    for (int i = 0; i < 100; i++)
    {
        byte x = digitalPinToBitMask(i);
        bool ok = false;
        for (int j = 0; j < 8; j++)
        {
            if (x == (1 << j))
            {
                ok = true;
                break;
            }
        }

        if (!ok)
        {
            return i;
        }
    }
    return -1;
}

// http://code.google.com/p/tinkerit/wiki/SecretVoltmeter
long readVcc()
{
    long result;
    // Read 1.1V reference against AVcc
    ADMUX = _BV(REFS0) | _BV(MUX3) | _BV(MUX2) | _BV(MUX1);
    delay(2); // Wait for Vref to settle
    ADCSRA |= _BV(ADSC); // Convert
    while (bit_is_set(ADCSRA, ADSC))
        ;
    result = ADCL;
    result |= ADCH << 8;
    result = 1126400L / result; // Back-calculate AVcc in mV
    return result;
}


void nanpy::ArduinoCoreClass::elaborate(nanpy::MethodDescriptor* m)
{
    if (strcmp(m->getClass(), "ArduinoCore") == 0)
    {
        RETURN_PIN_FUNC(digitalPinToBitMask);
        RETURN_PIN_FUNC(digitalPinToPort);
        RETURN_PIN_FUNC(digitalPinToTimer);
        RETURN_PIN_FUNC(analogInPinToBit);

        RETURN_PORT_FUNC(portModeRegister);
        RETURN_PORT_FUNC(portOutputRegister);
        RETURN_PORT_FUNC(portInputRegister);

        RETURN_GLOBAL_FUNC(totalPinCount);
        RETURN_GLOBAL_FUNC(readVcc);
    }
}

