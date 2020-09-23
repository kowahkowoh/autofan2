import os
try:
	from websocket import create_connection
except:
	os.system('pip install websocket-client')
import json
import datetime
from datetime import datetime

try:
    import thread
except ImportError:
    import _thread as thread
import time
try:
	import requests
except:
	os.system('pip install requests')


import websocket
import traceback
try:
	from fake_useragent import UserAgent
except:
	os.system('pip install fake-useragent')
import re
import threading
import random
import uuid
import platform





counter = 0
penghitung=0

def tele(bot_message):
    
    bot_token = '1160430048:AAHWoxOJxQ8amBHh0b3CsRTz8NeXphWVf70'
    bot_chatID = '-483298315'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
   
 
def activation(bot_message):
    
    bot_token = '1160430048:AAHWoxOJxQ8amBHh0b3CsRTz8NeXphWVf70'
    bot_chatID = '-426516657'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)


def unblock():
	print("[ INFO ]")
	print(" - digunakan untuk menghapus semua list block \n - login akun terlebih dahulu via no telp dan password \n - akan otomatis meng unblock semua dari daftar block")
	
	
	print("____________________________________________________________")
	
	response5 = requests.get('https://id-api.spooncast.net/users/'+userid+'/followings/',headers=headers2)
	nexts=(response5.json()['next'])
	idd2=[]
	z=0
	for i in range(0,len(response5.json()['results'])):
		idd2.append(str(response5.json()['results'][int(i)]['id']))
	while nexts!="":
		print("========================")
		response6 = requests.get(nexts,headers=headers2)
		link1=(response6.json()['next'])
		print(link1)
		nexts=link1
		for i in range(0,len(response6.json()['results'])):
			idd2.append(str(response6.json()['results'][int(i)]['id']))
			thread.start_new_thread(unfolcepet, (str(response6.json()['results'][int(i)]['id']),))
			z+=1
			print(z)
	print("debug")
	print(len(idd2))
	print(idd2)
	il=0
	for idkickers in idd2:
		try:
			#thread.start_new_thread(unfolcepet, (idkickers,))
			#response = requests.post('https://id-api.spooncast.net/users/'+idkickers+'/unfollow/',headers=headers,)
#			print(response.json())
#			print(idkickers+" berhasil dibersihkan")
			print(il)
			il+=1
		except:
			print("error")

def unfolcepet(idkickers):
	response = requests.post('https://id-api.spooncast.net/users/'+idkickers+'/unfollow/',headers=headers2,)
	print(response.json())
	print(idkickers+" berhasil diunfollow")
	
	
	


def refresher():
	global counter
	global usertoken
	#pesan='{"event":"live_health","type":"live_rpt","live_id":'+slink+',"user_id":'+userid+',"useragent":"Web","appversion":"5.4.9"}'
	pesan='{"event":"live_health","type":"live_rpt","live_id":'+slink+',"user_id":'+userid+',"useragent":"Web","appversion":"5.4.9"}'
	pesan='{"event":"live_health","type":"live_rpt","live_id":'+slink+',"user_id":'+idnyadj+',"useragent":"Web","appversion":"5.4.9"}'
	print("ini counrr "+str(counter))
	if counter >= 0:
		ws.send(pesan)
	counter+=1
	threading.Timer(10, refresher).start()
	

def autochat():
	global counter
	global usertoken
	olahankata="Jangan lupa fan to fan ya"
	
	if counter >= 2:
		ws.send('{"appversion":"5.4.9","event":"live_message","token":"29b0534f029ff4614cffbd466a5c1b2327f65f72","useragent":"Web","message":"'+olahankata+'","type":"live_rpt"}')
	counter+=1
	threading.Timer(180, autochat).start()
	
	
def infoer():
	z=open('listid.txt','r+').read().split('\n')
	print('______________________\n\n')
	
	print('Total keseluruhan yang telah difan '+str(len(z))+' akun')
	
	print('\n\n_______________________')
	
	
	threading.Timer(120, infoer).start()
	




def getslink(txtid):
	regex = re.compile(r'^(?:http|ftp)s?://', re.IGNORECASE)
	
	
	if re.match(regex, txtid) == None:
		txtid='https://'+txtid
	response = requests.get(txtid)
	url = response.url
	return url[34:-59]
	
	
def getlives(slink):
	response = requests.get('https://id-api.spooncast.net/lives/'+slink,headers=headers2).json()
	return response
	

listfb=[
'Fanback ya kak makasih',
'aku fan nih kak , fan back ya',
'fanback kak , jangan pelit :p',
'fanback ya',
'fanback kak :3'
]

