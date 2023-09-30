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
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
# đánh dấu bản quyền
ndp_tool = "\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
# # Config
# __ZALO__ = 'lỏ'
# __ADMIN__ = 'HIẾU_TOOL'
# __FACEBOOK__ = 'NOT'
# __VERSION__ = '0.0'


# def banner():
#     banner = f"""
# \033[0m───────────────────────────────────────────────────────────
# \033[1;34m  *********************** HIẾU TOOL *********************
# \033[0m───────────────────────────────────────────────────────────
# """
#     for X in banner:
#         sys.stdout.write(X)
#         sys.stdout.flush()
#         sleep(0.00125)


# # =======================[ NHẬP KEY ]=======================
# os.system("cls" if os.name == "nt" else "clear")
# banner()
# time = datetime.now()
# a = time.strftime("%d")
# h = int(time.strftime("%d"))
# ngày_trc = h-1
# b = time.strftime("%m")
# day = time.strftime("%d-%m-%Y")
# today = time.strftime("%d-%m-%Y")
# d = time.strftime("%d-%m")
# encodedBytes = base64.b64encode(d.encode("utf-8"))
# key = str(encodedBytes, "utf-8")
# long_url = (f"https://keyvip24h.net/giaodien/key.php?key={key}")
# api_token = '3cb519b30f0bf1cc2a37e10fdf9545c0b56d6465'
# url = requests.get(
#     f'https://link1s.com/api?api={api_token}&url={long_url}').json()
# status = url['status']
# link = url['shortenedUrl']
# # lấy key
# file_key = f'key-ngày{a}.txt'
# file_key_cũ = f'key-ngày{ngày_trc}.txt'
# check_file_key = os.path.exists(file_key)
# if check_file_key == False:
#     print(f"{ndp_tool}{luc}Đây Là Tool Free Nên Key Sẽ Thay Đổi Mỗi Ngày !!")
#     print(f'{ndp_tool}{luc}Truy Cập Vào Link{trang}: {link} {luc}Để Lấy Key Miễn Phí')
#     print(thanh)
#     while (True):
#         ma = input(
#             f"{ndp_tool}{luc}Nhập API Key\033[1;32m Ngày \033[1;37m{today}: \033[1;33m")
#         if ma == key:
#             print(f'{ndp_tool}{luc}API Key Chính Xác')
#             luu = open(file_key, 'a+')
#             luu.write(ma)
#             luu.close()
#             break
#         elif ma != key:
#             print(f'{ndp_tool}{do}API Key Sai')
# elif check_file_key == True:
#     print(f'{ndp_tool}{luc}Đang Lấy Key...', end='\r')
#     sleep(2)
#     k = open(file_key, 'r')
#     ma = k.read()
#     k.close()
#     if ma == key:
#         print(f'{ndp_tool}{luc}Lấy Key Thành Công       ', end='\r')
#         sleep(0)
#     elif ma != key:
#         if os.path.exists(file_key_cũ) == True:
#             os.system(f'rm {file_key_cũ}')
#         os.system(f'rm {file_key}')
#         print(f'{ndp_tool}{do}API Key Sai         ')
#         while (True):
#             ma = input(
#                 f"{ndp_tool}{luc}Nhập API Key\033[1;32m Ngày \033[1;37m{today}: \033[1;33m")
#             if ma == key:
#                 print(f'{ndp_tool}{luc}API Key Chính Xác')
#                 luu = open(file_key, 'a+')
#                 luu.write(ma)
#                 luu.close()
#                 break
#             elif ma != key:
#                 print(f'{ndp_tool}{do}API Key Sai           ')

# # ======================== [ HOME TOOL ] ========================

os.system("cls" if os.name == "nt" else "clear")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Trao Đổi Sub  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool TDS FB FULL JOD ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool TDS FB VIP")

print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool TDS Pro5")
# print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTool TDS Pro5 \033[1;31m[\033[1;33mV2\033[1;31m] ")

print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;32mTool TDS TikTok & TDS TIKTOK NOW ")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═══════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tương Tác Chéo  \033[1;37m║")
print("\033[1;37m╚═══════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;32mTool TTC TikTok ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;32mTool TTC Pro5 ")


