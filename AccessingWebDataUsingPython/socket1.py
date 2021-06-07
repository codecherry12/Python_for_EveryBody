import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data=mysock.recv(512)
    if len(data)<1:break
    print(data.decode(),end='')
mysock.close()
'''in python3--> every string is a unicode string and it is differ to byte string
   in python2-->every string is differ to unicode string and same to byte string
   encode()-->it takes the string as unicode string and convert it into byte string which is UTF-8(which is most popular byte string)
   and then we get the data in byte string
   decode()-->it takes the recived byte string data and convert it into unicode string and prints that unicode string'''
