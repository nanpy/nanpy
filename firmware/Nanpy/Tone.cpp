#include "Tone.h"
#include <Arduino.h>

void Tone::play(int note, int duration) {
    #if defined(__AVR__)
        tone(pin, note, duration);
        delay(duration * 1.30);
        noTone(pin);
    #endif
}

void Tone::stop(void) {
    #if defined(__AVR__)
        noTone(pin);
    #endif
}