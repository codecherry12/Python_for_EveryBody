'''hand=open('filetest2.txt')
for line in hand:
    line=line.rstrip()
    if line.startswith('From:'):
        print(line)'''
#both above and below programs gives the same output
import re
hand =open('filetest2.txt')
for line in hand:
    line=line.rstrip()
    if re.search('^From:',line):
        print(line)
