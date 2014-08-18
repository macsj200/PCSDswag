import libStuff

class Signup:
	def __init__(self, registrant, classId, date, time, paid, seatCost, notes, className, seats, groupId, agentName, agentCompany):
		self.registrant
		self.classId = classId
		self.date = date
		self.time = time
		self.paid = paid
		self.seatCost = seatCost
		self.notes = notes
		self.className = className
		self.seats = seats
		self.groupId = groupId
		self.agentName = agentName
		self.agentCompany = agentCompany
		
class Registrant:
	def __init__(self, firstName, lastName, address, phone, email):
		self.firstName = firstName
		self.lastName = lastName
		self.address = address
		self.phone = phone
		self.email = email

def scrape(br):
	signups = []
	
	soup = libStuff.getSoup(br, 'http://thepaintmixer.com/admin/viewdailysignups.php')

	table = soup.find(id='Calendar')
	rows = table.find_all('tr')
	rowNumber = 0
	for row in rows:
		if rowNumber == 0:
			rowNumber = rowNumber + 1
			continue
		cells = row.find_all('td')
		cellNumber = 0
		for cell in cells:
			if cellNumber == 0:
				try:
					cardNumber = cell.contents[0]
				except IndexError:
					cardNumber = None
			elif cellNumber == 1:
				try:
					firstName = cell.contents[0]
				except IndexError:
					firstName = None
			elif cellNumber == 2:
				try:
					lastName = cell.contents[0]
				except IndexError:
					lastName = None
			elif cellNumber == 3:
				try:
					email = cell.contents[0]
				except IndexError:
					email = None
			elif cellNumber == 4:
				try:
					balance = cell.contents[0]
				except IndexError:
					balance = None
			elif cellNumber == 5:
				try:
					pin = cell.contents[0]
				except IndexError:
					pin = None
			elif cellNumber == 6:
				try:
					datePurchased = cell.contents[0]
				except IndexError:
					datePurchased = None
			elif cellNumber == 7:
				try:
					charitable = cell.contents[0]
				except IndexError:
					charitable = None
			elif cellNumber == 8:
				try:
					notes = cell.contents[0]
				except IndexError:
					notes = None
			elif cellNumber == 9:
				try:
					amount = cell.contents[0]
				except IndexError:
					amount = None
			elif cellNumber == 10:
				try:
					price = cell.contents[0]
				except IndexError:
					price = None
			cellNumber = cellNumber + 1
		
		registrant = Registrant(firstName, lastName, address, phone, email)
		signup = Signup(registrant, classId, date, time, paid, seatCost, notes, className, seats, groupId, agentName, agentCompany)
		signups.append(signup)
	return signups
