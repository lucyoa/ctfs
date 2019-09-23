#!/usr/bin/env python

import re
from pwn import *

seed = 0

def get_digits(seed, start, end):
    seed = str(seed)
    return int(seed[len(seed)-end: len(seed)-start+1])

def nextRand():
    global seed

    seed = get_digits(seed, 5, 12)
    seed *= seed
    return seed

r = remote("shell.2019.nactf.com", 31425)
r.recvuntil("> ")
r.sendline("r")
data = r.recvuntil("> ")
seed = re.search("([0-9]+)", data).group(1)
print(seed)

nextRand()
r.sendline("g")
r.recvuntil("> ")
r.sendline(str(seed))
r.recvuntil("> ")

nextRand()
r.sendline(str(seed))
print(r.recvall())
