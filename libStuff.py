from mechanize import Browser
from bs4 import BeautifulSoup
import json

def login(username, password):
	br = Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Firefox')]
	br.open('http://thepaintmixer.com/admin/?stat=1&nm=' + username +  '&pd=' + password)
	return br

def getSoup(br, url):
	html = br.open(url).read()
	soup = BeautifulSoup(html)
	return soup
	
def writeListToFile(exportFile, data):
	jsonified = json.dumps(data, default=lambda o: o.__dict__)
	
	exportFile.write(jsonified)
