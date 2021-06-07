#assignment QUESTION URL:
#https://www.py4e.com/tools/python-data/?PHPSESSID=322b98a3e8e7f51f37f9f560ed41fce1
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter url -')#http://py4e-data.dr-chuck.net/comments_42.html (OR) http://py4e-data.dr-chuck.net/comments_1254845.html
html=urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
#retrieving the span tags
tags=soup('span')
count=0
sum=0
for tag in tags:
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    sum+=int(tag.contents[0])
    count+=1
    #print('Attrs:', tag.attrs)
print("count",count)
print("sum",sum)
