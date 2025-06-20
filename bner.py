#Thư Viện
import os, sys, requests, socket
from time import sleep
#Màu
xam = "\033[1;38;5;8m"
xla = "\033[1;38;5;10m"
vang = "\033[1;38;5;11m"
xduong = "\033[1;38;5;14m"
trang = "\033[1;38;5;15m"
xdam = "\033[1;38;5;21m"
xlv1 = "\033[1;38;5;42m"
xv1 = "\033[1;38;5;44m"
xlv2 = "\033[1;38;5;49m"
dv1 = "\033[1;38;5;50m"
la = "\033[1;38;5;79m"
vchuoi = "\033[1;38;5;154m"
do = "\033[1;38;5;196m"
tim = "\033[1;38;5;201m"
cam = "\033[1;38;5;202m"
hdam = "\033[1;38;5;204m"
hong = "\033[1;38;5;211m"
vlightc = "\033[1;38;5;214m"
clightv = "\033[1;38;5;220m"
#Clear All
os.system('clear')
#Hợp Tác
wjm = "?"
#Admin hợp tác
wnn = xdam+"W"+xla+"h"+vang+"i"+do+"t"+cam+"e"+vchuoi+" NN"+xam
ma = hdam+"M"+hong+"i"+hdam+"n"+hong+"h"+hdam+"A"+hong+"n"+hdam+"h"+hong+"s🐰"+xam
jndk = xdam+"J"+xv1+"u"+xduong+"n"+xlv2+"i"+xlv1+"d"+xla+"o" +clightv+" K"+vlightc+ "a"+cam+"i"+xam
ht = wnn+trang+" & "+ma+trang+" & "+ jndk
#IP
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
#Banner
def minhanhs():
 os.system("cls" if os.name == "nt" else "clear")
 macuti = f"""               {ht}\n
⠀⠀⠀⠀⠀⣠⣶⣦⠀⠀⠀⣀⣤⣴⣶⣶ ⠀⠀⠀⠀⣀⣴⣦⠀     {dv1}Copyright{trang} : {ma}
⠀⠀⠀ ⣾⣿⣿⣿⣠⣴⣿⣿⣿⣿⣿⣿⠀⣀⣤⣶⣿⣿⣿⡟⠀     {dv1}Admin{trang}     : {wnn}
⣀⣀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀     {dv1}Admin{trang}     : {jndk}
⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣤⣤⣤
⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿     {xla}Name Tool{trang} :{xam}
⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁        {xlv2}         Banner{xam}
⠀⠀⣿⣿⡟⠀⠀⠀⠀{xla} ⡴⠖⠦{xam}⠼⢿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀
⠀⠀⣿⣿⠀⠀⠀⠀⠀{xla}⣼⣇⣋⡗{xam}⠀⠀⢿⣿⢻⣿⡟⢿⣿⣿⣷⠀     {dv1}Github   {trang} : {do}@404ERROR{xam}
⠀⣀⣿⣿⣤⣤⣤⣤⣤⣬⣭⣥⣤⣤⣤⣤⣤⣼⣿⣇⡀⠙⣿⡿⠀                 {xlv1}@whitenn{xam}
⠀⣿⣿⣿⠛⠻⣿⡟⠛⠛⠛⠛⠛⠛⣿⡿⠛⠻⣿⣿⡇⠀⠀⠀⠀                 {xlv1}@junidokai{xam}
⠀⣿⣿⣿⠀⠀⠀⣠⣾⣿⣿⣿⣿⣦⣀⠀{do}⣿{xam}⠀⣿⣿⡇⠀⠀⠀⠀
⠀⠙⢿⣿⣶⣾⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣶⣾⣿⠟⠁⠀⠀⠀⠀     {xduong}IP của bạn : {xlv2}{ip}{xam}
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣦⣴⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{do}                         Hoàng Xa - Trường Xa{trang} là của {vang}Việt Nam 🇻🇳
"""
 for X in macuti:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00010)
minhanhs()
#hah
