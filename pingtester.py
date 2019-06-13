#! /usr/bin/env python
# Generates ISP connectivity log until stopped by user.
# Version 0.2

from datetime import datetime
import time
import os
import sys

hostname = 'someIPaddress'
logfile = open('pinglog.csv', 'w')
logfile.write('Test of: ' + os.uname()[1])
logfile.close()	

if len(sys.argv) == 1:
	interval = 60
else:
	if sys.argv[1].isdigit() == False:
		sys.exit('Usage: pinger.py [x] where x is an the number of seconds for ping interval.')	
	interval = float(sys.argv[1])

while 1 == 1:
	logfile = open('pinglog.csv', 'a')
	todaysDate = str(datetime.now())[:10]
	currentTime = str(datetime.now())[11:-10]
	response = os.system('ping -c 1 ' + hostname)
	if response == 0:
		logfile.write(todaysDate +',' + currentTime + '\n')
	else:
		logfile.write(todaysDate +',' + currentTime + ' lost connection'+ '\n')
		print hostname, 'lost connection'
	logfile.close()
	
	time.sleep(interval)
