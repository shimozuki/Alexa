from time import sleep
print('    _    _                ') 
sleep(0.5)
print('   / \  | | _____  ____ _ ')
sleep(0.5)
print('  / _ \ | |/ _ \ \/ / _` |')
sleep(0.5)
print(' / ___ \| |  __/>  < (_| |')
sleep(0.5)
print('/_/   \_\_|\___/_/\_\__,_|')
sleep(0.5)
                                                      

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import webbrowser
import wikipedia
import datetime
import sys
import re
import random,os
import smtplib


def Alexa(text):
	sn = gTTS(text,lang="id")
	sn.save("sound.mp3")
	playsound("sound.mp3")
	print("Alexa :",text)

def greeting():
	ch = int(datetime.datetime.now().hour)
	if (ch >= 0 and ch < 12):
		Alexa("Assalamualaikum, Selamat pagi!")
	if (ch >= 12 and ch < 18):
		Alexa("Assalamualaikum, Selamat siang!")
	if (ch >= 18 and ch != 0):
		Alexa("Assalamualaikum, Selamat malam!")
greeting()

Alexa("hy shimozuki ada yang bisa aku bantu")

def command():
	r = sr.Recognizer()
	with sr.Microphone() as source:

		print("\nMendengarkan...")
		r.pause_threshold = 1
		audio = r.listen(source)
		try:
			query = r.recognize_google(audio,language="id-ID")
			print("Kamu:",query)
		except:
			Alexa("Maaf, aku tidak mengerti apa yang kamu katakan , tolong ketikkan perintah ")
			query = input("Perintah : ")
	return query
#credential email
def send_email(recipient,subject,pesan):
	user = "robbishimozuki@gmail.com" 
	pawd = "Robbivani1305" 
	From = user
	to = recipient if isinstance(recipient, list) else [recipient]
	subj = subject
	body = pesan
	try:
		message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (From, ", ".join(to), subj, body)
		server_ssl = smtplib.SMTP_SSL("smtp.gmail.com",465)
		server_ssl.ehlo()
		server_ssl.login(user,pawd)
		server_ssl.sendmail(From,to,message)
		server_ssl.close()
		Alexa('berhasil mengirim email')
	except Exception as a:
		print(a)
		Alexa('gagal mengirim email')
		pass

def wiki(kt):
	wikipedia.set_lang("id")
	res = wikipedia.summary(kt,sentences=2)
	Alexa(res)

def predict(kata):
	kabar = ['kabarmu','kabar','keadaanmu','keadaan']
	umur = ['umurmu','umur']
	pembuat = ['alexa beritahu aku informasi tentang mu']
	pencipta = ['alexa beritahu aku informasi tentang mu']
	jawabP = ['aku dibuat di sumbawa dengan bahasa program python, umur ku yang jelas lebih muda dari mu, dan aku dibuat oleh seseorang yang bernama shimozuki']
	jawabU = ['maaf itu rahasia','yang pasti aku lebih muda darimu','tanyakan saja kepada pembuatku']
	jawabK = ["hem aku tidak pernah seceria ini","kabarku baik baik saja","aku merasa bahagia hari ini"]
	jawabI = ["hem aku tidak pernah seceria ini","kabarku baik baik saja","aku merasa bahagia hari ini"]
	
	for ta in kabar:
		if ta in kata:
			Alexa(random.choice(jawabK))
	for um in umur:
		if um in kata:
			Alexa(random.choice(jawabU))
	for pem in pembuat:
		if pem in kata:
			Alexa(random.choice(jawabP))
	for bu in pencipta:
		if bu in kata:
			Alexa(random.choice(jawabI))
				
	if 'musik' in kata:
		Alexa("Ketikkan letak direktori musikmu")
		dir = input("Direktori : ")
		try:
			for play in os.listdir(dir):
				if play.endswith('mp3'):
					try:
						Alexa('memutar musik !')
						Alexa('selamat mendengarkan')
						playsound(dir+"/"+play)
					except Exception as a:
						print(a)
				else:
					Alexa("mencari file lagu !")
		except Exception as a:
			print("Direktori tidak ditemukan")
	if 'email' in kata:
		Alexa("siapa penerima emailnya ?")
		pen = input("Penerima : ")
		Alexa("tuliskan subjectnya ")
		sub = input('subject : ')
		Alexa("tuliskan pesan yang ingin dikirim")
		pes = input('Pesan : ')	
		Alexa("sedang mengirim email")
		send_email(pen,sub,pes)		
			
	if 'buka' in kata and 'exploit database' not in kata:	
		pecah = kata.split()
		if len(pecah) != 1:
			Alexa('oke')
			webbrowser.open("http://"+pecah[1]+".com")
		else:
			Alexa('tidak bisa membuka mesin pencari')
			pass
	if 'wiki' in kata:	
		pecah = kata.split('wiki')
		if len(pecah) != 1:
			Alexa('oke')
			wiki(pecah[1])
		else:
			Alexa('tidak bisa membuka wikipedia')
			pass
	if 'exploit database' in kata:
		Alexa('oke')
		webbrowser.open("http://exploit-db.com")
	if 'cari' in kata:
		pecah = kata.split('cari')
		if len(pecah) != 1:
			Alexa('oke')
			webbrowser.open("https://www.google.com/search?q="+pecah[1]+"&ie=utf-8&oe=utf-8&client=firefox-b-ab")
		else:
			Alexa('tidak bisa membuka mesin pencari')
	
	Alexa("menunggu perintah selanjutnya")
def main():
	
	a = 1
	while a > 0:
		qr = command()
		if "Alexa stop" in qr:
			Alexa("Assalamualaikum,selamat beristirahat shimozuki")
			sys.exit()
		predict(qr.lower())
		
if __name__ == "__main__":
	main()
		
			
