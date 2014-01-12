#    sleep_after_connect=2 is required for most of the boards !


# custom board with 20MHz quartz and ATMEGA328P
# config = dict(
#     A0=14,
#     ARDUINO=105,
#     F_CPU=20000000.0,
#     MCU='__AVR_ATmega328P__',
#     avr_name='ATmega328P',
#     sleep_after_connect=0,
# )

# custom board with 16MHz quartz and ATMEGA328P
config = dict(
    A0=14,
    ARDUINO=105,
    F_CPU=16000000.0,
    MCU='__AVR_ATmega328P__',
    avr_name='ATmega328P',
    sleep_after_connect=0,
)


# Uno (not tested)
# config = dict(
#     A0=14,
#     ARDUINO=105,
#     F_CPU=16000000.0,
#     MCU='__AVR_ATmega328__',
#     avr_name='ATmega328',
#     sleep_after_connect=2,
# )
