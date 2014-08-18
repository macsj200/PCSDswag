'''
site nommer
so i don't have to do it
'''
import dailySignupScraper
import libStuff
import sys

if len(sys.argv) != 3:
	raise ValueError('You need to pass username and password as arguments')

exportFile = open('paintMixerExports.json', 'w')
libStuff.writeListToFile(exportFile, dailySignupScraper.scrape(libStuff.login(sys.argv[1], sys.argv[2])))
