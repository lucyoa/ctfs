#!/usr/bin/env python

from pwn import *

import sys
import re

context(arch = 'x86_64', os = 'linux')
r = remote('2019shell1.picoctf.com',31615)

line = r.recvuntil("Input:")
regex = re.compile(r'([0|1]+)', re.MULTILINE)
result = regex.findall(line)
solv = ''
for binlol in result:
    num = int(binlol, 2)
    solv += chr(num)
r.send(solv)
r.send("\n")

line = r.recvuntil("Input:")
regex = re.compile(r'([\d]+)', re.MULTILINE)
result = regex.findall(line)

solv = ''
for binlol in result:
    num = int(binlol, 8)
    solv += chr(num)

if len(solv) > 0:
    r.send(solv)
    r.send("\n")

line = r.recvuntil("Input:")
regex = re.compile(r'^Please give me the (.*?) as a word.$', re.MULTILINE)
result = regex.findall(line)
solv = result[0].decode("hex")
r.send(solv)
r.send("\n")

r.interactive()
r.close()
exit(1)


