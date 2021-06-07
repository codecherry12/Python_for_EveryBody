import urllib.request,urllib.parse,urllib.error#library function rather than using socker

fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')#looks like opening a file
for line in fhand:
    print(line.decode().strip())#decode means converting a bite string into unicode string
