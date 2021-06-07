"""7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name"""
file_name=input("enter the file name:")
file=open(file_name,"r")
count=0
s=0
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        x=line[20:]
        y=float(x.rstrip())
        s=s+y
        count+=1
avg=s/count
print("Average spam confidence:",avg)
