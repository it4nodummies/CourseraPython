import re

hand = open('regex_sum_256134.txt')
numlist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    
    for n in range(len(stuff)) :
        num = int(stuff[n])
        print num
        numlist.append(num)

print 'Sum: ', sum(numlist)




