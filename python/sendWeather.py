from OSC 	import OSCClient, OSCBundle
from owmAPI import owmAPI
from random import randint
from time 	import sleep
from sendWeatherUtils import *

# ID Dictionary used for data retreival
ID_ARRAY = ["5327684", "2648579", "2253354", "5392323", "1816670", "5128581",
			"6693229", "6255152", "2673730", "2193733", "524901" , "1857910",
			"3703443", "456172" , "993800" , "1609350"]

# ID:City dictionary used for console printing
ID_DICT = {"5327684":"UC Berkeley, California", "2648579":"Glasgow, Scotland",
			"2253354":"Dakar, Senegal", 
			"5392323":"San Luis Obispo, California",
			"1816670":"Beijing, China", "5128581":"New York, New York",
			"6693229":"San Nicolas, Argentina", "6255152":"Antarctica",
			"2673730":"Stockholm, Sweden", "2193733":"Auckland, New Zealand",
			"524901":"Moscow, Russia" , "1857910":"Kyoto, Japan",
			"3703443":"Panama City, Panama", "456172":"Riga, Latvia",
			"993800":"Johannesburg, South Africa",
			"1609350":"Bangkok Thailand"}

client = OSCClient()
client.connect(("localhost", 54345))

# Main Loop
while True:
	id0 = ID_ARRAY[randint(0, 3)]
	id1 = ID_ARRAY[4 + randint(0, 3)]
	id2 = ID_ARRAY[8 + randint(0, 3)]
	id3 = ID_ARRAY[12 + randint(0, 3)]

	# Choose random nodes from length-4 chunks in array
	node0 = owmAPI(id0)
	node1 = owmAPI(id1)
	node2 = owmAPI(id2)
	node3 = owmAPI(id3)

	# Print current cities to console
	print("Fetching weather from:")
	print("{0} | {1} | {2} | {3}".format(ID_DICT[id0], ID_DICT[id1], 
										ID_DICT[id2], ID_DICT[id3]))
	
	# Create new bundle
	bundle = OSCBundle()

	# Get node0 data
	sys0 = node0.fetch('sys')
	main0 = node0.fetch('main')
	ms = main0['pressure']
	melody0 = digitArray(sys0['sunrise'], sys0['sunset'])
	voices0 = main0['humidity']
	spread0 = node0.fetch('wind')['speed']
	wave0 = int(node0.fetch('wind')['deg'] % 3)
	trem0 = int(main0['temp']) % 2
	trIn0 = main0['temp'] - 240
	vol0 = digitArray(int(main0['pressure']), int(main0['temp']))

	# Add node0 data to bundle
	bundle.append({'addr': "/ms", 'args': ms})
	bundle.append({'addr': "/mel/hz", 'args': melody0})
	bundle.append({'addr': "/mel/voices", 'args': voices0})
	bundle.append({'addr': "/mel/spread", 'args': spread0})
	bundle.append({'addr': "/mel/waveform", 'args': wave0})
	bundle.append({'addr': "/mel/tremolo", 'args': trem0})
	bundle.append({'addr': "/mel/tremInt", 'args': trIn0})
	bundle.append({'addr': "/mel/volumes", 'args': vol0})
	client.send(bundle)

	#Create another new bundle (yes, it has to be this way due to size limits)
	bundle1 = OSCBundle()

	# Get node1 data
	sys1 = node1.fetch('sys')
	main1 = node1.fetch('main')
	melody1 = digitArray(int(main1['temp']), int(main1['pressure']))
	voices1 = int(node1.fetch('wind')['speed']) * 3
	spread1 = main1['humidity'] / 20
	wave1 = int(node1.fetch('wind')['speed']) % 3
	trem1 = int(main1['temp']) % 2
	trIn1 = main1['temp'] - 250
	vol1 = digitArray(int(main1['temp']), 0)

	# Add node1 data to bundle
	bundle1.append({'addr': "/har1/hz", 'args': melody1})
	bundle1.append({'addr': "/har1/voices", 'args': voices1})
	bundle1.append({'addr': "/har1/spread", 'args': spread1})
	bundle1.append({'addr': "/har1/waveform", 'args': wave1})
	bundle1.append({'addr': "/har1/tremolo", 'args': trem1})
	bundle1.append({'addr': "/har1/tremInt", 'args': trIn1})
	bundle1.append({'addr': "/har1/volumes", 'args': vol1})
	client.send(bundle1)

	#Create another new bundle (yes, it has to be this way due to size limits)
	bundle2 = OSCBundle()

	# Get node2 data
	sys2 = node2.fetch('sys')
	main2 = node2.fetch('main')
	melody2 = digitArray(int(main2['temp']), int(main2['pressure']))
	voices2 = int(node2.fetch('wind')['speed']) * 3
	spread2 = main2['humidity'] / 20
	wave2 = int(node2.fetch('wind')['speed']) % 3
	trem2 = int(main2['temp']) % 2
	trIn2 = main2['temp'] - 250
	vol2 = digitArray(int(main2['temp']), 0)

	# Add node2 data to bundle
	bundle2.append({'addr': "/har2/hz", 'args': melody2})
	bundle2.append({'addr': "/har2/voices", 'args': voices2})
	bundle2.append({'addr': "/har2/spread", 'args': spread2})
	bundle2.append({'addr': "/har2/waveform", 'args': wave2})
	bundle2.append({'addr': "/har2/tremolo", 'args': trem2})
	bundle2.append({'addr': "/har2/tremInt", 'args': trIn2})
	bundle2.append({'addr': "/har2/volumes", 'args': vol2})
	client.send(bundle2)




	#Create another new bundle 
	bundle3 = OSCBundle()

	# Get node3 data
	sys3 = node3.fetch('sys')
	main3 = node3.fetch('main')
	melody3 = digitArray(int(node3.fetch('wind')['speed']), 0)
	voices3 = (int(node3.fetch('wind')['deg']) + 1) / 25
	spread3 = main3['humidity'] / 15
	wave3 = int(node3.fetch('wind')['speed']) % 3
	trem3 = int(main3['temp']) % 2
	trIn3 = main3['temp'] - 230
	vol3 = digitArray(int(main3['humidity']), 0)

	# Add node3 data to bundle
	bundle3.append({'addr': "/bass/hz", 'args': melody3})
	bundle3.append({'addr': "/bass/voices", 'args': voices3})
	bundle3.append({'addr': "/bass/spread", 'args': spread3})
	bundle3.append({'addr': "/bass/waveform", 'args': wave3})
	bundle3.append({'addr': "/bass/tremolo", 'args': trem3})
	bundle3.append({'addr': "/bass/tremInt", 'args': trIn3})
	bundle3.append({'addr': "/bass/volumes", 'args': vol3})
	client.send(bundle3)

	# Wait 30 seconds
	sleep(30)

