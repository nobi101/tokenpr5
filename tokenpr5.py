dem = 0
import requests, threading
import os, sys
from time import sleep
from datetime import datetime
from pystyle import Write,Colors
try:
	import requests,pystyle
except:
	Write.Print (luc + "Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải \n",Colors.blue_to_red,interval=0.0001)
	os.system('pip install requests && pip install bs4 && pip install pystyle')
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    Write.Print('──────────────────────────────────────────────────────\n',Colors.blue_to_red,interval=0.0001)
clear()
token = Write.Input('Vui Lòng Nhập Token Facebook: ',Colors.blue_to_red,interval=0.0001)
thanh()
file_save = Write.Input('Vui Lòng Nhập Tên File Muốn Lưu: ',Colors.blue_to_red,interval=0.0002)
thanh()
get_token = requests.get('https://graph.facebook.com/me/accounts?access_token='+token).json()['data']
# RUN
for get in get_token:
    time = datetime.now().strftime("%H:%M:%S")
    dem = dem+1
    tokenpro5 = get['access_token']
    namepro5 = get["name"]
    idpro5 = get['id']
    Write.Print(f'[{dem}] | {time} | SUCCESS  | {idpro5} | {namepro5} | {tokenpro5} |\n',Colors.blue_to_red,interval=0.0001)
    #print('['+str(dem)'] | '+str(time)' | SUCCESS  | '+str(idpro5)' | '+str(namepro5)' | '+str(tokenpro5)+'')
    thanh()
    open(f'{file_save}', "a+").write(f'{tokenpro5}\n')
Write.Print(f'[SUCCESS]: Đã Lưu Thành Công Vào File, {file_save}\n',Colors.blue_to_red,interval=0.0001)
#print('[SUCCESS]: Đã Lưu Thành Công Vào File, '+file_save+' ')
