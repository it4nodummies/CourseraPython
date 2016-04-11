import urllib
import json



url = 'http://python-data.dr-chuck.net/comments_256140.json'


uh = urllib.urlopen(url)
data = uh.read()
print 'Retrivied:',len(data),'characters'

js = json.loads(str(data))
print json.dumps(js, indent=4)

count = 0
for item in js['comments']:
    count += item['count']
    
print 'Sum =', count


