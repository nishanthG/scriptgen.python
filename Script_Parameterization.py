# script_file_name = 'script.py'
# log_file_name = 'log_file.txt'

# script_keyword = 'vc.findViewWith'
# log_keyword = '#LOG'

# script_new_filename = 'new_script.py'
# log_new_filename = 'new_log_file.txt'

lines = []
indexes = []
logs = []

# GUI_list = [('3','7'),{'ADD TIMESHEET':['/media/gn/Work/AQM/PY_RepV2.0/Iris.xls','Data','Petal_width',[0,5]]},None,None,('HalfDayWorking','Absent'),None,None,('National Stock Exchange of India','Aditya Birla'),None,None,('NSE Now 2.0','Aditya Birla New'),None,None,None,None,None,('Automation Testing','Manual Testing'),None,None,('Test Script Creation','Manual'),None]
# GUI_list = [('3','7'),None,None,None,('HalfDayWorking','Absent'),None,None,('National Stock Exchange of India','Aditya Birla'),None,None,('NSE Now 2.0','Aditya Birla New'),None,None,None,None,None,('Automation Testing','Manual Testing'),None,None,('Test Script Creation','Manual'),None]

class Parameterise(object):
	"""docstring for Parameterise"""
	def __init__(self, old_filename, keyword, new_filename, GUI_list):
		super(Parameterise, self).__init__()
		print(old_filename.encode('ascii','ignore').replace('txt','py'), keyword, new_filename)
		self.GUI_list = GUI_list
		# self.read_file(old_filename.encode('ascii','ignore').replace('txt','py'), keyword, new_filename)
		
	def read_file(self,old_filename, keyword, new_filename):
		with open(old_filename, 'r') as file:
			global lines
			lines = file.readlines()
			# print(lines)
		self.marinate(keyword, new_filename)

	def marinate(self,keyword, new_filename):
		for index, log in enumerate(lines):
			if keyword in log:
				indexes.append(index)
				logs.append(log)
		
		import os
		file, extension = os.path.splitext(new_filename)

		if 'txt' in extension:
			self.replace_value(new_filename)
		else:
			self.replace_values(new_filename)

	def replace_value(self, new_filename):
		assert len(indexes)==len(self.GUI_list)
		for i,v in enumerate(self.GUI_list):
			if v!= None and type(v)==tuple:
				logs[i]=logs[i].replace(v[0],v[1])
			elif v!= None and type(v)==dict:
				key = list(v.keys())[0]
				value = self.fetch_value_from_file(v[key][0],v[key][1],v[key][2],v[key][3])
				logs[i]=logs[i].replace(key,str(value))

		assert len(indexes)==len(logs)
		self.rebuild_file(new_filename)

	def replace_values(self, new_filename):
		assert len(indexes)==len(self.GUI_list)
		for i,v in enumerate(self.GUI_list):
			if v!= None and type(v)==tuple:
				logs[i]=logs[i].replace(v[0],v[1])
			elif v!= None and type(v)==dict:
				key = list(v.keys())[0]
				log="\tvalue = pick_value('{file_path}','{sheet_name}','{column_name}',{range})\n".format(file_path=v[key][0],sheet_name=v[key][1],column_name=v[key][2],range=v[key][3])
				logs[i]=log+logs[i].replace(key,'value').replace("'", '')

		assert len(indexes)==len(logs)
		self.rebuild_file(new_filename)

	def rebuild_file(self, new_filename):
		for index, new_log in zip(indexes,logs):
			lines[index] = new_log
		
		with open(new_filename,'w') as log_file:
			for log in lines:
				log_file.write(log)
			log_file.close()
			print(new_filename,'generated')
	
	def clear_cache(self):
		lines = []
		indexes = []
		logs = []

	def fetch_value_from_file(self,file_name, sheet_name, column_name, data_range):
		import pandas as pd
		try:
			df = pd.read_excel(file_name, index_col=0, sheetname=sheet_name)
			column=df[column_name][data_range[0]:data_range[1]+1].tolist()
			assert len(column)!=0
			print(column)
			return column[0]
		except Exception as e:
			print(str(e))

if __name__ == '__main__':
	# Parameterise(script_file_name, script_keyword, script_new_filename)
	Parameterise(log_file_name, log_keyword, log_new_filename)