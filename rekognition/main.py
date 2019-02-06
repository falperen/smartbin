#!/usr/bin/python3
import pprint as pp
import Rekognition
import subprocess
import os


DIRECTORY = '~/pictures/'
WEBCAM = '~/smartbin/scripts/webcam.sh'

RASP = False

imagePath = '~/Downloads/empty3.png'
waste = None
photoTime = 0
is_running = True

def parseWaste(key):
	if(key == '1'):
		return 'UNSORTED'
	elif(key == '2'):
		return 'PLASTIC'
	elif(key == '3'):
		return 'PAPER'
	elif(key == '4'):
		return 'GLASS'
	else:
		return 'UNSORTED'

if __name__ == "__main__":
	reko = Rekognition.Rekognition(True)
	while(is_running):
		if(RASP):
			waste = raw_input('picture?')
			waste = parseWaste(waste)
			photoTime = time.time()
			file_name = subprocess.check_output(os.path.expanduser(WEBCAM))
			file_name = os.path.expanduser(DIRECTORY)+str(file_name)[:-1]
			photoTime = time.time() - photoTime
		else: 
			file_name = imagePath

		print file_name
		waste_type = reko.getLabels(os.path.expanduser(file_name))
		
		if(waste_type != waste):
			#cheat
			print(waste)
		else:
			#true
			print(waste_type)

		reko.timeoutRecap(photoTime)
		if(not RASP):
			is_running = False

