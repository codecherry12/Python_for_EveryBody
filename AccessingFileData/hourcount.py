'''10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and
 then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''
file_name=input("Enter the file name:")#filetest2.txt
hour_count=dict()
lst=list()
if len(file_name)<1:
    file_name="filetest2.txt"
fh=open(file_name)
for line in fh:
    x=line.rstrip()
    if x.startswith("From "):
        list=x.split()
        y=list[5].split(":")
        lst.append(y[0])
for hour in lst:
    hour_count[hour]=hour_count.get(hour,0)+1
for k,v in sorted(hour_count.items()):
    print(k,v)
