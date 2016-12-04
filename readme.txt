Requirements:
	- Python 2.7
	- Max MSP

Dependencies:
	- Other than Ilya's pyOSC package, I used one external library: requests. I apologize for not including it in the zip. To install it, use pip:
		
	pip install requests


To run, open bodyPatch.maxpat and activate sound. I apologize for the mess of aseq errors which will arise, I couldn't find an elegant way to handle them. After that, 
run: 
	python/sendWeather.py

It will begin playing belltones, based on weather data taken from 4 locations. These 4 locations are chosen randomly out of 16 pre-selected locations across the globe.
For my final project, I hope to flesh this out and create a sound (or "composition") which is more dynamic and evocative of weather. I feel that this is a good 
prototype version of what will become a much more robust data sonification engine, with a fair amount of tweaking, development, and redevelopment.  


Known errors:
	- Since I use Windows, I am stuck with the 32-bit version of Max. I was getting a lot of clipping and sound-lag that I just couldn't seem to fix, and I hope a
	fair amount of that boils down to the lack of available resources. I'm sure some of it is also due to my inexperience.
	- jit.buffer~ - matrix etc... This is another error I ran into, and spend a lot of time working down. I tried my best to split up OSC packages to mitigate this
	but I found myself stuck between a desired sound and a console devoid of error messages.
	- I had a little trouble allowing Python to bypass my firewall, so that may be something to look out for. 

Features I would like to add to the Final Version:
	- More natural/dynamic volume and phrasing
	- More diverse harmonies
	- More creative use of data (this may require a more reliable/predictable API, as the one I am currently using has some frustrating quirks)
	- More voices
	- More blended, natural sound
	- Less bugs, clipping, lag