import re
file_name=open('filetest2.txt')
numlist=list()
for line in file_name:
    line=line.rstrip()
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)#extracting the value after X-DSPAM-Confidence:
                                                           #  ( -->indicates starts extracting [0-9.]--> dot is a period
    if len(stuff)!=1:continue
    print(stuff,"==>",len(stuff))
    num=float(stuff[0])
    numlist.append(num)
print('Maximum',max(numlist))
