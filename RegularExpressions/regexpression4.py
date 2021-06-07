"""data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atposition=data.find('@')
print(atposition)
spaceposition=data.find(' ',atposition)
print(spaceposition)
slicing=data[atposition+1:spaceposition]
print(slicing)"""#output:uct.ac.za

#similar code by using split method

'''string='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words=string.split()
email=words[1]
pieces=email.split('@')
print(pieces[1])'''

#similar code using regular expressions
'''import re
string='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y=re.findall('@([^ ]*)',string)
print(y)'''

#similar code using regular expressions in different way
import re
string='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y=re.findall('^From .*@([^ ]*)',string)
print(y)
