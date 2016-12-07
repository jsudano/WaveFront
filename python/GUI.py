# A hacked-together GPU. It's messy as hell, but it works???
import Tkinter as tk
import ctypes
from PIL import Image, ImageTk

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

		# Attach the image to a canvas so it doesn't get GC'd
		# Also, need a canvas to register mousey clicks
		self.canvas = tk.Canvas(root, background = 'white', 
							width = self.IMAGE_WIDTH, 
							height = self.IMAGE_HEIGHT)
		canvas = self.canvas
		canvas.create_image((0,0), anchor = 'nw', image = photo) # keep a reference!

		# Configure text
		self.prev_var = tk.StringVar(value='-:-')
		labels = tk.Frame(root)
		labels.pack()
		tk.Label(labels, text='Last Point Clicked: ').pack(side=tk.LEFT)
		prev = tk.Label(labels, textvariable=self.prev_var)
		prev.pack(side=tk.LEFT)

		# Set canvas to check for left-click and record coordinates
		self.canvas.bind('<Button-1>', self.on_click)

		root.config(cursor="dotbox")

		canvas.pack() #add image to root 
		root.mainloop()

	# Handler function for left-click
	def on_click(self, event):
		last_point = event.x, event.y
		self.prev_var.set('%s:%s' % last_point)
		self.calcCoords(last_point)

	def calcCoords(self, point):
		a = 0

intf = Interface()