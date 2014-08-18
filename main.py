'''
site nommer
so i don't have to do it
'''
import cardScraper

exportFile = open("paintMixerExports.json", "w")
cardScraper.export(exportFile)
