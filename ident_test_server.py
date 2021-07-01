#!/usr/bin/env python3

import sys
import socket
import _thread as thread

if __name__ != "__main__":
    sys.exit(1)

def send_ident_request(client_addr, client_port, server_port):
    try:
        try:
            s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
            s.settimeout(timeout)
            s.connect((client_addr, ident_port))
        except:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            s.connect((client_addr, ident_port))
        s.send(str('%s, %s\r\n' % (client_port, server_port)).encode('utf-8'))
        msg = s.recv(1024)
        s.close()
        return msg
    except:
        return b'Connection to ident server failed!\r\n'

def on_new_client(clientsocket,addr):
    clientsocket.send(send_ident_request(addr[0], addr[1], port))
    clientsocket.close()

if len(sys.argv[1:]) > 0:
    host = str(sys.argv[1])
else:
    host = "::"

if len(sys.argv[2:]) > 0:
    port = int(sys.argv[2])
else:
    port = 6000

if len(sys.argv[3:]) > 0:
    ident_port = int(sys.argv[3])
else:
    ident_port = 113

if len(sys.argv[4:]) > 0:
    timeout = float(sys.argv[4])
else:
    timeout = 1.0

print ("Server on %s port %s. Ident server port is %s with timeout %ss." % (host, port, ident_port, timeout))

try:
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.bind((host, port))
except:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

s.listen()
while True:
   c, addr = s.accept()
   print ('Got connection from %s' % (addr,))
   thread.start_new_thread(on_new_client,(c,addr))
s.close()
