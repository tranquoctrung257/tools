from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep
black='\033[1;90m'
pink='\033[1;97m'
red='\033[1;91m'
green='\033[1;92m'
blue='\033[1;96m'
yellow='\033[1;93m'
pinkx='\033[7;37m\033[1;37m'
pink='\033[1;95m'
redb='\033[7;37m\033[1;91m'
redz='\033[1;41;97m'
end='\033[0m'
hquantool=pink+'['+blue+'Hiếu-Tool'+pink+']'
hquantool_no_pro=pinkx+'[Hiếu-Tool]'+end
hln=pink+"["+blue+"Hiếu-Tool"+pink+"]"
sadboiz=pink+"["+blue+"Hiếu-Tool"+pink+"]"
def logo():
    log="""        
\033[1;34m ██╗░░██╗██╗███████╗██╗░░░██╗ ████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;37m ██║░░██║██║██╔════╝██║░░░██║ ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;34m ███████║██║█████╗░░██║░░░██║ ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;37m ██╔══██║██║██╔══╝░░██║░░░██║ ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;34m ██║░░██║██║███████╗╚██████╔╝ ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;37m ╚═╝░░╚═╝╚═╝╚══════╝░╚═════╝░ ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;33mTool TDS FB VIP 
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mHiếu Tool
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32m SUPPORT: \033[1;37m 84939271874
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;34mYOUTUBE: \033[1;37mhttps://www.youtube.com/@hieutool248
\033[1;31m────────────────────────────────────────────────────────────
"""
    os.system('clear')  
    for h in log:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.001)
logo()
while(True):
        token_tds=input(pink+'\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP ACCESS_TOKEN TDS: \033[1;33m')
        print("\033[1;31m────────────────────────────────────────────────────────────")
        ttacc=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+str(token_tds))
        if 'error' in ttacc.text:print(red+ttacc.json()['error'].upper())
        if 'success' in ttacc.text:
                user=ttacc.json()['data']['user']
                xu=ttacc.json()['data']['xu']
                xu_die=ttacc.json()['data']['xudie']
                print(pink+''+blue+'\033[1;92mTên Tài Khoản TDS : '+pink+user.upper()+blue+'')
                sleep(1)
                print("\033[1;31m────────────────────────────────────────────────────────────")
                break
while(True):
        while(True):
                while(True):
                        ck_fb=input(blue+'\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP COOKIE FACEBOOK: \033[1;33m')
                        os.system("clear")
                        if ck_fb=='':break
                        u_check='https://mbasic.facebook.com/profile.php'
                        h={'cookie':ck_fb}
                        check=requests.get(url=u_check,headers=h).text
                        try:
                                name=check.split('<title>')[1].split('</title>')[0]
                                id_fb=ck_fb.split('c_user=')[1].split(';')[0]
                                print(f'[SUCCESS-NAME:{name}][COOKIE LIVE]')
                                sleep(2)
                                break
                        except:
                                print(sadboiz,pink+'['+red+'COOKIE FACEBOOK DIE'+pink+']')
                if ck_fb=='':
                        print(blue+'THANKS BẠN ĐÃ SỬ DỤNG TOOL CỦA',sadboiz+' !')
                        quit()
                logo()
                u_run='https://traodoisub.com/api/?fields=run&id='+id_fb+'&access_token='+token_tds
                print(pink+'['+blue+'ĐANG'+pink+' CẤU HÌNH'+blue+' ID: '+pink+id_fb+blue+']')
                run=requests.get(url=u_run)
                if 'success' in run.text:
                        print(hquantool,'['+run.json()['data']['msg'].upper()+']')
                        sleep(0.5)
                        break
                else:
                        print(red+run.json()['error'].upper())
        logo()
        stop=int(input(pink+'NHẬP '+blue+'SỐ NHIỆM VỤ: '+pink))
        delay=int(input(blue+'NHẬP '+pink+'DELAY: '+green))
        s=0
        logo()
        while(True):
                print(hquantool,' Đợi Giây Lát',end="\r")
                while(True):
                        try:
                                list_nv=requests.get('https://traodoisub.com/api/?fields=reaction&access_token='+token_tds)
                                if 'id' in list_nv.text:break
                        except:
                                print(hquantool_no_pro+pink+'['+red+'INTERNET KHÔNG ỔN ĐỊNH !!!'+pink+']','               ',end='\r')
                for x in range(0,len(list_nv.json())):
                        try:
                                id_post=list_nv.json()[x]['id']
                                type_post=list_nv.json()[x]['type']
                                if str(type_post)=='LIKE':
                                        type_rect='LIKE'
                                        v=1
                                if str(type_post)=='LOVE':
                                        type_rect='LOVE '
                                        v=2
                                if str(type_post)=='CARE':
                                        type_rect='CARE '
                                        v=3
                                if str(type_post)=='HAHA':
                                        type_rect='HAHA '
                                        v=4
                                if str(type_post)=='WOW':
                                        type_rect='WOW  '
                                        v=5
                                if str(type_post)=='SAD':
                                        type_rect='SAD  '
                                        v=6
                                if str(type_post)=='ANGRY':
                                        type_rect='ANGRY'
                                        v=7
                                host='https://mbasic.facebook.com'
                                u=host+'/reactions/picker/?is_permalink=1&ft_id='+id_post
                                h={'cookie':ck_fb}
                                check=requests.get(url=u,headers=h).text
                                if 'Trước tiên, bạn phải đăng nhập.' in check:
                                        break
                                if 'Phẫn nộ' in check:
                                        cx=BeautifulSoup(check,'html.parser')
                                        type_cx=cx.find_all('a')
                                        u_cx=host+str(type_cx[v]['href'])
                                        rect=requests.get(url=u_cx,headers=h).text
                                        #print(rect)
                                        #1like_2tym_3thuongthuong_4haha
                                        #5wow_6sad_7phanno
                                nhan_tien=requests.get('https://traodoisub.com/api/coin/?type='+type_post+'&id='+id_post+'&access_token='+token_tds)
                                if 'success' in nhan_tien.text:
                                        s=s+1
                                        xu=str(nhan_tien.json()['data']['xu'])
                                        msg=str(nhan_tien.json()['data']['msg']).upper()
                                        time=datetime.now().strftime("%H:%M:%S")
                                        print(hquantool_no_pro+pink+'['+blue+str(s)+pink+']['+time+']['+blue+type_rect+pink+']['+blue+msg+pink+']['+blue+xu+pink+']','     ')
                                        if s==stop:break
                                        for a in range(delay,0,-1):
                                                print(hquantool,'['+blue+str(a)+pink+']','     ',end='\r')
                                                sleep(0.7)
                        except:
                                print(hquantool_no_pro+pink+'['+red+'INTERNET KHÔNG ỔN ĐỊNH !!!'+pink+']','               ',end='\r')
                if s==stop:break
                if 'Trước tiên, bạn phải đăng nhập.' in check:
                                        print(hquantool_no_pro+pink+'['+red+'COOKIE FACEBOOK DIE'+pink+']','                    ')
                                        break
        print(hquantool+pink+'[DỪNG TOOL ẤN'+blue+' ENTER !!!'+pink+']')
        ttacc=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+str(token_tds)).json()
        if s==stop:print(hquantool_no_pro+pink+'[CHẠY TOOL SUCCESS, TỔNG XU:',yellow+str(ttacc['data']['xu'])+']')
