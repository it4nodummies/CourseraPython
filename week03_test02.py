import urllib
import xml.etree.ElementTree as ET
# from week04_examination01 import listResult

url = 'http://python-data.dr-chuck.net/comments_256136.xml'


uh = urllib.urlopen(url)
data = uh.read()

print data

stuff = ET.fromstring(data)
listResult = stuff.findall('comments/comment')

listCount = list()

for item in listResult:
    count = int(item.find('count').text)
    listCount.append(count)

print 'Sum:', sum(listCount)

