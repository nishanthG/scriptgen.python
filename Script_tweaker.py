class Script_Tweaks(object):
	script_data = []
	fields = []
	field_indexes =[]
	
	"""docstring for Script_Tweaks"""
	def __init__(self, script_filename, element_type, element_id, element_value, at_position, element_value_ET = None, change_script = True):
		super(Script_Tweaks, self).__init__()
		
		self.script_filename = script_filename
		self.element_type = element_type
		self.element_id = element_id
		self.element_value = element_value
		self.at_position = at_position
		self.element_value_ET = element_value_ET

		if change_script:
			self.element = self.make_element(self.element_type, self.element_id, self.element_value, element_value_ET)
			self.update_script()
		else:
			self.update_log()

	def make_element(self, element_type, element_id,element_value,element_value_ET): 
		if element_type in ['Button','Spinner', 'View']:
			if element_id == 'id':
				return '''vc.findViewByIdOrRaise("{element_value}").touch()'''.format(element_value = element_value)
			elif element_id == 'text':
				return '''vc.findViewWithTextOrRaise("{element_value}").touch()'''.format(element_value = element_value)
		
		elif element_type == 'EditText':
			if element_id == 'id':
				return '''vc.findViewByIdOrRaise("{element_value}").setText('{value}')'''.format(element_value = element_value, value = element_value_ET)
			elif element_id == 'text':
				return '''vc.findViewWithTextOrRaise("{element_value}").setText('{value}')'''.format(element_value = element_value, value = element_value_ET)

	def read_script(self, keyword):
		with open(self.script_filename,'r') as file:
			for index,line in enumerate(file):
				self.script_data.append(line)
				
				if keyword in line:
					self.fields.append(line)
					self.field_indexes.append(index)

		print(*zip(self.field_indexes, self.fields))

	def append_element_script(self, new_field, at_position):
		index = self.field_indexes[at_position-1]
		self.script_data.insert(index-2, new_field)
		self.remake_script()

	def append_element_log(self, new_log, at_position):
		index = self.field_indexes[at_position -1]
		self.script_data.insert(index, new_log)
		self.remake_script()

	def remake_script(self):
		with open(self.script_filename,'w') as outfile:
			outfile.write("".join(self.script_data))

	def element_to_add(self):
		string = '''\ntry:\n\t{script_line}
\tvc.sleep(3)
except Exception as e:
\texception.append(str(e))
\tpass
try:
\tvc.dump(window = -1)
except Exception as e:
\tpass\n\n'''.format(script_line=self.element)

		self.append_element_script(string, self.at_position)

	def log_to_add(self):
		if self.element_type in ['Button', 'RadioButton', 'View']:
			line = "#LOG(android.widget.{type}): Clicked on element with text : '{text}'\n".format(type=self.element_type,text=self.element_value)
			self.append_element_log(line, self.at_position)
			print('log to add : ', line)
		
		elif self.element_type == 'EditText':
			line = "#LOG(android.widget.EditText): Cleared and Typed : '{text}'\n".format(text=self.element_value_ET)
			self.append_element_log(line, self.at_position)
			print('log to add : ', line)
		
		elif self.element_type == 'Spinner':
			line = "LOG(android.widget.Spinner): Selected element with value : '{text}'\n".format(text=self.element_value)
			self.append_element_log(line, self.at_position)
			print('log to add : ', line)

	def update_script(self):
		self.read_script(keyword = 'vc.find')
		self.element_to_add()
		self.clear_cache()
		self.read_script(keyword = 'vc.find')

	def update_log(self):
		self.read_script(keyword = 'LOG')
		self.log_to_add()
		self.clear_cache()
		self.read_script(keyword = 'LOG')

	def clear_cache(self):
		self.script_data.clear()
		self.fields.clear()
		self.field_indexes.clear()

Script_Tweaks('new_log_file.txt', 'EditText', 'text', 'Login', 3, change_script = False, element_value_ET = "Nishanth")
# Script_Tweaks('new_script.py', 'EditText', 'text', 'Login', 3, element_value_ET = "Nishanth")