from SciptMaker import ScriptMaker
from logger import logger


class ScriptGen(object):
	"""docstring for ScriptGen"""
	except_block = "except Exception as e: \n\texception.append(str(e))\n"
	try_block = "try:\n\t"
	
	def __init__(self):
		super(ScriptGen, self).__init__()

	def script(self, line):
		with open('script.py','a') as script:
			script.write(self.try_block)
			script.write(line)
			script.write(self.except_block)						
			script.write(ScriptMaker().dump)
			script.write(ScriptMaker().line_break)
			script.close()

	def log_checker(self, line):
		with open('script.py','a') as script:
			script.write(line)					
			script.write(ScriptMaker().line_break)
			script.close()

	def log(self, log):
		with open('log_file.txt','a') as log_file:
			log_file.write(log)
			log_file.close()