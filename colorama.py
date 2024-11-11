import colorama
from colorama import Fore,init,Back

#Warna Colorama
B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
#Backround Teks Colorama
BB = Back.BLUE
WW = Back.WHITE
RR = Back.RED
GG = Back.GREEN
YY = Back.YELLOW

print(f'''
\033[1m{B}WARNA BIRU COLORAMA
\033[1m{W}WARNA PUTIH COLORAMA
\033[1m{R}WARNA MERAH COLORAMA
\033[1m{G}WARNA HIJAU COLORAMA
\033[1m{Y}WARNA KUNING COLORAMA

{BB}Backround Teks Warna Biru \033[0m
{WW}Backround Teks Warna Putih \033[0m /Jarang
{RR}Backround Teks Warna Merah \033[0m
{GG}Backround Teks Warna Hijau \033[0m /Jarang
{YY}Backround Teks Warna Kuning \033[0m''')
