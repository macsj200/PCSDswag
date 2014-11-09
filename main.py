'''
site nommer
so i don't have to do it
'''

'''
import dailySignupScraper
import cardScraper
'''
import SalaryScraper
import libStuff
import sys

'''
if len(sys.argv) != 3:
	raise ValueError('You need to pass username and password as arguments')
'''

exportFile = open('SalaryScraperExports.json', 'w')
url = sys.argv[1]
br = libStuff.getPage(url)
libStuff.writeListToFile(exportFile, SalaryScraper.scrape(br))
