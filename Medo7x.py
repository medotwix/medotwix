#Coded By Mohamed habeb Musa 
#Twitter : @@zOalMoShAgEp
#Sate !
#Sate !
#Sate !
import random 
import string
import  re, os,time,getpass,sys
from platform import system
from random import choice
B = '\033[0;34m'
R = '\033[1;31m'
Y = '\033[0;33m'
######## Clear Terminal Or cmd ########
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
######## Work ########
def steam() :
 print("""  Steam Generator (c) Medo7x """)
 zz=input('Enter Number Keys > ')
 try :
   for az in range(int(zz)) :
    urname = string.ascii_letters + string.digits
    urname1 = ''.join(choice(urname) for _ in range(5))
    taki = string.ascii_letters + string.digits
    taki2 = ''.join(choice(taki) for _ in range(5))
    metsuha = string.ascii_letters + string.digits
    metsuha3 = ''.join(choice(metsuha) for _ in range(5)) 
    mark = urname1.upper() +('-')+ taki2.upper() +('-')+ metsuha3.upper()
    print(az+1,")",mark," by M7X")
    save = open("steam.txt", 'a')
    save.write(mark + '\n')
   print("Continue ? [Y/N(yes/No)] ")
   so=input("> ")
   if so =='y' or so =='Y':
    main()
   else:
    exit()
 except : 
	   	 pass
def hma() :
 print("""  Hidemyass Generator (c) Medo7x """)
 zz=input('Enter Number Keys > ')
 try :
   for az in range(int(zz)) :
    urname = string.ascii_letters + string.digits
    urname1 = ''.join(choice(urname) for _ in range(6))
    taki = string.ascii_letters + string.digits
    taki2 = ''.join(choice(taki) for _ in range(6))
    metsuha = string.ascii_letters + string.digits
    metsuha3 = ''.join(choice(metsuha) for _ in range(6)) 
    mark = urname1.upper() +('-')+ taki2.upper() +('-')+ metsuha3.upper()
    print(az+1,")",mark," by M7X")
    save = open("hma.txt", 'a')
    save.write(mark + '\n')
   so=input("Continue ? [Y/N(yes/No)] > ")
   if so =='y' or so =='Y':
        main()
   else:
        exit()
 except : 
	   	 pass
def g2a() :
  print("""  G2A Generator (c) Medo7x """)
  zz=input('Enter Number Keys > ')
  try :
   for az in range(int(zz)) :
    urname = string.ascii_letters + string.digits
    urname1 = ''.join(choice(urname) for _ in range(4))
    taki = string.ascii_letters + string.digits
    taki2 = ''.join(choice(taki) for _ in range(4))
    metsuha = string.ascii_letters + string.digits
    metsuha3 = ''.join(choice(metsuha) for _ in range(4)) 
    mark = urname1.upper() +('-')+ taki2.upper() +('-')+ metsuha3.upper()
    print(az+1,")",mark," by M7X")
    save = open("g2a.txt", 'a')
    save.write(mark + '\n')
   so=input("Continue ? [Y/N(yes/No)] > ")
   if so =='y' or so =='Y':
        main()
   else:
        exit()
  except : 
	   	 pass
	   	
def gplay() :
 print("""  Googleplay Generator (c) Medo7x """)
 zz=input('Enter Number Keys > ')
 int(zz)
 try :
   for az in range(int(zz)) :
    urname = string.ascii_letters + string.digits
    urname1 = ''.join(choice(urname) for _ in range(4))
    taki = string.ascii_letters + string.digits
    taki2 = ''.join(choice(taki) for _ in range(4))
    metsuha = string.ascii_letters + string.digits
    metsuha3 = ''.join(choice(metsuha) for _ in range(4))
    miki = string.ascii_letters + string.digits
    miki3 = ''.join(choice(miki) for _ in range(4))
    tsukaza = string.ascii_letters + string.digits
    tsukaza3 = ''.join(choice(tsukaza) for _ in range(4))
    mark = urname1.upper() +('-')+ taki2.upper() +('-')+ metsuha3.upper() +('-')+ miki3.upper() +('-')+ tsukaza3.upper()
    print(az+1,")",mark," by M7X")
    save = open("gplay.txt", 'a')
    save.write(mark + '\n')
   so=input("Continue ? [Y/N(yes/No)] > ")
   if so =='y' or so =='Y':
        main()
   else:
        exit()
 except : 
	   	 pass
