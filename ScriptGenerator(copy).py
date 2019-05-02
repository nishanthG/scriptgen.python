from Script_Initializer import FileCreator
from logger import logger

class ScriptGen(object):
	"""docstring for ScriptGen"""
	except_block = "except Exception as e: \n\texception.append(str(e))\n"
	try_block = "try:\n\t"
	
	def __init__(self, filename):
		super(ScriptGen, self).__init__()
		self.filename = filename

	def script(self, line):
		with open(self.filename+'.py','a') as script:
			script.write(self.try_block)
			script.write(line)
			script.write(self.except_block)						
			script.write(FileCreator(self.filename).dump)
			script.write(FileCreator(self.filename).line_break)
			script.close()

	def log_checker(self, line):
		with open(self.filename+'.py','a') as script:
			script.write(line)					
			script.write(FileCreator(self.filename).line_break)
			script.close()

	def log(self, log):
		with open(self.filename+'.txt','a') as log_file:
			log_file.write(log)
			log_file.close()