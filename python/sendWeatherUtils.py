# Takes two ints, makes them into a concatenated digit array
def digitArray(sr, ss):
	melody = []
	while sr:
	    melody.insert(0, (sr % 10))
	    sr //= 10
	while ss:
		melody.insert(0, (ss % 10))
		ss //= 10
	return melody