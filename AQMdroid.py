import Tkinter
from Tkinter import *
from PIL import ImageTk, Image
from layout import UIDump
from Event_Listener import Sniffer
from Replicator import Replicator
from Device import Device

class AQMdroid(object):

	def __init__(self, img_path, img_dim, filename):
		""" initializes the device screen settings."""
		super(AQMdroid, self).__init__()
		
		UIDump.bounds = list()
		UIDump.elements.clear()
		UIDump.check_className.clear()
		UIDump.check_text.clear()
		UIDump.check_unique_id.clear()
		UIDump.check_resource_id.clear()
		
		self.window = Tkinter.Toplevel()
		self.img_path = img_path
		self.img_dim = img_dim
		self.curr_screen_bounds = UIDump().get_ui_dump()
		self.filename = filename
		self.launch()

	def close_Button(self):
		self.window.destroy()

		Device().capture_screenshot()
		droid = AQMdroid(self.img_path, self.img_dim, self.filename)
		
		try:
			droid.getorigin()
		except Exception as e:
			print "\nFrame Clossed."
		
	def getorigin(self, eventorigin):
	      """the main method that compares user clicks to the element of contact."""
	      global x,y
	      x = eventorigin.x*3
	      y = eventorigin.y*3

	      Sniffer(list((x,y))).bounds_Compare(self.curr_screen_bounds, self.filename)
	      Replicator(list((x,y))).replicate()
	      import time
	      time.sleep(2)
	      self.close_Button()

	def load_screen(self, image_path, image_dimension):
		"""displays the device screen"""

		raw_image = Image.open(image_path)
		smooth_image = raw_image.resize(((image_dimension[0]/3), (image_dimension[1]/3)), Image.ANTIALIAS)
		img = ImageTk.PhotoImage(smooth_image)
		panel = Tkinter.Label(self.window, image = img)
		panel.pack(side = "bottom", fill = "both", expand = "yes")
		self.window.bind("<Button 1>", self.getorigin)
		self.window.resizable(0,0)
		self.window.mainloop() 

	def launch(self):
		"""main method,  execution starts from this point."""
		self.load_screen(self.img_path, self.img_dim)

if __name__ == '__main__':
	path = 'image.png'
	res = (1080, 1920)
	AQMdroid(path, res)