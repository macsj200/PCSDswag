'''
site nommer
so i don't have to do it
'''
import dailySignupScraper
import cardScraper
import libStuff
import sys

if len(sys.argv) != 3:
	raise ValueError('You need to pass username and password as arguments')

exportFile = open('paintMixerExports.json', 'w')
libStuff.writeListToFile(exportFile, cardScraper.scrape(libStuff.login(sys.argv[1], sys.argv[2])))
