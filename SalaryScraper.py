#Salary Scraper
import libStuff
import collections

#todo finish template
#Salary = collections.namedtuple('Signup', 'firstName lastName address1 address2 city state zip phone email classId date time paid seatCost notes className seats groupId agentName agentCompany')

def scrape(br):
	salaries = []
	
	#todo place url
	soup = libStuff.getSoup(br, 'http://thepaintmixer.com/admin/viewdailysignups.php')

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
