'''9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
 The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
 The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
  After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''
file_name=input("enter the file name:")#enter filetest2.txt
fh=open(file_name)
list=[]
counts={}
for line in fh:
    line.strip()
    if line.startswith('From '):
        x=line.split()
        list.append(x[1])
print(list)
for mail in list:
    counts[mail]=counts.get(mail,0)+1
print(counts)
bigmail=None
bigcount=None
for i,j in counts.items():
    if bigcount is None or j>bigcount:
        bigmail=i
        bigcount=j
print(bigmail,bigcount)
