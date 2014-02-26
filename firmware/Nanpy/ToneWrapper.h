#ifndef TONE_WRAPPER_H
#define TONE_WRAPPER_H

namespace nanpy {
class ToneWrapper {

    private:

        int pin;

    public:

        ToneWrapper(int pin) : pin(pin) {}
        void play(int note, int duration);
        void stop(void);

};
}

#endif
