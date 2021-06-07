"""code to get data in XML"""
import xml.etree.ElementTree as ET
data='''<stuff>
       <users>
           <user x="2">
               <id>001</id>
               <name>Chuck</name>
           </user>
           <user x="7">
                 <id>009</id>
                 <name>Brent</name>
           </user>
       </users>
     </stuff>'''

tree=ET.fromstring(data)
lst=tree.findall('users/user')
#print(lst)
print('User Count:',len(lst))
for item in lst:
    print('Name:',item.find('name').text)
    print("Id",item.find('id').text)
    print('Attribute:',item.get('x'))
