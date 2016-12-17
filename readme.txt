Requirements:
	- Python 2.7
	- Max MSP

Dependencies (non-default python libraries):
	- requests ("pip install requests")
	- PIL ("pip install pillow")


To run, open max/Play.maxpat and activate sound. then run python/sendWeather.py

It will begin playing an assortment of chimes based on the 50 nearest measurement nodes to your selected location.

Unfortunately, it is not perfect, and it may not run on a mac at the moment. This is because I used a Windows-specific method for getting screen dimensions. I apologize.
