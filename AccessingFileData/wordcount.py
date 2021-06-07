file_name=input("Enter the file_name:")#enter filelist.txt
fh=open(file_name)
counts=dict()
for line in fh:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,"-->",bigcount)