def on_message(ws, message):
	global penghitung
	chat = json.loads(message)
	#print(chat)
	
	try:
		evn=chat['event']
		if evn == "live_join" or evn == "live_shadowjoin" or evn == "live_like":
			print(evn)
			appender=open('listid.txt','a+')
			listid=open('listid.txt','r+').read().split('\n')
			uid = str(chat['data']['author']['id'])
			if uid not in listid:
				following=requests.post('https://id-api.spooncast.net/users/'+uid+'/follow/',headers=headers2)
				fanb={"contents":random.choice(listfb)}
				fanboard=requests.post('https://id-api.spooncast.net/users/'+uid+'/fanmessages/',headers=headers2,json=fanb)
				appender.write(uid+'\n')
				penghitung+=1
				print(str(penghitung)+' berhasil ke id '+uid)
			else:
				print('skip '+uid)
				

	except Exception as e:
		print('ini error bawah definisi')
		print(traceback.format_exc())
		print(e)
	
	
	

def on_error(ws, error):
	print(error)

def on_close(ws):
	print("### closed ###")
	

def on_open(ws):
	def run(*args):
		global usertoken
		#print(usertoken)
		#time.sleep(5)
		#pesan0 = '{"live_id":'+slink+',"token":"'+usertoken+'","event":"live_state","appversion":"5.4.9","useragent":"Web","type":"live_req","user_id":'+userid+'}'
		#ws.send(pesan0)
		#pesan0 = '{"live_id":'+slink+',"event":"live_state","appversion":"5.4.9","useragent":"Web","type":"live_req","user_id":'+userid+'}'
		pesan0 = '{"live_id":'+slink+',"event":"live_state","appversion":"5.4.9","useragent":"Web","type":"live_req","user_id":'+userid+'}'
		
		if True:
			ws.send(pesan0)

		
		pesan = '{"live_id":'+slink+',"token":"'+usertoken+'","event":"live_join","appversion":"5.4.9","useragent":"Web","type":"live_req","retry":0,"reconnect":false}'
		ws.send(pesan) 
		
		refresher()
		autochat()
		infoer()
		print(slink)
		print(userid)
		#print(usertoken)
		print("====")
	
	thread.start_new_thread(run, ())


