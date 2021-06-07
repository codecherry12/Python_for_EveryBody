#regexpression_sum.py code in less number of steps using list comprehension
import re
print(sum([int(i) for i in re.findall('[0-9]+',open('regexpression1.txt').read()) ]))
