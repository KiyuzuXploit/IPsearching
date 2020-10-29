#!/bin/python

import requests, os, sys, time

def ulang():
  print('\033[90m[\033[92m?\033[90m] \033[97mGunakan Tools lagi?')
  ulg = input('\033[90m[\033[96my\033[96m/\033[96mt\033[90m] \033[96m•> ')
  if ulg == "y":
    time.sleep(1.1)
    os.system("python IPsearching.py")
  elif ulg == "t":
    time.sleep(1.1)
    print('\033[92m[\033[93m#\033[92m] \033[93mTerimakasih Telah menggunakan tools ini:)') 
    time.sleep(1.1)
    print('\033[97m[?] Keluar..')
    time.sleep(2.1)
    sys.exit()
  else:
    print("\033[91m[!] \033[97mHarap isi imput dengan benar:)")
    time.sleep(1.12)
    ulang()

banner = """\033[92m
╦╔═╗╔═╗╔═╗╔═╗╦═╗╔═╗╦ ╦╦╔╗╔╔═╗
║╠═╝╚═╗║╣ ╠═╣╠╦╝║  ╠═╣║║║║║ ╦
╩╩    ╚═╝╚═╝╩ ╩╩╚═╚═╝╩ ╩╩╝╚╝╚═╝
\033[96m•\033[90m===================================\033[96m•
 \033[90m{\033[96m•\033[90m} \033[92mAuthor \033[91m: \033[95mMr.Kiyuzu
 \033[90m{\033[96m•\033[90m} \033[92mFB     \033[91m: \033[95mYg Baca Pacarku
 \033[90m{\033[96m•\033[90m} \033[92mWA     \033[91m: \033[95m+62895344414334
\033[96m•\033[90m===================================\033[96m•"""
def bersih():
  os.system("clear")

def cekip():
 print(f'\033[90m[\033[96m!\033[90m] \033[92mMendapatkan IP..')
 time.sleep(2.1)
 re = requests.get('https://api.myip.com').json()
 ip = re['ip']
 print(f'\033[92m[\033[93m!\033[92m] \033[93mIP kamu \033[91m:\033[96m {ip}')
 time.sleep(1.1)
 ulang()
 
def lacakip():
 lacak = input('\033[92mMasukan IP target \033[91m:\033[96m')
 print(f'Melacak IP...')
 time.sleep (2.2)
 os.system('curl -s https://ip-api.com/'+lacak)
 ulang()

os.system("clear")
time.sleep(1.2)
print(banner)
time.sleep(1.2)
print ('Tools ini update an dari IPlocation')
time.sleep(1.2)
print('''    \033[1;0m\033[1;41mMENU PILIHAN\033[1;0m
\033[90m[\033[96m01\033[90m] \033[93mCek IP
\033[90m[\033[96m02\033[90m] \033[93mLacak IP
\033[90m[\033[96m00\033[90m] \033[93mEXIT
''')
menu = input('\033[90m[\033[96m?\033[90m] \033[92mSilahkan pilih menu \033[91m:\033[93m ')

if menu == '1':
 cekip()
elif menu == '2':
 lacakip()
elif menu == '00':
 time.sleep(1.1)
 print('\033[92m[\033[93m#\033[92m] \033[93mTerimakasih Telah menggunakan tools ini:)') 
 time.sleep(1.1)
 print('\033[97m[?] Keluar..')
 time.sleep(2.1)
 sys.exit()
else: 
 print('\033[91m[?] \033[97mPerintah tidak diketahui..')
 time.sleep(2.1)
 os.system("python IPsearching.py")