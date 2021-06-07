#In this code we use a software called Beautiful Soup where it takes out the html data
#and make that data html.parser
#folder bs4 is unzipped file of BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
"""this SSL is for https:// sites"""
#import ssl

#ignore SSL certificate errors
#ctx=ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode=ssl.CERT_NONE

url=input("Enter url:")
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

#Retrieve all of the anchor tags
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))
