#include "cfg.h"

#if USE_ArduinoCore

#include <Arduino.h>
#include "ArduinoCoreClass.h"
#include <stdlib.h>

#define RETURN_PIN_FUNC(x)         if (strcmp(m->getName(), #x) == 0) { m->returns(x(m->getInt(0))); }
#define RETURN_PORT_FUNC(x)        if (strcmp(m->getName(), #x) == 0) { m->returns((uint16_t)x(m->getInt(0))); }

const char* nanpy::ArduinoCoreClass::get_firmware_id()
{
    return "Core";
}

void nanpy::ArduinoCoreClass::elaborate(nanpy::MethodDescriptor* m)
{
    RETURN_PIN_FUNC(digitalPinToBitMask);
    RETURN_PIN_FUNC(digitalPinToPort);
    RETURN_PIN_FUNC(digitalPinToTimer);
    RETURN_PIN_FUNC(analogInPinToBit);

    RETURN_PORT_FUNC(portModeRegister);
    RETURN_PORT_FUNC(portOutputRegister);
    RETURN_PORT_FUNC(portInputRegister);
}

#endif
