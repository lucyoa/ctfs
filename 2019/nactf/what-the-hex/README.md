# What the HEX?

## Description
What the HEX man! My friend Elon just posted this message and I have no idea what it means >:( Please help me decode it:

https://twitter.com/kevinmitnick/status/1028080089592815618?lang=en

Leave the text format: no need to add nactf{} or change punctuation/capitalization

49 20 77 61 73 2e 20 53 6f 72 72 79 20 74 6f 20 68 61 76 65 20 6d 69 73 73 65 64 20 79 6f 75 2e

## Solution

Python one-liner:
```
"".join([chr(int(x, 16)) for x in "49 20 77 61 73 2e 20 53 6f 72 72 79 20 74 6f 20 68 61 76 65 20 6d 69 73 73 65 64 20 79 6f 75 2e".split()])
```

The flag is:
```
I was. Sorry to have missed you.
```