def express() :
 print("""  Express Vpn Generator (c) Medo7x """)
 zz=input('Enter Number Keys > ')
 try :
   for az in range(int(zz)) :
    urname = string.ascii_letters + string.digits
    urname1 = ''.join(choice(urname) for _ in range(22))
    print(az+1,")","E"+ urname1.upper()," by M7X")
    save = open("express.txt", 'a')
    save.write(urname1 + '\n')
   so=input("Continue ? [Y/N(yes/No)] > ")
   if so =='y' or so =='Y':
        main()
   else:
        exit()
 except : 
	   	 pass
def karta() :
 print("""  7ammass Generator (c) Medo7x """)
 zz=input('Enter Number Keys > ')
 try :
   for az in range(int(zz)) :
    gothar = string.digits
    gothar69 = ''.join(choice(gothar) for _ in range(14))
    print(az+1,")",gothar69," by M7X")
    save = open("karta.txt", 'a')
    save.write(gothar69 + '\n')
   so=input("Continue ? [Y/N(yes/No)] > ")
   if so =='y' or so =='Y':
        main()
   else:
        exit()
 except : 
	   	 pass
def Norton() :
 print("""  7ammass Generator (c) Medo7x """)
 zz=input('Enter Number Keys > ')
 try :
   for az in range(int(zz)) :
    gothar = string.ascii_letters + string.digits
    gothar69 = ''.join(choice(gothar) for _ in range(23))
    print(az+1,")",'V'+gothar69.upper()," by M7X")
    save = open("norton.txt", 'a')
    save.write('V'+gothar69.upper() + '\n')
   so=input("Continue ? [Y/N(yes/No)] > ")
   if so =='y' or so =='Y':
        main()
   else:
        exit()
 
 except : 
         pass
def avgantiv() :
 print("""  AVGAntivurus Generator (c) Medo7x """)
 zz=input('Enter Number Keys > ')
 try :
   for az in range(int(zz)) :
    meliodas = string.ascii_letters + string.digits
    meliodas1 = ''.join(choice(meliodas) for _ in range(4))
    ban = string.ascii_letters + string.digits
    ban1 = ''.join(choice(ban) for _ in range(5))
    king = string.ascii_letters + string.digits
    king1 = ''.join(choice(king) for _ in range(5))
    eskanor = string.ascii_letters + string.digits
    eskanor1 = ''.join(choice(eskanor) for _ in range(5))
    gothar = string.ascii_letters + string.digits
    gothar1 = ''.join(choice(gothar) for _ in range(2))
    nanatsu = '8MEH-R'+meliodas1.upper()+'-'+ban1.upper()+'-'+king1.upper()+'-'+eskanor1.upper()+'-'+gothar1.upper()+'MBR-ACED'
    print(az+1,")",nanatsu," by M7X")
    save = open("avgantiv.txt", 'a')
    save.write(nanatsu + '\n')
   so=input("Continue ? [Y/N(yes/No)] > ")
   if so =='y' or so =='Y':
        main()
   else:
        exit()
 except : 
         pass
def esetss() :
 print("""  ESet Smart Security Generator (c) Medo7x \n\n  1) Keyz\n  2) Accounts  """)
 psyco = input('$ ')
 if psyco == '1':
  zz=input('Enter Number Keys > ')
  try :
   for az in range(int(zz)) :
    meliodas = string.ascii_letters + string.digits
    meliodas1 = ''.join(choice(meliodas) for _ in range(5))
    ban = string.ascii_letters + string.digits
    ban1 = ''.join(choice(ban) for _ in range(5))
    king = string.ascii_letters + string.digits
    king1 = ''.join(choice(king) for _ in range(5))
    eskanor = string.ascii_letters + string.digits
    eskanor1 = ''.join(choice(eskanor) for _ in range(5))
    gothar = string.ascii_letters + string.digits
    gothar1 = ''.join(choice(gothar) for _ in range(5))
    nanatsu = meliodas1.upper()+'-'+ban1.upper()+'-'+eskanor1.upper()+'-'+king1.upper()+'-'+gothar1.upper()
    print(az+1,")",nanatsu," by M7X")
    save = open("esetsskeys.txt", 'a')
    save.write(nanatsu + '\n')
   so=input("Continue ? [Y/N(yes/No)] > ")
   if so =='y' or so =='Y':
        main()
   else:
        exit()
  except : 
         pass
 elif psyco =='2':
  zz=input('Enter Number Accounts > ')
  try:
    for az in range(int(zz)) :
      nbadelelrapx99 = ''.join(choice(string.digits) for _ in range(10))
      mazelbekry = string.ascii_letters + string.digits
      mazelbekryx99 = ''.join(choice(string.digits) for _ in range(10))
      nhabettitle = 'UserNaMe : EVA-'+nbadelelrapx99+'\nPassword: '+mazelbekryx99.lower()+'\n-----------------------\nGenerated By M4rkWalker\n\n '
      print(az+1,")",nhabettitle)
      save = open("esetssup.txt", 'a')
      save.write(nhabettitle + '\n')
    so=input("Continue ? [Y/N(yes/No)] > ")
    if so =='y' or so =='Y':
        main()
    else:
        exit()
  except:
          pass
 else : 
    print("What U doing !! Bakka ")

