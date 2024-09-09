#!/usr/bin/python3
# Copyright (c) PLUMgrid, Inc.
# Licensed under the Apache License, Version 2.0 (the "License")

# run in project examples directory with:
# sudo python3 print_verifier_log.py"

from bcc import BPF
import ctypes as ct

# example 1
program = r"""
int fibonacci(int n) {
    if(n == 0) {
        return 0;
    } else if(n == 1) {
        return 1;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}
"""

# example 2
'''
program = r"""
int fibonacci(int n) {
    if(n <= 1) {
        return n;
    }
    int a = 0, b = 1;
    for(int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}
"""
'''

# example 3
'''
program = r"""
unsigned int fibonacci(unsigned int* n) {
    if(*n <= 1) {
        return *n;
    }
    unsigned int a = 0, b = 1;
    for(int i = 2; i <= *n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}
"""
'''

# example 4
'''
program = r"""
unsigned int fibonacci(void * ctx) {
    unsigned int a = 0, b = 1;
    for(int i = 2; i <= 3; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}
"""
'''

# normally, we should set debug=0x10 to `Debug output register state on all instructions`, but for my bcc variant, it should be useless, but keep it, safely
b = BPF(text=program, cflags=["-O0"], debug=0x10)

# create a buffer to store the verifier debug info
log_buf = ct.create_string_buffer(10000000) # 2^20 = 1048576

# load binary code, then use bpf verifier checking and record all static analysis info. It should be fine if `BPF.KPROBE` is replaced with other types?
fn = b.load_func_print(b"fibonacci", BPF.KPROBE, log_buf)

# print `b"hello1"`
print(fn.name)

# original bpf binary? 
# print(fn.bpf)

# print the verifier debug info
print(log_buf.value.decode('utf-8'))

#output_file_path = 'fib_buf_log.txt'
#with open(output_file_path, 'w', encoding='utf-8') as file:
#    file.write(log_buf)

# may be useless
#b.trace_print()

