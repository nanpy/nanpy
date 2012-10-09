#!/usr/bin/env python

# Author: Andrea Stagi <stagi.andrea@gmail.com>
# Description: play a melody
# Dependencies: None

from nanpy import Tone

melody = [[Tone.NOTE_C4, 4], [Tone.NOTE_G3, 8], [Tone.NOTE_G3, 8], 
            [Tone.NOTE_A3, 4], [Tone.NOTE_G3, 4], [0, 4], 
            [Tone.NOTE_B3, 4], [Tone.NOTE_C4, 4]]

tone = Tone(4)

for note in melody:
    tone.play(note[0] , 1000/note[1])