def photoshop():
  print(""" PhotoShop Cs6 Genrator (c) Medo7x """)
  zz=input('Enter Number Keys > ')
  try:
    for az in range(int(zz)) :
        meliodas = string.digits
        meliodas1 = ''.join(choice(meliodas) for _ in range(5))
        ban = string.digits
        ban1 = ''.join(choice(ban) for _ in range(5))
        king = string.digits
        king1 = ''.join(choice(king) for _ in range(5))
        eskanor = string.ascii_letters + string.digits
        eskanor1 = ''.join(choice(eskanor) for _ in range(5))
        gothar = string.digits
        gothar1 = ''.join(choice(gothar) for _ in range(5))
        nanatsu= '1330'+'-'+meliodas1+'-'+ban1+'-'+king1+'-'+eskanor1+'-'+gothar1
        print(az+1,")",nanatsu,"\n------------By M7X---------------\n")
        save = open("cs6.txt", 'a')
        save.write(nanatsu + '\n')
    so=input("Continue ? [Y/N(yes/No)] > ")
    if so =='y' or so =='Y':
        main()
    else:
        exit()    
  except:
           pass
def winkeyz():
  print(""" WinDows Genrator (c) Medo7x """)
  zz=input('Enter Number Keys > ')
  try:
    for az in range(int(zz)) :
        meliodas = string.ascii_letters + string.digits
        meliodas1 = ''.join(choice(meliodas) for _ in range(5))
        ban = string.ascii_letters + string.digits
        ban1 = ''.join(choice(ban) for _ in range(5))
        king = string.ascii_letters + string.digits
        king1 = ''.join(choice(king) for _ in range(5))
        eskanor = string.ascii_letters + string.digits
        eskanor1 = ''.join(choice(eskanor) for _ in range(5))
        gothar = string.ascii_letters + string.digits
        gothar1 = ''.join(choice(gothar) for _ in range(5))
        nanatsu= meliodas1.upper()+'-'+ban1.upper()+'-'+king1.upper()+'-'+eskanor1.upper()+'-'+gothar1.upper()
        print(az+1,")",nanatsu,"\n------------By M7X---------------\n")
        save = open("win.txt", 'a')
        save.write(nanatsu + '\n')
    so=input("Continue ? [Y/N(yes/No)] > ")
    if so =='y' or so =='Y':
        main()
    else:
        exit() 
  except:
           pass 
def amazon():
 print("""  Amazon Generator (c) Medo7x """)
 zz=input('Enter Number Keys > ')
 try :
  for az in range(int(zz)) :
    urname = string.ascii_letters + string.digits
    urname1 = ''.join(choice(urname) for _ in range(4))
    taki = string.ascii_letters + string.digits
    taki2 = ''.join(choice(taki) for _ in range(6))
    metsuha = string.ascii_letters + string.digits
    metsuha3 = ''.join(choice(metsuha) for _ in range(5)) 
    mark = urname1.upper() +('-')+ taki2.upper() +('-')+ metsuha3.upper()
    print(az+1,")",mark," by M7X")
    save = open("amazon.txt", 'a')
    save.write(mark + '\n')
  so=input("Continue ? [Y/N(yes/No)] > ")
  if so =='y' or so =='Y':
        main()
  else:
        exit()
 except : 
          pass

      
