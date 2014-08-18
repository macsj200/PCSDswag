import libStuff

class Address:
	def __init__(self, address1, address2, city, state, zip):
		self.address1 = address1
		self.address2 = address2
		self.city = city
		self.state = state
		self.zip = zip

class Signup:
	def __init__(self, registrant, classId, date, time, paid, seatCost, notes, className, seats, groupId, agentName, agentCompany):
		self.registrant = registrant
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
					firstName = cell.contents[0]
				except IndexError:
					firstName = None
			elif cellNumber == 1:
				try:
					lastName = cell.contents[0]
				except IndexError:
					lastName = None
			elif cellNumber == 2:
				try:
					address1 = cell.contents[0]
				except IndexError:
					address1 = None
			elif cellNumber == 3:
				try:
					address2 = cell.contents[0]
				except IndexError:
					address2 = None
			elif cellNumber == 4:
				try:
					city = cell.contents[0]
				except IndexError:
					city = None
			elif cellNumber == 5:
				try:
					state = cell.contents[0]
				except IndexError:
					state = None
			elif cellNumber == 6:
				try:
					zip = cell.contents[0]
				except IndexError:
					zip = None
			elif cellNumber == 7:
				try:
					phone = cell.contents[0]
				except IndexError:
					phone = None
			elif cellNumber == 8:
				try:
					email = cell.contents[0]
				except IndexError:
					email = None
			elif cellNumber == 9:
				try:
					classId = cell.contents[0]
				except IndexError:
					classId = None
			elif cellNumber == 10:
				try:
					date = cell.contents[0]
				except IndexError:
					date = None
			elif cellNumber == 11:
				try:
					time = cell.contents[0]
				except IndexError:
					time = None
			elif cellNumber == 12:
				try:
					paid = cell.contents[0]
				except IndexError:
					paid = None
			elif cellNumber == 13:
				try:
					seatCost = cell.contents[0]
				except IndexError:
					seatCost = None
			elif cellNumber == 14:
				try:
					notes = cell.contents[0]
				except IndexError:
					notes = None
			elif cellNumber == 15:
				try:
					className = cell.contents[0]
				except IndexError:
					className = None
			elif cellNumber == 16:
				try:
					seats = cell.contents[0]
				except IndexError:
					seats = None
			elif cellNumber == 17:
				try:
					groupId = cell.contents[0]
				except IndexError:
					groupId = None
			elif cellNumber == 18:
				try:
					agentName = cell.contents[0]
				except IndexError:
					agentName = None
			elif cellNumber == 19:
				try:
					agentCompany = cell.contents[0]
				except IndexError:
					agentCompany = None
			cellNumber = cellNumber + 1

		address = Address(address1, address2, city, state, zip)
		registrant = Registrant(firstName, lastName, address, phone, email)
		signup = Signup(registrant, classId, date, time, paid, seatCost, notes, className, seats, groupId, agentName, agentCompany)
		signups.append(signup)
	return signups
