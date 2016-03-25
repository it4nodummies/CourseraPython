import urllib
import json
from urllib import urlencode
from OpenSSL.rand import status

serviceUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: taranto')
    if len(address) < 1:
        break
    url = serviceUrl + urllib.urlencode({'sensor' : 'false', 'address':address})
    print 'Retrieving:', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrivied:',len(data),'characters'
    
    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK' :
        print 'Failure to retrieve!'
        print data
        continue
    
    print json.dumps(js, indent=4)
    
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    
    print 'lat:', lat
    print 'lng:', lng
    location = js['results'][0]['formatted_address']
    print location