def abo():
 print("""
 Name : Mohamed Habeb Musa
 Nickname : Medo7x
 Country : SD
 Facebook : [Not Avaible] / Maybe Im Here > Page : Fb.com/tnwix 
 Mail Me : mhmdhbyb@mail.ru
Telegram : https://t.me/zoalmoshagip
 Github : https://github.com/medo_twix_5
 Youtube : no """)
 exit()
######## Menu ########
#Ps : Dont Change Logo 2 Say That u r The Coder ...Lean Python Its Free 
def main():
 logo = (f"""
\033[1;31m          ___  ___    {B}    _   _  {R}          ___  ___
 {R}        /   |/   |    {B}  | | | |        {R}  /   |/   |
  {R}      / /|   /| |     {B} | |_| |       {R}  / /|   /| |
 {R}      / / |__/ | |    {B}  |  _  |       {R} / / |__/ | |
 {R}     / /       | |    {B}  | | | |     {R}  / /       | |
 {R}    /_/        |_|    {B}  |_| |_|    {R}  /_/        |_|\033[1;32m


                   `         '
   ;,,,             `       '             ,,,;
   `Y888888bo.       :     :       .od888888Y'
     8888888888b.     :   :     .d8888888888
     88888Y'  `Y8b.   `   '   .d8Y'  `Y88888
    j88888  \033[1;31m.db.\033[1;32m  Yb. '   ' .dY  \033[1;31m.db.\033[1;32m  88888k
      `888  \033[1;31mY88Y\033[1;32m    `b ( ) d'    \033[1;31mY88Y\033[1;32m  888'
       888b  \033[1;31m'"\033[1;32m        ,',        \033[1;31m"'\033[1;32m  d888
      j888888bd8gf"'   ':'   `"?g8bd888888k
        'Y'   .8'     d' 'b     '8.   'Y'
         !   .8' \033[0;35mdb\033[1;32m  d'; ;`b  \033[0;35mdb\033[1;32m '8.   !
            d88  \033[0;35m`'\033[1;32m  8 ; ; 8  \033[0;35m`'\033[1;32m  88b
           d888b   .g8 ',' 8g.   d888b
          :888888888Y'     'Y888888888:
          '! 8888888'       `8888888 !'
             '8Y  `Y         Y'  Y8'
              Y                   Y
              !                   !
 """)
 print(logo)
 print(' \033[1;36mHello '+getpass.getuser()+' : '+time.asctime( time.localtime(time.time()) ),'\n \033[1;33m[!] Sometimes U Need To Use Vpn (Ban Or CountryNotAvaible)\n \033[1;36m[1]  Steam ')
 print(" [2]  Express ")
 print(" [3]  Hidemyass ")
 print(" [4]  Tn Mobile Sold ")
 print(" [5]  G2A ")
 print(" [6]  Google Play ")
 print(" [7]  AVG Antivurus ")
 print(" [8]  Eset Smart Security ")
 print(" [9]  Norton Antivurus  ")
 print(" [10] PhotoShop Cs6  ")
 print(" [11] Win Keyz  ")
 print(" [12] Amaz0n  ")
 print(" [13] CCGen & CC'Check ")
 print(" [69] About & Exit ")
 print('')
 zack = input("   └──╼ \033[0;31m❯\033[1;32m❯\033[1;31m\033[1;33m❯ ")
 if zack == '1':
     steam()
 elif zack == '2':
    express()
 elif zack == '3' :
    hma()
 elif zack == '4' :
    karta()
 elif zack == '5' :
    g2a()
 elif zack == '6' :
    gplay()
 elif zack == '7' :
    avgantiv()
 elif zack == '8':
    esetss()
 elif zack == '9':
    Norton()
 elif zack == '10':
    photoshop()
 elif zack == '11':
    winkeyz()
 elif zack == '12':
    amazon()
 elif zack == '13':
    print("  Go To http://m4rkwalker.ga/cc.html Or Contact Me")
 elif zack == '69' :
    abo()
 else :
     print(f"{R} Open Ur Eye !! Asshool -____- ")
     exit()
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print (" \nNani ?? ... R U Bakka ??")
sys.exit()
######## Hey U r ... Do u Like Pizza ?? xD ########
