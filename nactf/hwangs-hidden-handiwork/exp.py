#!/usr/bin/env python

cipher = {}

with open("substituion.csv", "r") as f:
    plaintext_letters = f.readline().strip().split(",")[1:]
    cipher_letters = f.readline().strip().split(",")[1:]

    for i in range(0, len(cipher_letters)):
        cipher[cipher_letters[i]] = plaintext_letters[i]

res = ""
with open("hwangshandiwork.txt","r") as f:
    content = f.read().strip()
    print(content)
    for f in content:
        res += cipher[f]

    print(res)
