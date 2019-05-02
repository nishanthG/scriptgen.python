class File_Generator(object):
	"""docstring for ScriptMaker"""
	line_break = '\n'
	import_1 = 'import re \nimport sys \nimport os\nimport time\n'
	import_2 = 'from com.dtmilano.android.viewclient import ViewClient\nfrom logger import logger\nimport pandas as pd\n'

	check_Lists = "import time\nstart_time = int(time.time())\n\nflag = False\nstep_results = []\nexception = []\nexception_result = []\ntime_result = []\n"

	kwargs1 = "kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': False}\n"
	set_up_device = 'device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)\n'
	kwargs2 = "kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False, 'ignoreuiautomatorkilled': True, 'autodump': False, 'debug': {}, 'startviewserver': True, 'compresseddump': True}\n"
	set_up_viewclient = 'vc = ViewClient(device, serialno, **kwargs2)\n\n'

	utility_function = """def pick_value(file_name, sheet_name, column_name, data_range):
\ttry:
\t\tdf = pd.read_excel(file_name, index_col=0, sheetname=sheet_name)
\t\tcolumn=df[column_name][data_range[0]:data_range[1]+1].tolist()
\t\tassert len(column)!=0
\t\treturn column[0]
\texcept Exception as e:
\t\tprint(str(e))\n"""
	
	dump = 'try:\n\tvc.dump(window = -1)\nexcept Exception as e:\n\tpass\n'

	def __init__(self, filename):
		super(File_Generator, self).__init__()
		self.filename = filename
		self.log_filename = "filename = '{filename}'\n".format(filename=self.filename)
		
	def generate_files(self):
		with open(self.filename +'.py', 'w+') as script:
			script.close()

		with open(self.filename +'.txt', 'w+') as log_file:
			log_file.close()

		self.write_initial_content(self.filename)

	def write_initial_content(self, filename):
		parser = [self.import_1, self.import_2, self.line_break, self.utility_function, self.line_break, self.check_Lists, self.line_break, self.kwargs1, self.set_up_device, self.kwargs2, self.set_up_viewclient, self.log_filename, self.dump, self.line_break]

		with open(filename+'.py', 'a') as script:
			for lex in parser:
				script.write(lex)
			script.close()