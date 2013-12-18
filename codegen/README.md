Code generation
================

C code is generated for AVR type and registers.
All information is parsed from AVR Libc header files.

dependencies:

 - path.py  
 - AVR Libc (http://www.nongnu.org/avr-libc/)

    sudo apt-get install python-pip avr-libc
    sudo pip install path.py

running from project directory:

	python codegen/__init__.py

generated files:

 - firmware/Nanpy/generated_mcu.h
 - firmware/Nanpy/generated_avr_registers.h


generated_mcu.h
-----------------

This is a list of all known AVR types, "MCU" is defined to the type name.
Example: 

	#ifdef __AVR_ATmega328P__
	#    ifdef MCU
	#        error "MCU is already defined"
	#    endif
	#    define MCU "__AVR_ATmega328P__"
	#endif
	
generated_avr_registers.h
---------------------------
This is a list of all known register names.
Example: 

	#ifdef DDRB
		DEFINE(DDRB)
	#else
		MISSING(DDRB)
	#endif
