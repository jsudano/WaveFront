""" A set of utility functions for the gui """
import Tkinter as tk
import owmAPI as owm
import random as r

# Takes a huge dict of dicts of dicts of... 
# and turns the weather data into arrays of like values
def mineJson(data):
	temps = []
	tempMins = []
	tempMaxes = []
	tempRanges = []
	humidities = []
	pressures = []
	windspeeds = []
	headings = []
	clouds = []
	for di in data['list']:
		temps.append(di['main']['temp'])
		tempmin = di['main']['temp_min']
		tempmax = di['main']['temp_max']
		tempMins.append(tempmin)
		tempMaxes.append(tempmax)
		tempRanges.append(tempmax - tempmin)
		humidities.append(di['main']['humidity'])
		pressures.append(di['main']['pressure'])
		if ('wind' in di):
			windspeeds.append(di['wind']['speed'])
			headings.append(di['wind']['deg'])
		else:
			windspeeds.append(0)
			headings.append(0)
		if ('clouds' in di):
			clouds.append(di['clouds']['all'])
		else:
			clouds.append(0)

	return {'temps':temps, 'hum':humidities, 'pres':pressures, 
			'winds':windspeeds, 'head':headings, 'cloud':clouds,
			'tMin':tempMins, 'tMax':tempMaxes, 'tempR':tempRanges}

# Turn all that data into three sets of frequencies and a time in seconds
def genFreqs(data):
	pres = data['pres']
	time = (int(sum(pres)/len(pres))) * 8 # make it divisible by 4

	# Get high freqs
	wind = data['winds']
	deg = data['head']

	mod = [d % 10 for d in deg] # Use heading to randomize frequencies a bit
	for i in range(0, len(mod)):
		if (deg[i] > 180):
			mod[i] = -(mod[i])

	avgW = sum(wind)/len(wind)
	devW = [abs(avgW - w) for w in wind]
	highF = [((1000 * devW[i]) + 750 + (10 * mod[i])) for i in range(0, len(devW))]
	randZero(highF, 0.25) # 25% chance of a frequency becoming a rest
	
	# Get mid freqs
	temp = data['temps']
	tRan = data['tempR']

	midF = [(200 + temp[i] + (30 * (tRan[i] % 10))) for i in range(0, len(temp))]
	randZero(midF, .15)

	# Get low freqs
	hum = data['hum']
	lowF = [int((1.5 * hum[i] + (pres[i] % 100) * (pres[i] % 10))) for i in range(0, len(hum))]
	randZero(lowF, .05)

	return {'time':time, 'highF':highF, 'midF':midF, 'lowF':lowF}

# Zeroes an element in a list with probability PROB
def randZero(l, prob):
	for i in range(0, len(l)):
		if r.randint(0, 100) < (100 * prob):
			l[i] = 0

# Calculates coordinates from an input tuple of X, Y pixels
def CalcCoords(point, gui):
	gui.status_var.set('Calculating Coordinates')
	x = point[0]
	y = point[1]

	dispPM = x - 640.5 # These are the pixel locations relative to EQ and PM
	dispEQ = 322.5 - y

	longitude = dispPM * (360 / 1280.0)
	latitude = dispEQ * (180 / 644.0)
	gui.prev_var.set('{0} : {1}'.format(latitude, longitude))

	# Return a tuple (latitude, longitude)
	return (latitude, longitude)

# Fetches data from API (may need to parse it here too)
def FetchWeather(point, gui):
	gui.status_var.set('Fetching weather data from 50 nearest nodes')
	gui.root.update_idletasks() # Force update of text variables in root

	try:
		node = owm.owmAPI(point)
	except TypeError:
		gui.status_var.set("Data fetch failed." + 
							" See console for details or" + 
							" check connection and try again")
		return

	json = node.Fetch()
	if (json == -1):
		gui.status_var.set("An error occurred during data fetch." + 
							" See console for details")
		return -1
	elif (json == -2):
		gui.status_var.set("Insufficient data for selected coordinates." +
							" Try an area nearer to civilization")
		return -2
	elif(isinstance(json, dict)):
		gui.status_var.set("Data Success!")
		return json

# Randomly picks values distributed within subd within meas
def distRhythm(meas, subd):
	times = []
	for i in range(0, subd):
		s = meas / subd
		distHelp(s, s, times)
	return times

# Recursive helper for distRhythm
def distHelp(num, start, times):
	if not num:
		return
	elif num <= start / 4:
		times.append(num)
	else:
		m = start / 8
		new = r.randint(m, num - m) # Never less than 1/8th subdivision
		times.append(new)
		distHelp(num - new, start, times)
