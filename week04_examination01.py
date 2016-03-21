import urllib
import xml.etree.ElementTree as ET

url = 'https://maps.googleapis.com/maps/api/geocode/xml?&address=rome'

fhand = urllib.urlopen(url)
data = fhand.read()
print data

stuff = ET.fromstring(data)
listResult = stuff.findall('result')
print 'Result:', len(listResult)

for item in listResult:
    print 'formatted_address:', item.find('formatted_address').text
    print 'lat:', item.find('geometry').find('location').find('lat').text
    print 'lng:', item.find('geometry').find('location').find('lng').text
    
    