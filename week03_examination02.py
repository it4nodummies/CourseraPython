import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Mickey.html'
count = 7
position = 18

for followLink in range(count):
    positionLink = 0
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        positionLink += 1

        
        if positionLink == position:
            print 'Contents:',tag.contents[0]
            url = tag.get('href', None)
        