nurut = False
usertoken = ''
if __name__ == "__main__":
	
	
	
	
	
	
	try:
		#saring
		if os.path.exists('000aktivasi.johnson') == True:
			namaaktivasi='000aktivasi.johnson'
		else:
			namaaktivasi='000aktivasi.johnson'
		
		kode=0
		print("sedang mengecek ...")
		print("sedang memuat ...")
		print("pastikan internet aman ...")
		req = requests.get('https://diveot.site/spoon/fan.fan').text
		
		act = requests.get('https://diveot.site/spoon/kodepublik')
		
		active = act.json()['kode']
		#active = requests.get('https://diveot.site/spoon/kodecat').json()['kode']
		
		imei = act.json()['imei']
		#imei = requests.get('https://diveot.site/spoon/imei').json()['imei']
		perangkat = act.json()['perangkat']
		ver = act.json()['versi']
		os.system('clear')
		print("sedang memuat ...")
		if req != "A":
			try:
				print(req)
			except:
				print("SCRIPT DIMATIKAN")
			exit()
	
		
		#pess = requests.get('https://diveot.site/spoon/pesan.txt').text
		#pesse = requests.get('https://diveot.site/spoon/ucingmessage.json')
		#pesen = pesse.json()
		
		
		#print(pess)
		#time.sleep(10)
		
		#aktivasi = zz.json()['kode']
		
		#print(aktivasi)
		#cur_path = os.path.dirname(__file__)
		#new_path = os.path.relpath('..\\subfldr1\\testfile.txt', cur_path)
		#with open(new_path, 'w') as f:
			#f.write(data)
	
		
		
		
		#proses aktivasi
		with open(namaaktivasi, "r") as jsonFile:
			aktivasi = json.load(jsonFile)
		
		
		if aktivasi['kode'] not in active:
			if aktivasi['kode']==0:
				
				while(aktivasi['nama']==""):
					print('nama tidak boleh kosong')
					aktivasi['nama']=input('Masukkan nama sesuai yang diperintahkan : ')
					if aktivasi['nama']!="":
						with open(namaaktivasi, "w") as jsonFile:
							json.dump(aktivasi, jsonFile)
				
				abc=random.randint(100000,999999)
				aktivasi['kode']=abc
				
				with open(namaaktivasi, "w") as jsonFile:
					json.dump(aktivasi, jsonFile)
				
				activation(str(datetime.now())[:19]+'\n-'+str(aktivasi['nama'])+'\n-'+str(aktivasi['kode'])+'\n-'+str(uuid.uuid1())[24:]+'\n-'+str(platform.platform())+'\n'+platform.version()[15:])
				activation('\['+str(aktivasi['kode'])+',')
				activation('\["'+str(uuid.uuid1())[24:]+'",')
				print('silahkan tunggu aktivasi ya akak '+aktivasi['nama'])
				print('KODE ANDA : '+str(aktivasi['kode']))
				print('\n\nPERINGATAN !!!')
				print('BACA ATAU TIDAK BACA DIANGGAP SUDAH BACA')
				print('JANGAN SEBAR KODE INI KESIAPAPUN')
				print('KECUALI PENJUAL')
				print('MELANGGAR PERATURAN INI DAPAT MENGAKIBATKAN PEMATIAN KODE')
				print('silahkan tunggu aktivasi ya akak '+aktivasi['nama'])
				
				
				exit()
				
				
				
			else:
				while(aktivasi['nama']==""):
					print('nama tidak boleh kosong')
					aktivasi['nama']=input('Masukkan nama sesuai yang diperintahkan : ')
					if aktivasi['nama']!="":
						with open(namaaktivasi, "w") as jsonFile:
							json.dump(aktivasi, jsonFile)
					
				activation(str(datetime.now())[:19]+'\n-'+str(aktivasi['nama'])+'\n-'+str(aktivasi['kode'])+'\n-'+str(uuid.uuid1())[24:]+'\n-'+str(platform.platform())+'\n'+platform.version()[15:])
				activation('\['+str(aktivasi['kode'])+',')
				activation('\["'+str(uuid.uuid1())[24:]+'",')
				print('silahkan tunggu aktivasi ya akak '+aktivasi['nama'])
				print('KODE ANDA : '+str(aktivasi['kode']))
				print('\n\nPERINGATAN !!!')
				print('BACA ATAU TIDAK BACA DIANGGAP SUDAH BACA')
				print('JANGAN SEBAR KODE INI KESIAPAPUN')
				print('KECUALI PENJUAL')
				print('MELANGGAR PERATURAN INI DAPAT MENGAKIBATKAN PEMATIAN KODE')
				print('silahkan tunggu aktivasi ya akak '+aktivasi['nama'])
				
				
				exit()
		
		else:
			print('KODE sudah aktif')
			time.sleep(.3)
		
		
		if str(uuid.uuid1())[24:] not in imei:
			
			if str(platform.platform()).translate({ord(i): None for i in '-+ .'}) in perangkat:
				
				if str(platform.version())[15:] in ver:
					pass
				
				else:
					print('Perangkat ini di ban oleh mimin')
					activation('Aktivitas Illegal \nFUN versi\n'+str(datetime.now())[:19]+'\n'+str(aktivasi['kode'])+'\n'+str(aktivasi['nama'])+'\n'+str(uuid.uuid1())[24:]+'\n'+platform.platform())
					activation('\["'+str(platform.version())[15:]+'",')
					exit()
					
				
				
			else:
				
				#print(str(platform.platform()).translate({ord(i): None for i in '-+ .'}))
				#print(perangkat)
				print('Perangkat ini di ban oleh mimin')
				activation('Aktivitas Illegal \nFUN platform\n'+str(datetime.now())[:19]+'\n'+str(aktivasi['kode'])+'\n'+str(aktivasi['nama'])+'\n'+str(uuid.uuid1())[24:]+'\n'+platform.platform())
				activation('\["'+str(platform.platform()).translate({ord(i): None for i in '-+ .'})+'",')
				activation('\["'+str(platform.version())[15:]+'",')
				exit()
			
			
			
		
		
		
		#pw = zz.json()['password']
		#print(pw)
		#pww = input("masukkan password: ")
		#while pww != pw:
			#print("password salah")
		#	exit()
		print("SELAMAT DATANG")
		tele(str(datetime.now())[:19]+'\n-'+aktivasi['nama']+' '+str(aktivasi['kode'])+' FUN \n-'+str(uuid.uuid1())[24:]+'\n-'+str(platform.platform())+'')
		os.system('clear')
		print("enjoy")
		
	except Exception as e:
		print(e)
		print(traceback.format_exc())
		exit()
	
	
	
	
	
	
	
	
	
	
	

	e="ini error"
	namaconfig='config.johnson'
	totid=[]
	with open(namaconfig, "r") as jsonFile:
		config = json.load(jsonFile)
	
	headers = {"User-Agent":"Mozilla/5.0",'origin':'https://www.spooncast.net','referer':'https://www.spooncast.net/','content-type':'application/json'}
	headers2={'User-Agent':'Mozilla/5.0','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','origin':'https://www.spooncast.net','referer':'https://www.spooncast.net/','content-type':'application/json'}
	params1 = {'cv':'heimdallr'}
	params2 = {'cv':'heimdallr2'}

	print('autofan')

	if True:
		if config['nomor']=='':
			print("Contoh seperti ini : 6285155415154")
			print("depannya harus 62")
			config['nomor'] = input('masukkan nomor telepon akun anda : ')
			config['password'] = input('masukkan password : ')
			with open(namaconfig, "w") as jsonFile:
				json.dump(config, jsonFile)
				
			os.system("python autofan.py")
		
		c = open('listid.txt','w+')
			
		nomer = config['nomor']
		password = config['password']
		infoer()
		print("nomor sekarang "+nomer)
		print("password sekarang "+password)
		print("otw login ...")
		if True:
			if True:
				ua = UserAgent()
				uafix = ua.random
				headers = {"User-Agent":uafix,'origin':'https://www.spooncast.net','referer':'https://www.spooncast.net/','content-type':'application/json'}
				tokens = requests.post('https://id-auth.spooncast.net/tokens',headers=headers,json={"device_unique_id":uafix,"auth_data":{"act_type":"phone","password":password,"msisdn":nomer}})
				
				try:
					jwt = tokens.json()['data']['jwt']
					rtoken = tokens.json()['data']['refresh_token']
					headers2 = {"Authorization":"Bearer "+jwt,"User-Agent":uafix,'origin':'https://www.spooncast.net','referer':'https://www.spooncast.net/','accept':'application/json','host':'id-api.spooncast.net','save-data':'on','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'en-US,en;q=0.9,ru;q=0.8','access-control-request-method':'GET','access-control-request-headers':'authorization'}
					headersopt = {"User-Agent":uafix,'origin':'https://www.spooncast.net','referer':'https://www.spooncast.net/','accept':'*/*','host':'id-api.spooncast.net','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'en-US,en;q=0.9,ru;q=0.8'}
					login = requests.post('https://id-api.spooncast.net/signin/?version=2',headers=headers2,json={"device_unique_id":uafix,"auth_data":{"act_type":"phone","password":password,"msisdn":nomer}}).json()
					print(login)
					userid = str(login['results'][0]['id'])
					usertoken = 'Bearer '+jwt
					print('berhasil login')
					
					
				except Exception as e:
					
					print(e)
					
					print(traceback.format_exc())
					print('_________________________________________________')
					print('AKUN GAGAL')
					print('SILAHKAN PILIH MENU NOMOR 3 UNTUK GANTI AKUN')
					print('_________________________________________________')
			print("""
MENU
1. Unfollow semua following sampai 0 
2. Parkun di room rame + autofollowing + fanboard + autochat ngemis fan
3. Ganti akun
4. reset idlist 

SCRIPT GW GA ABAL2
GAK DIPASANGIN PHISING
CP : 085155415154
	""")
		
		pil = int(input("masukkan pilihan anda : "))
		if pil == 1:
			unblock()
			
		elif pil == 2:
			print('tips : masukkin ke room rame')
			print('sharelink room rame dibawah ini')
			print('contoh link https://spoon.click/id_live_7826870')
			txtid = input("masukkan link : ")
			slink = getslink(txtid)
			lives = getlives(slink)
			
			headers={'User-Agent':'Mozilla/5.0','Authorization':'Token '+usertoken,'origin':'https://www.spooncast.net','referer':'https://www.spooncast.net/','content-type':'application/json'}
			reqacc = requests.get('https://id-api.spooncast.net/lives/'+str(slink)+'/access/',headers=headers2)
			idnyadj = str(reqacc.json()['results'][0]['author']['id'])
			
			
			reqtemp = requests.get('https://id-api.spooncast.net/items/template/',headers=headers2)
			
		
			websocket.enableTrace(False)
			ws = websocket.WebSocketApp("wss://id-heimdallr.spooncast.net/"+slink,on_message = on_message,on_error = on_error,on_close = on_close,header={'User-Agent':'Mozilla/5.0'})
			ws.on_open = on_open
			ws.run_forever()
		elif pil==3:
			
			if config['nomor']=="":
				print("Contoh seperti ini : 6285155415154")
				print("depannya harus 62")
				config['nomor'] = input('masukkan nomor telepon akun anda : ')
				with open(namaconfig, "w") as jsonFile:
					json.dump(config, jsonFile)
				
				os.system("python autofan.py")
			
		elif pil==4:
			os.remove('listid.txt')
			print('berhasil')
			os.system("python autofan.py")

