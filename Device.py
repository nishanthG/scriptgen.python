class Device(object):
	"""docstring for ClassName"""
	width = 0
	height = 0

	def __init__(self):
		super(Device, self).__init__()
		
	def capture_screenshot(self):
		"""captures the screenshot and pulls it to local dir."""
		capture_image = 'adb shell screencap -p /sdcard/image.png'
		pull_image = 'adb pull /sdcard/image.png .'

		import subprocess
		subprocess.call(capture_image.split(), shell = True)
		subprocess.call(pull_image.split(), shell = True)
		print "Capturing Screenshot.."

	def clear_image_cache(self):
		"""deleates SS from local dir."""
		rm_image = 'adb shell rm /sdcard/image.png'
		
		import subprocess
		subprocess.call(rm_image.split(), shell = True)
		print "deleting Screenshot.."	

	def get_screen_resolution(self):
		"""deletes SS from local dir.
			returns a tuple(width, height) """					
		resolution = 'adb shell wm size'
		device_res = self.run_command(resolution)
		device_res  = device_res.split()[-1].split('x')
		self.width, self.height = int(device_res[0]), int(device_res[1])
		return self.width, self.height

	def run_command(self, command):
		"""runs the command given and captures output."""		
		import subprocess

		process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
		while True:
			output = process.stdout.readline()
			if output == '' and process.poll() is not None:
				break
			if output:
				res = output.strip()
		
		return res

def main():
	screencap = Device()
	screencap.capture_screenshot()
	screencap.get_screen_resolution()
	screencap.clear_image_cache()