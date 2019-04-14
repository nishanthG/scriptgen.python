class Replicator(object):
	"""docstring for Replicator"""
	def __init__(self, XY):
		super(Replicator, self).__init__()
		self.XY = XY

	def replicate(self):
		import subprocess

		command = 'adb shell input tap {X} {Y}'.format(X=self.XY[0], Y=self.XY[1])
		process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)