# Off-base

## Description
It seems my friend Rohan won't stop sending cryptic messages and he keeps mumbling something about base 64. Quick! We need to figure out what he is trying to say before he loses his mind...

bmFjdGZ7YV9jaDRuZzNfMGZfYmE1ZX0=

## Solution

```
>>> import base64
>>> base64.b64decode('bmFjdGZ7YV9jaDRuZzNfMGZfYmE1ZX0=')
'nactf{a_ch4ng3_0f_ba5e}'
```

The flag is:
```
nactf{a_ch4ng3_0f_ba5e}
```
