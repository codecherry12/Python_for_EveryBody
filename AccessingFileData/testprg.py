fname=input("enter file name:")
count=0
try:
    file=open(fname,"r")
except:
    print("file name is not valid:",fname)
#for line in file:
#    count=count+1
#print(count)
x=file.read()
print(x)
