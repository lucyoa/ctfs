# Vyom's Soggy Croutons

## Description
Vyom was eating a CAESAR salad with a bunch of wet croutons when he sent me this:

ertkw{vk_kl_silkv}

Can you help me decipher his message?

## Solution
It's a caesar cipher. More information can be found at `https://en.wikipedia.org/wiki/Caesar_cipher`

We need to figure out what is the rotation to decode the cipher `ertkw{vk_kl_silkv`. For that simple python script can be used:

```python
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
```

Results:
```
ylneq{pe_ef_mcfep}
zmofr{qf_fg_ndgfq}
anpgs{rg_gh_oehgr}
boqht{sh_hi_pfihs}
cpriu{ti_ij_qgjit}
dqsjv{uj_jk_rhkju}
ertkw{vk_kl_silkv}
fsulx{wl_lm_tjmlw}
gtvmy{xm_mn_uknmx}
huwnz{yn_no_vlony}
ivxoa{zo_op_wmpoz}
jwypb{ap_pq_xnqpa}
kxzqc{bq_qr_yorqb}
lyard{cr_rs_zpsrc}
mzbse{ds_st_aqtsd}
nactf{et_tu_brute}
obdug{fu_uv_csvuf}
pcevh{gv_vw_dtwvg}
qdfwi{hw_wx_euxwh}
regxj{ix_xy_fvyxi}
sfhyk{jy_yz_gwzyj}
tgizl{kz_za_hxazk}
uhjam{la_ab_iybal}
vikbn{mb_bc_jzcbm}
wjlco{nc_cd_kadcn}
```

The flag is:
```
nactf{et_tu_brute}
```
