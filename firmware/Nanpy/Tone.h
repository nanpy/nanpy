#ifndef TONE_H
#define TONE_H

class Tone {

    private:

        int pin;

    public:

        Tone(int pin) : pin(pin) {}
        void play(int note, int duration);
        void stop(void);

};

#endif