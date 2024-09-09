#!/usr/bin/python3
# Copyright (c) PLUMgrid, Inc.
# Licensed under the Apache License, Version 2.0 (the "License")

# run in project examples directory with:
# sudo python3 print_verifier_log.py"

from bcc import BPF
import ctypes as ct


# example 4
program = r"""
struct fletcher32_ctx {
  const unsigned short * data;
  uint32_t words;
};

uint32_t fletcher32(struct fletcher32_ctx * ctx)
{
    uint32_t sum1 = 0xffff, sum2 = 0xffff, sumt = 0xffff, words = (*ctx).words;
    const uint16_t *data = (*ctx).data;

    while (words) {
        unsigned tlen = words > 359 ? 359 : words;
        words -= tlen;
        do {
            sumt = sum1;
            sum2 += sum1 += *data++;
        } while (--tlen);
        sum1 = (sum1 & 0xffff) + (sum1 >> 16);
        sum2 = (sum2 & 0xffff) + (sum2 >> 16);
    }
    sum1 = (sum1 & 0xffff) + (sum1 >> 16);
    sum2 = (sum2 & 0xffff) + (sum2 >> 16);
    return (sum2 << 16) | sum1;
}
"""

# normally, we should set debug=0x10 to `Debug output register state on all instructions`, but for my bcc variant, it should be useless, but keep it, safely
b = BPF(text=program, cflags=["-O1"], debug=0x10)

# create a buffer to store the verifier debug info
log_buf = ct.create_string_buffer(65536)

# load binary code, then use bpf verifier checking and record all static analysis info. It should be fine if `BPF.KPROBE` is replaced with other types?
fn = b.load_func_print(b"fletcher32", BPF.KPROBE, log_buf)

# print `b"hello1"`
print(fn.name)

# original bpf binary? 
# print(fn.bpf)

# print the verifier debug info
print(log_buf.value.decode('utf-8'))

# may be useless
b.trace_print()

