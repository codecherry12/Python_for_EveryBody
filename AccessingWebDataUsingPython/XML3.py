import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
import ssl
#ignore ssl certificate error
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
while True:
    address=input("Enter location:")
    sum=0
    print("Retrieving",address)
    uh=urllib.request.urlopen(address,context=ctx)
    data=uh.read()
    print("Retrieved",len(data),"characters")
    #print(data.decode())
    tree=ET.fromstring(data)
    #counts=tree.findall('comments/comment')
    counts = tree.findall('.//count')
    print("Count:",len(counts))
    for count in counts:
        #sum+=int(count.find('count').text)
        sum+=int(count.text)
    print("Sum:",sum)
