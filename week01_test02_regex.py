import re
# from distutils.filelist import findall

x = "i miei 2 numeri preferiti sono il 3 edil 42"
y = re.findall("[0-9]+", x)
print y 



x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print y 

x = 'From: ivano.turi@me.com    Sat Jan 5 12:34:32 2016'
y = re.findall('@(\S+)', x)
print y

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@(\S+)', x)
print y

x = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
y = re.findall('href="(.+)"', x)
print y