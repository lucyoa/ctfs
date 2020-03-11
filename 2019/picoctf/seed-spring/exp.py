#!/usr/bin/env python

# RUN ON PICOCTF SERVER,
# otherwise its hard to sync

import subprocess
import random
from pwn import *

for j in range(0, 20):
    numbers = subprocess.check_output(["./numbers", str(j)]).split()
    try:
        r = remote("2019shell1.picoctf.com", 47241)
    except:
        continue

    r.recvuntil("Guess the height: ")
#    r = process("./seed_spring")

    for i in range(0, 30):
        r.sendline(numbers[i])
        data = r.recv(1024)
        if "WRONG!" in data:
            break
        else:
            print(data)
