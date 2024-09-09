#!/usr/bin/python3
# Copyright (c) PLUMgrid, Inc.
# Licensed under the Apache License, Version 2.0 (the "License")

# run in project examples directory with:
# sudo python3 print_verifier_log.py"

from bcc import BPF
import ctypes as ct

# example 1
program = r"""
unsigned array_sum(void* ctx) {
  unsigned a [10] = {0}, sum = 0;
  for (int i = 0; i < 10; i++){
    a[i] = 100+i*10;
  }
  
  for (int j = 9; j >= 0; j--){
    sum += a[j];
  }
  return sum;
}
"""

# normally, we should set debug=0x10 to `Debug output register state on all instructions`, but for my bcc variant, it should be useless, but keep it, safely
b = BPF(text=program, cflags=["-O0"], debug=0x10)

# create a buffer to store the verifier debug info
log_buf = ct.create_string_buffer(1000000)

# load binary code, then use bpf verifier checking and record all static analysis info. It should be fine if `BPF.KPROBE` is replaced with other types?
fn = b.load_func_print(b"array_sum", BPF.KPROBE, log_buf)

# print `b"hello1"`
print(fn.name)

# original bpf binary? 
# print(fn.bpf)

# print the verifier debug info
print(log_buf.value.decode('utf-8'))

# may be useless
b.trace_print()

