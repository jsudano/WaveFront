# A hacked-together GPU. It's messy as hell, but it works???
import Tkinter as tk
import ctypes
from PIL import Image, ImageTk
import owmAPI as owm 
from math import *

class Interface():
	def __init__(self):
		self.getScreenSize()
		self.initialize()

	def getScreenSize(self):
		# Get monitor size
		user32 = ctypes.windll.user32
		self.SCR_WIDTH = user32.GetSystemMetrics(0) 
		self.SCR_HEIGHT = user32.GetSystemMetrics(1)
		self.WINDOW_WIDTH = int(self.SCR_WIDTH / 1.5)
		self.WINDOW_HEIGHT = int(self.SCR_HEIGHT / 1.5)

	def initialize(self):
		# Declare root window, set size
		self.root = tk.Tk()
		root = self.root # Damn right I'm so lazy I waste space in the stack
		root.geometry('{}x{}'.format(self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
		root.resizable(width=False, height=False) # Copout so I can't resize

		# Load image, resize, and convert to tk-compatible format
		image = Image.open("../resources/EQR_world_map.jpg")
		maxSize = (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
		image.thumbnail(maxSize, Image.ANTIALIAS)
		photo = ImageTk.PhotoImage(image)
		# Save image size as class variable
		self.IMAGE_WIDTH = image.size[0]
		self.IMAGE_HEIGHT = image.size[1] 

		# Configure text
		self.prev_var = tk.StringVar(value='-:-')
		self.status_var = tk.StringVar(value = 'Select an area on the map to hear its weather')
		labels = tk.Frame(root, cursor = 'dotbox', height = self.WINDOW_HEIGHT,
						width = self.WINDOW_WIDTH)
		labels.pack(side = 'bottom')
		tk.Label(labels, text='Selected Coordinates: ').pack(side='left')
		prev = tk.Label(labels, textvariable=self.prev_var)
		prev.pack(side='left')
		tk.Label(labels, text = 'Status:').pack(side = 'left')
		status = tk.Label(labels, textvariable = self.status_var)
		status.pack(side='left')


		# Attach the image to a canvas so it doesn't get GC'd
		# Also, need a canvas to register mousey clicks
		self.imageCanvas = tk.Canvas(root, background = 'white', 
							width = self.IMAGE_WIDTH, 
							height = self.IMAGE_HEIGHT)
		imageCanvas = self.imageCanvas
		imageCanvas.create_image((0,0), anchor = 'nw', image = photo) # keep a reference!

		

		# Set canvas to check for left-click and record coordinates
		imageCanvas.bind('<Button-1>', self.OnClick)

		root.config(cursor="arrow")

		imageCanvas.pack() #add image to root 
		root.mainloop()

	# Handler function for left-click
	def OnClick(self, event):
		last_point = (event.x, event.y)
		coords = self.CalcCoords(last_point)
		
		json = self.FetchWeather(coords)
		
		# Data parsing time


	# Calculates coordinates from an input tuple of X, Y pixels
	def CalcCoords(self, point):
		self.status_var.set('Calculating Coordinates')
		x = point[0]
		y = point[1]

		dispPM = x - 640.5 # These are the pixel locations relative to EQ and PM
		dispEQ = 322.5 - y

		longitude = dispPM * (360 / 1280.0)
		latitude = dispEQ * (180 / 644.0)
		self.prev_var.set('{0} : {1}'.format(latitude, longitude))

		# Return a tuple (latitude, longitude)
		return (latitude, longitude)


	# Fetches data from API (may need to parse it here too)
	def FetchWeather(self, point):
		self.status_var.set('Fetching weather data from 50 nearest nodes')
		self.root.update_idletasks() # Force update of text variables in root

		try:
			node = owm.owmAPI(point)
		except TypeError:
			print("Input of values to API failed, check type")
			self.status_var.set("An error occurred during data fetch." + 
								" See console for details")
			return

		json = node.Fetch()
		if (json == -1):
			self.status_var.set("An error occurred during data fetch." + 
								" See console for details")
			return -1
		elif (json == -2):
			self.status_var.set("Insufficient data for selected coordinates." +
								" Try an area nearer to civilization")
		elif(isinstance(json, dict)):
			self.status_var.set("Data Success!")



intf = Interface()