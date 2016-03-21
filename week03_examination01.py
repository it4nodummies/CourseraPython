import urllib
import re
from BeautifulSoup import *

# url = raw_input('Enter - ')
url = 'http://python-data.dr-chuck.net/comments_256139.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')

numlist = list()

for tag in tags:
    print tag.contents[0]
    num = int(tag.contents[0])
    numlist.append(num)

print sum(numlist)