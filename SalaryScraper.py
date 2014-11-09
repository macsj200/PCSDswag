#Salary Scraper
import libStuff
import collections
import json
from mechanize import Browser
from bs4 import BeautifulSoup
from urlparse import urlparse

#todo finish template
Salary = collections.namedtuple('Salary', 'name position department grossCompensation')

def getSalaries():
	salaries = scrape('http://www.utahsright.com/salaries.php?city=pc_schools&query=')
	return salaries

def scrape(url):
	salaries = []

	br = Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Firefox')]
	
	html = br.open(url).read()
	soup = BeautifulSoup(html)

	imgs = soup.find_all('img')

	lastPage = 0

	for img in imgs:
		if img['src'] == 'images/en_last.jpg':
			lastPage = img.parent['href'].split('=')
			lastPage = lastPage[len(lastPage) - 1]
	print lastPage

	for pageNumber in range(int(lastPage)):
		pageNumber = pageNumber + 1
		html = br.open(url + '&page=' + str(pageNumber)).read()
		soup = BeautifulSoup(html)

		table = soup.find('table', 'dataTable')

		rows = table.find_all('tr')
		rowNumber = 0
		for row in rows:
			if rowNumber == 0:
				rowNumber = rowNumber + 1
				continue
			cells = row.find_all('td')

			names = cells[0]
			names = names.span
			names = [unicode(name.string).strip() if name.string != None else '' for name in names]

			cells = [unicode(cell.string).strip() if cell.string != None else '' for cell in cells]

			i = 0
			for name in names:
				cells[i] = name

				i = i + 1

			salary = Salary(*cells)
			salaries.append(salary)
		print salaries

	return salaries


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
		salary = Salary(*cells)
		signups.append(signup)
	'''
	return salaries
	

def getPage(url):
	br = Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Firefox')]
	br.open(url)
	return br

salaries = getSalaries()

exportFile = open('SalaryScraperExports.json', 'w')
jsonified = json.dumps(salaries, default=lambda o: o.__dict__)
exportFile.write(jsonified)