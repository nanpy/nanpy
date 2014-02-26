#include "cfg.h"

#if USE_Tone

#include "ToneWrapper.h"
#include <Arduino.h>

void nanpy::ToneWrapper::play(int note, int duration) {
    #if defined(__AVR__)
        tone(pin, note, duration);
        delay(duration * 1.30);
        noTone(pin);
    #endif
}

void nanpy::ToneWrapper::stop(void) {
    #if defined(__AVR__)
        noTone(pin);
    #endif
}

#endif
