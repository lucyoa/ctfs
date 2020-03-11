#!/usr/bin/env python

import requests
import time

"""
POST /api/v1/submissions HTTP/1.1
Host: 2019game.picoctf.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://2019game.picoctf.com/problems
Content-Type: application/json
X-CSRF-Token: 0478355b75a64fc897ebf7398f85f9af
X-Requested-With: XMLHttpRequest
Content-Length: 104
Connection: close
Cookie: _ga=GA1.2.1717347723.1569630945; _gid=GA1.2.1418283022.1569630945; token=0478355b75a64fc897ebf7398f85f9af; flask=.eJwNyjEKgDAMAMC_ZHYQk5jEz0hbExCxitRJ_LvefA_Mp197ql4bTO26vYN2bF5hgp5EkTkLp5GiqInnEDQN5bAU0MG9Ln80FjPvSyJUKgNmVeMF2YoEqQi8H2JHHYQ.XY6dJA.d1uFgcq9K7BYTD_-Yd_O3jYUoJQ

{"pid":"messy-malloc-0d46f25","key":"picoCTF{g0ttA_cl3aR_y0uR_m4110c3d_m3m0rY_5ed10d92}","method":"web"}
"""

with open("res", "r") as fp:
    i = 0
    for line in fp.readlines():
        i += 1
        if i % 5 == 0:
            time.sleep(30)

        flag = line.strip()
        print('-------')
        print(flag)
        data = {"pid":"messy-malloc-0d46f25","key":flag,"method":"web"}
        headers = {
            "Cookie": "_ga=GA1.2.1717347723.1569630945; _gid=GA1.2.1418283022.1569630945; token=0478355b75a64fc897ebf7398f85f9af; flask=.eJwNyjEKgDAMAMC_ZHYQk5jEz0hbExCxitRJ_LvefA_Mp197ql4bTO26vYN2bF5hgp5EkTkLp5GiqInnEDQN5bAU0MG9Ln80FjPvSyJUKgNmVeMF2YoEqQi8H2JHHYQ.XY6dJA.d1uFgcq9K7BYTD_-Yd_O3jYUoJQ",
            "X-CSRF-Token": "0478355b75a64fc897ebf7398f85f9af",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://2019game.picoctf.com/problems",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0"
        }

        response = requests.post("https://2019game.picoctf.com/api/v1/submissions", headers=headers, json=data)
        print(response.text)
        if "That is incorrect!" not in response.text:
            break
        time.sleep(10)
