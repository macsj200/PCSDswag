import requests
import json
from bs4 import BeautifulSoup
from subprocess import call
from mechanize import Browser


class CardHolder:
	def __init__(self, firstName, lastName, email):
		self.firstName = firstName
		self.lastName = lastName
		self.email = email

class GiftCard:
	def __init__(self, cardNumber, cardHolder, balance, pin, datePurchased, charitable, notes, amount, price):
		self.cardNumber = cardNumber
		self.cardHolder = cardHolder
		self.balance = balance
		self.pin = pin
		self.datePurchased = datePurchased
		self.charitable = charitable
		self.notes = notes
		self.amount = amount
		self.price = price

def login(username, password):
	br = Browser();
	br = Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Firefox')]
	br.open('http://thepaintmixer.com/admin/?stat=1&nm=' + username +  '&pd=' + password)
	return br

def export(exportFile):
	cards = []

	html = login('Americansaddler12', 'paintmixer12').open('http://thepaintmixer.com/admin/viewgiftcards.php').read()
	soup = BeautifulSoup(html)

	table = soup.find('table', 'borderTable')
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
			
		cardHolder = CardHolder(firstName, lastName, email)
		giftCard = GiftCard(cardNumber, cardHolder, balance, pin, datePurchased, charitable, notes, amount, price)
		cards.append(giftCard)

	jsonified = json.dumps(cards, default=lambda o: o.__dict__)
	
	exportFile.write(jsonified)
