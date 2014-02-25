
/* FreqCount Library, for measuring frequencies
 * http://www.pjrc.com/teensy/td_libs_FreqCount.html
 * Copyright (c) 2011 PJRC.COM, LLC - Paul Stoffregen <paul@pjrc.com>
 *
 * Version 1.0
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

// FreqCount Library was so modified that it can be included in Nanpy

#include "cfg.h"
#if USE_Counter

#include "FreqCount.h"
#include "timers.h"

static uint16_t count_msw;
static uint32_t count_prev;
static volatile uint32_t count_output;
static volatile uint8_t count_ready;
static uint16_t gate_length;
static uint16_t gate_index;


void FreqCountClass::begin(uint16_t msec)
{
	if (msec < 10) return;
	gate_index = 0;
	count_msw = 0;
	count_prev = 0;
	count_ready = 0;
	counter_init();
	gate_length = timer_init(msec);
	uint8_t status = SREG;
	cli();
	timer_start();
	timer_isr_latency_delay();
	counter_start();
	SREG = status;
}

uint8_t FreqCountClass::available(void)
{
	return count_ready;
}

uint32_t FreqCountClass::read(void)
{
	uint32_t count;
	uint8_t status;

	status = SREG;
	cli();
	count = count_output;
	count_ready = 0;
	SREG = status;
	return count;
}

void FreqCountClass::end(void)
{
	timer_shutdown();
	counter_shutdown();
}


ISR(TIMER_ISR_VECTOR)
{
	uint16_t count_lsw;
	uint32_t count;
	uint16_t index, length;

	count_lsw = counter_read();
	if (counter_overflow()) {
		counter_overflow_reset();
		count_msw++;
	}
	index = gate_index + 1;
	length = gate_length;
	if (index >= length) {
		gate_index = 0;
		count = ((uint32_t)count_msw << 16) + count_lsw;
		count_output = count - count_prev;
		count_prev = count;
		count_ready = 1;
		restore_other_interrupts();
	} else {
		if (index == length - 1) disable_other_interrupts();
		gate_index = index;
	}
}


FreqCountClass FreqCount;


#endif
