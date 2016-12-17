# A hacked-together GPU. It's messy as hell, but it works???
import Tkinter as tk
import ctypes
from PIL import Image, ImageTk
from utils import *
import sendWeather as sw

class Interface():
	def __init__(self):
		self.getScreenSize()
		self.initialize()

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
		self.status_var = tk.StringVar(value = 'Click a spot on the map to hear its weather')
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
		coords = CalcCoords(last_point, self)
		
		json = FetchWeather(coords, self)
		if(isinstance(json, int)):
			return
		dic = mineJson(json)
		freqs = genFreqs(dic)

		self.status_var.set('Now playing!')
		self.send = sw.SendWeather(freqs)


	def getScreenSize(self):
		# Get monitor size
		user32 = ctypes.windll.user32
		self.SCR_WIDTH = user32.GetSystemMetrics(0) 
		self.SCR_HEIGHT = user32.GetSystemMetrics(1)
		self.WINDOW_WIDTH = int(self.SCR_WIDTH / 1.5)
		self.WINDOW_HEIGHT = int(self.SCR_HEIGHT / 1.5)



Interface()