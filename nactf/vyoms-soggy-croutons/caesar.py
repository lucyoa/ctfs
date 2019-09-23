#!/usr/bin/env python

cipher = "ertkw{vk_kl_silkv}"

for i in range(1, 26):
    res = ""
    for c in cipher:
        if c not in ("{", "}", "_"):
            res += chr(ord('a') + ((ord(c) + i) % 26))
        else:
            res += c

    print(res)
