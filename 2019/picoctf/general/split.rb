
split = 4

checkpass = "a" * split * 8
checkpass[0..3] = 'pico'
checkpass[split*6..split*7-1] = '4454'
checkpass

checkpass[split..split*2-1] = 'CTF{'
checkpass[split*4..split*5-1] = 'ts_p'
checkpass[split*3..split*4-1] = 'lien'
checkpass[split*5..split*6-1] = 'lz_2'
checkpass[split*2..split*3-1] = 'no_c'
checkpass[split*7..split*8-1] = 'a}'
print checkpass

