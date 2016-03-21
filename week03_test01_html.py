import urllib
import bs4


#url = raw_input('URL site - ')
url = 'http://python-data.dr-chuck.net/comments_42.html'

html = urllib.urlopen(url).read()
soup = bs4.BeautifulSoup(html, "html.parser")

tags = soup('span')

for tag in tags:
    #print tag.get('comment', None)    
    print tag