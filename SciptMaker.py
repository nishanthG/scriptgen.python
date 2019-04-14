class ScriptMaker(object):
	"""docstring for ScriptMaker"""
	line_break = '\n'
	import_1 = 'import re \nimport sys \nimport os\nimport time\n'
	import_2 = 'from com.dtmilano.android.viewclient import ViewClient\nfrom logger import logger\nimport pandas as pd\n'

	check_Lists = "import time\nstart_time = int(time.time())\n\nflag = False\nstep_results = []\nexception = []\nexception_result = []\ntime_result = []\n"

	kwargs1 = "kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': False}\n"
	set_up_device = 'device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)\n'
	kwargs2 = "kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False, 'ignoreuiautomatorkilled': True, 'autodump': False, 'debug': {}, 'startviewserver': True, 'compresseddump': True}\n"
	set_up_viewclient = 'vc = ViewClient(device, serialno, **kwargs2)\n\n'

	utility_function = """def pick_value(file_name, column_name):
\tdf = pd.read_excel(file_name, index_col=0)
\tcolumn=df[column_name].tolist()
\tassert len(column)!=0
\treturn column[0]\n"""
	
	dump = 'try:\n\tvc.dump(window = -1)\nexcept Exception as e:\n\tpass\n'

	def __init__(self):
		super(ScriptMaker, self).__init__()
		
	def create_files(self):
		with open('script.py', 'w+') as script:
			script.close()

		with open('log_file.txt', 'w+') as log_file:
			log_file.close()

	def write_initial_content(self):
		parser = [self.import_1, self.import_2, self.line_break, self.utility_function, self.line_break, self.check_Lists, self.line_break, self.kwargs1, self.set_up_device, self.kwargs2, self.set_up_viewclient, self.dump, self.line_break]

		with open('script.py', 'a') as script:
			for lex in parser:
				script.write(lex)
			script.close()

if __name__ == '__main__':
	ScriptMaker = ScriptMaker()
	ScriptMaker.create_files()
	ScriptMaker.write_initial_content()