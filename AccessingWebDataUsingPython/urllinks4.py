'''
ASSIGNMENT QUESTITION LINK: https://www.py4e.com/tools/python-data/?PHPSESSID=de4926cd1723bc924a199405a1bb4489
Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Kiyara.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: V
'''
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url:')#enter http://py4e-data-dr-chuck.net/known_by_Fikret.html (OR) http://py4e-data-dr-chuck.net/known_by_Kiyara.html
list=[]
count=int(input("Enter Count:"))
pos=int(input("Enter position:"))
while(count!=0):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        list.append(tag.get('href', None))
    print(list[pos-1])
    url=str(list[pos-1])
    list=[]
    count-=1
