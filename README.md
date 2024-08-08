# A BCC specific version for printing verifier log

## Something New

1. A new API `load_func_print` in the [init.py](src/python/bcc/__init__.py#L503) for printing verifier log: `load_func_print` is similar to `load_func` but passing the user-defined `log_buf` as parameters, so that when eBPF verifier outputs debugging info, `log_buf` can record all messages.

```python
def load_func_print(self, func_name, prog_type, log_buf, device = None, attach_type = -1)
```

2. An example [print_verifier_log.py](print_verifier_log.py) for testing

## How to install
using the `Source` way from [INSTALL.md](INSTALL.md), for example,
```shell
# For Focal (20.04.1 LTS)
sudo apt install -y zip bison build-essential cmake flex git libedit-dev \
  libllvm12 llvm-12-dev libclang-12-dev python zlib1g-dev libelf-dev libfl-dev python3-setuptools \
  liblzma-dev arping netperf iperf
  
git clone https://github.com/shenghaoyuan/bcc.git # replacing to my repo
mkdir bcc/build; cd bcc/build
cmake ..
make
sudo make install
cmake -DPYTHON_CMD=python3 .. # build python3 binding
pushd src/python/
make
sudo make install
popd  
```
## How to test
```shell
sudo python3 print_verifier_log.py

b'hello1'
func#0 @0
0: R1=ctx(id=0,off=0,imm=0) R10=fp0
0: (7b) *(u64 *)(r10 -8) = r1
1: R1=ctx(id=0,off=0,imm=0) R10=fp0 fp-8_w=ctx
1: (b7) r1 = 1
2: R1_w=inv1 R10=fp0 fp-8_w=ctx
2: (63) *(u32 *)(r10 -12) = r1
3: R1_w=inv1 R10=fp0 fp-8_w=ctx fp-16=mmmm????
3: (79) r1 = *(u64 *)(r10 -8)
4: R1_w=ctx(id=0,off=0,imm=0) R10=fp0 fp-8_w=ctx fp-16=mmmm????
4: (61) r1 = *(u32 *)(r1 +0)
5: R1_w=inv(id=0,umax_value=4294967295,var_off=(0x0; 0xffffffff)) R10=fp0 fp-8_w=ctx fp-16=mmmm????
5: (27) r1 *= 3
6: R1_w=inv(id=0,umax_value=12884901885,var_off=(0x0; 0x3ffffffff)) R10=fp0 fp-8_w=ctx fp-16=mmmm????
6: (61) r2 = *(u32 *)(r10 -12)
7: R1_w=inv(id=0,umax_value=12884901885,var_off=(0x0; 0x3ffffffff)) R2_w=inv(id=0,umax_value=4294967295,var_off=(0x0; 0xffffffff)) R10=fp0 fp-8_w=ctx fp-16=mmmm????
7: (0f) r2 += r1
8: R1_w=inv(id=0,umax_value=12884901885,var_off=(0x0; 0x3ffffffff)) R2_w=inv(id=0,umax_value=17179869180,var_off=(0x0; 0x3ffffffff)) R10=fp0 fp-8_w=ctx fp-16=mmmm????
8: (63) *(u32 *)(r10 -12) = r2
9: R1_w=inv(id=0,umax_value=12884901885,var_off=(0x0; 0x3ffffffff)) R2_w=inv(id=0,umax_value=17179869180,var_off=(0x0; 0x3ffffffff)) R10=fp0 fp-8_w=ctx fp-16=mmmm????
9: (61) r0 = *(u32 *)(r10 -12)
10: R0_w=inv(id=0,umax_value=4294967295,var_off=(0x0; 0xffffffff)) R1_w=inv(id=0,umax_value=12884901885,var_off=(0x0; 0x3ffffffff)) R2_w=inv(id=0,umax_value=17179869180,var_off=(0x0; 0x3ffffffff)) R10=fp0 fp-8_w=ctx fp-16=mmmm????
10: (95) exit
processed 11 insns (limit 1000000) max_states_per_insn 0 total_states 0 peak_states 0 mark_read 0

```


