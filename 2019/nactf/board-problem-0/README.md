# Dr. J's Group Test Randomizer: Board Problem #0

## Description
```
Dr. J created a fast pseudorandom number generator (prng) to randomly assign pairs for the upcoming group test. Leaf really wants to know the pairs ahead of time... can you help him and predict the next output of Dr. J's prng? Leaf is pretty sure that Dr. J is using the middle-square method.

nc shell.2019.nactf.com 31425

The server is running the code in class-randomizer-0.c. Look at the function nextRand() to see how numbers are being generated!
```

## Solution

Python script:
```
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
```

The flag is:
```
nactf{1_l0v3_chunky_7urn1p5}
```
