import csv
import datetime

class announcer:
	def __init__(self, fileName):
		self.fileName = fileName

	def announce(self, initiator, command):
	    announcementRow = str(datetime.datetime.now()) + ":" + initiator + ":" + command 
	    print(announcementRow)
	    announcementRow += "\n" 
	    with open(self.fileName,'a') as file:
	        file.write(announcementRow)
	    
