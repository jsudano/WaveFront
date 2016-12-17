from OSC 	import OSCClient, OSCBundle
from time 	import sleep
from utils	import *

class SendWeather():
	def __init__(self, data):
		time = data['time']

		# Open Client
		client = OSCClient()
		client.connect(("localhost", 54345))

		# Send noise data to max
		nBundle = OSCBundle()
		nBundle.append({'addr':"/high/freq", 'args':data['highF']})
		nBundle.append({'addr':"/mid/freq", 'args':data['midF']})
		nBundle.append({'addr':"/low/freq", 'args':data['lowF']})
		client.send(nBundle)

		# Send randomized duration data
		dBundle = OSCBundle()
		dBundle.append({'addr':"/high/dur", 'args':distRhythm(time, 4)})
		dBundle.append({'addr':"/mid/dur", 'args':distRhythm(time, 2)})
		dBundle.append({'addr':"/low/dur", 'args':distRhythm(time, 1)})
		client.send(dBundle)

		
