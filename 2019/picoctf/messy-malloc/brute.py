import string

flag = "picoCTF{g0ttA_cl3aR_y0uR_m4110c3d_m3m0rY_5ed10d"

for i in "abcdef" + string.digits:
    for j in "abcdef" + string.digits:
        print(flag + i + j + "}")
