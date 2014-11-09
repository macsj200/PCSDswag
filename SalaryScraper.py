#Salary Scraper
import libStuff
import collections
from mechanize import Browser
from bs4 import BeautifulSoup

#todo finish template
#Salary = collections.namedtuple('Signup', 'firstName lastName address1 address2 city state zip phone email classId date time paid seatCost notes className seats groupId agentName agentCompany')

def scrape(url):
	salaries = []

	br = Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Firefox')]
	
	html = br.open(url).read()
	soup = BeautifulSoup(html)

	'''
	table = soup.find(id='Calendar')
	rows = table.find_all('tr')
	#todo fill in table logic
	rowNumber = 0
	for row in rows:
		if rowNumber == 0:
			rowNumber = rowNumber + 1
			continue
		cells = row.find_all('td')
		cells = [cell.string if cell.string != None else '' for cell in cells]
		signup = Signup(*cells)
		signups.append(signup)
	return signups
	'''

def getPage(url):
	br = Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Firefox')]
	br.open(url)
	return br

scrape('http://google.com')