print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tiện Ích      \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;32mTool Đào Mail ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;32mTool Tạo Thẻ Thanh Toán ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m10\033[1;31m] \033[1;32mTool Check Valid")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m11\033[1;31m] \033[1;32mTool Check Ngày Tạo Acc FB")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m13\033[1;31m] \033[1;32mTool Spam-sms")


print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool PROFILE       \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m14\033[1;31m] \033[1;32mTool Reg Page Pro5")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m15\033[1;31m] \033[1;32msharefb")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m16\033[1;31m] \033[1;32mTool Reg Page Pro5 \033[1;31m[\033[1;33mV2\033[1;31m]")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m17\033[1;31m] \033[1;32mTOOL TĂNG SHARE AO BẰNG TOKEN")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m18\033[1;31m] \033[1;32mTool Buff View Story Max Speed Pro5 ")

print("\033[1;31m────────────────────────────────────────────────────────────")

print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool mới cập nhật  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m20\033[1;31m] \033[1;32mtool spam sms\033[1;31m[\033[1;33mV5\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m19\033[1;31m] \033[1;32mThoát Tool")
print("\033[1;31m────────────────────────────────────────────────────────────")

chon = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
#tool tds
if chon == 1 :
	exec(requests.get('https://run.mocky.io/v3/6f026b34-572d-4fdb-b6a2-76492bb73a32').text) 
if chon == 2:
	exec(requests.get('https://run.mocky.io/v3/b452f892-505d-4481-b043-e320b0217053').text)
if chon == 3 :
	exec(requests.get('https://run.mocky.io/v3/956f97cd-10d8-4b85-8cf9-42ec97d4674b').text) 
if chon == 4 :
	exec(requests.get('').text) 
elif chon == 5 : 
 exec(requests.get('https://run.mocky.io/v3/30e697ca-46ff-4516-b99f-2fba9ad55670').text) 
 
 
 #tool ttc
if chon == 6 :
	exec(requests.get('https://run.mocky.io/v3/ecb8ffa6-c3d3-4375-8e70-eee76c651590').text)
if chon == 7 :
	exec(requests.get('https://run.mocky.io/v3/5b26d318-842a-410d-9459-b9ba0cc446f6').text)

#tool công cụ 
elif chon == 8 :
 exec(requests.get('https://run.mocky.io/v3/4a04c1b4-e556-42fa-ab56-627cc1f46cea').text)
elif chon == 9 :
 exec(requests.get('https://run.mocky.io/v3/e1cb6200-5193-424f-9b60-a663e761d861').text)
if chon == 10 :
	exec(requests.get('https://run.mocky.io/v3/a8b7d110-4b72-4b36-a1f3-203d47125ff1').text)
if chon == 11 :
	exec(requests.get('https://run.mocky.io/v3/d7a8b3bf-737a-4cde-a032-5153d31dcb39').text)
if chon == 12 :
	exec(requests.get('https://run.mocky.io/v3/765d1f9e-82e0-468c-9ab6-33bed63ec01a').text)
if chon == 13 :
	exec(requests.get('https://run.mocky.io/v3/765d1f9e-82e0-468c-9ab6-33bed63ec01a').text)
if chon == 14 :
	exec(requests.get('https://run.mocky.io/v3/5b238244-de40-40c3-99ce-e0adee6808cc').text)	
if chon == 15 :
	exec(requests.get('https://run.mocky.io/v3/13a2a17b-521d-4470-9ea2-70b53bdea2b0').text)
if chon == 16 :
	exec(requests.get('https://run.mocky.io/v3/7ac4aa31-751d-46b0-bea7-fffe315f6219').text)
if chon == 17 :
	exec(requests.get('https://run.mocky.io/v3/11b0b7ed-e305-443a-9e08-e95c7e074933').text)
if chon == 18 :
	exec(requests.get('https://run.mocky.io/v3/f03a1dea-6c77-4609-9aab-26cfb79255e8').text)
if chon == 19 :
	exec(requests.get('https://run.mocky.io/v3/d04b932d-a0d5-4a42-b10c-aba744c6a88d').text)
if chon == 20 :
	exec(requests.get('https://run.mocky.io/v3/98beb54f-1afb-4f8d-9357-d3b63faa8028').text)
else :
     exit()
