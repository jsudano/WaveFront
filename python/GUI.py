#HelloWorld.py
import Tkinter as tk
import ctypes
from PIL import Image, ImageTk

# Get monitor size
user32 = ctypes.windll.user32
SCR_WIDTH = user32.GetSystemMetrics(0) 
SCR_HEIGHT = user32.GetSystemMetrics(1)
WINDOW_WIDTH = int(SCR_WIDTH / 1.5)
WINDOW_HEIGHT = int(SCR_HEIGHT / 1.5)

# Declare root window, set size
root = tk.Tk()
root.geometry('{}x{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))

# Load image, resize, and convert to tk-compatible format
image = Image.open("../resources/EQR_world_map.jpg")
maxSize = (WINDOW_WIDTH, WINDOW_HEIGHT)
image.thumbnail(maxSize, Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image) 

# Attach the image to a lable so it doesn't get GC'd
label = tk.Label(image=photo)
label.image = photo # keep a reference!

root.config(cursor="dotbox")

label.pack() #add image to root 
root.mainloop()
