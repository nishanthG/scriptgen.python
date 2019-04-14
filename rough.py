script_file_name = 'script.py'
log_file_name = 'log_file.txt'
script_keyword = 'vc.findViewWith'
log_keyword = '#LOG'
script_new_filename = 'new_script.py'
log_new_filename = 'new_log_file.txt'

lines = []
indexes = []
logs = []

GUI_list = [('3','7'),None,None,None,('HalfDayWorking','Absent'),None,None,('National Stock Exchange of India','Aditya Birla'),None,None,('NSE Now 2.0','Aditya Birla New'),None,None,None,None,None,('Automation Testing','Manual Testing'),None,None,('Test Script Creation','Manual'),None]

class Parameterise(object):
	"""docstring for Parameterise"""
	def __init__(self):
		super(Parameterise, self).__init__()

	def read_value(self,file_name, column_name):
		import pandas as pd
		df = pd.read_excel(file_name, index_col=0)
		assert len(df[column_name].tolist())!=0
		return df[column_name].tolist()[0]
		
	def read_file(self,file_name, keyword, new_filename):
		with open(file_name, 'r') as file:
			global lines
			lines = file.readlines()
			# print(lines)
		self.marinate(keyword, new_filename)

	def marinate(self,keyword, new_filename):
		for index, log in enumerate(lines):
			if keyword in log:
				indexes.append(index)
				logs.append(log)
		
		self.replace_values(new_filename)

	def replace_values(self, new_filename):
		assert len(indexes)==len(GUI_list)
		for i,v in enumerate(GUI_list):
			if v!= None:
				logs[i]=logs[i].replace(v[0],v[1])

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

if __name__ == '__main__':
	file_excel = '/media/gn/Work/AQM/PY_RepV2.0/Iris.xls'
	obj = Parameterise()
	obj.read_value(file_excel,'Petal_width')
	# obj.read_file(script_file_name, script_keyword, script_new_filename)
	# # obj.clear_cache()
	# obj.read_file(log_file_name, log_keyword, log_new_filename)