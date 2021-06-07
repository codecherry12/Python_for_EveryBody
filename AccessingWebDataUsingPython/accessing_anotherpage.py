import urllib.request,urllib.parse,urllib.error#library function rather than using socker
import re
def url(fh):
    fhand=urllib.request.urlopen(fh)#looks like opening a file
    for line in fhand:
        x=line.decode().strip()#decode means converting a bite string into unicode string
        print(x)
fh='http://www.dr-chuck.com/page1.htm'
url(fh)
url('http://www.dr-chuck.com/page2.htm')
