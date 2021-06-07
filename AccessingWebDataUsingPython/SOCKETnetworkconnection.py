#this is the python code where we dail to a webserver
import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#first parameter is calling internet and second parameter is to stream the server
mysock.connect(('data.pr4e.org',80))#data.pr4e.org is a webserver domain name and 80 is a port number
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data=mysock.recv(512)
    if len(data)<1:break
    print(data.decode(),end='')
mysock.close()
