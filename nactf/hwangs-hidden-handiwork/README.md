# Hwang's Hidden Handiwork

## Description

Hwang was trying to hide secret photos from his parents. His mom found a text file with a secret string and an excel chart which she thinks could help you decrypt it. Can you help uncover Hwang's Handiwork?

Of course, the nobler of you may choose not to do this problem because you respect Hwang's privacy. That's ok, but you won't get the points.

## Solution

```python
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
```

The flag is:
```
nactf{g00gl3_15nt_s3cur3_3n0ugh}
```
