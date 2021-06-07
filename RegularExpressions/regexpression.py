'''^  -->matches the beginning of a line
   $  -->Matches the end of the line
   .  -->Matches any character
   \s -->Matches whitespace
   \S -->Matches any non-whitespace character
   *  -->Repeats a character Zero or more times
   *? -->Repeats a character Zero or more times(non-greedy)
   +  -->Repeats a character one or more times
   +? -->Repeats a character one or more times(non-greedy)
   [aeiou]-->Matches a single characters in the lister set
   [^xyz]--->Matches a single character not in the listed set
   [a-z0-9]-->The set of characters can include a range
   (  --> Indicates where string extraction is to start
   )  --> Indicates where string exctraction is to end'''







"""hand = open('filetest2.txt')
#print(hand)
for line in hand:
    line= line.rstrip()
    #print(line.find('From:'))
    if line.find('From:')>=0:
        print(line)"""
#above program is similar to below porgram
import re
hand = open('filetest2.txt')
for line in hand:
    line= line.rstrip()
    if re.search('From:',line):
        print(line)
