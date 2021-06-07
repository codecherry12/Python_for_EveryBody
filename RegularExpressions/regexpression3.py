import re
x='My 2 favorite nu,bers are 19 and 42'
y=re.findall('[0-9]+',x)
print(y)
y=re.findall('[AEIOU]+',x)
print(y)
x='From:Using the : character'
y=re.findall('^F.+:',x)
print(y)
z=re.findall('^F.+?:',x)
print(z)
y=re.findall('^F.+',x)
print(y)
x='From:using the : charaxter'
y=re.findall('^F',x)
print(y)
string='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y=re.findall('\S+@\S+',string)
q=re.findall('^From (\S+@\S+)',string)
z=re.findall('\S+',string)
x=re.findall('\S+@\S+?',string)
w=re.findall('\S+?@\S+',string)
n=re.findall('\S +',string)
print(y)
print(q)
print(z)
print(x)
print(y)
print(n)
