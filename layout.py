class UIDump(object):
	"""docstring for Dump"""
	bounds = list()
	elements = dict()
	check_clickable = dict()
	check_text = dict()
	check_unique_id = dict()
	check_resource_id = dict()
	check_className = dict()

	def __init__(self):
		super(UIDump, self).__init__()

	def get_ui_dump(self):
		command = 'python dump -a'
		self.run_command(command)
		return self.bounds
	
	def get_bounds(self, string):
		''' returns a tuple of bounds of the string passed'''
		regex = "bounds="
		
		if regex in string:
			reg_output = string.split(regex)
			reg_output = reg_output[1].split('content-desc')
			# print reg_output[0].strip()
			return reg_output[0].strip()
		else:
			pass

	def get_class(self, string):
		''' returns a tuple of bounds of the string passed'''
		regex = "class="

		if regex in string:
			reg_output = string.split(regex)[1]
			reg_output = reg_output.split('index')
			return reg_output[0].strip()
		else:
			pass

	def get_clickable(self, string):
		''' returns a tuple of bounds of the string passed'''
		regex = "clickable="

		if regex in string:
			reg_output = string.split(regex)[1]
			reg_output = reg_output.split('package')
			return reg_output[0].strip()
		else:
			pass

	def get_uniqueID(self, string):
		''' returns a tuple of bounds of the string passed'''
		regex = "uniqueId="

		if regex in string:
			reg_output = string.split(regex)[1]
			reg_output = reg_output.split('checkable')
			return reg_output[0].strip()
		else:
			pass

	def get_resourceID(self, string):
		''' returns a tuple of bounds of the string passed'''
		regex = "resource-id="

		if regex in string:
			reg_output = string.split(regex)[1]
			reg_output = reg_output.split('password')
			return reg_output[0].strip()
		else:
			pass

	def get_text(self, string):
		''' returns a tuple of bounds of the string passed'''
		regex = "text="

		if regex in string:
			reg_output = string.split(regex)[1]
			reg_output = reg_output.split('long-clickable')
			return reg_output[0].strip()
		else:
			pass

	def run_command(self, command):
		"""runs the command given and captures output."""		
		import subprocess

		process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
		crude_bounds = list()
		index = 0

		while True:
			output = process.stdout.readline()
			
			if output == '' and process.poll() is not None:
				break
			
			if output:
				crude_bounds.append(self.get_bounds(output.strip()))
				
				self.elements[index] = self.get_class(output.strip())
				self.check_className[index] = self.get_class(output.strip())
				# self.check_clickable[index] = self.get_clickable(output.strip())
				self.check_text[index] = self.get_text(output.strip())
				self.check_unique_id[index] = self.get_uniqueID(output.strip())
				self.check_resource_id[index] = self.get_resourceID(output.strip())

				index += 1
		
		self.master_bound_list(crude_bounds)

	def master_bound_list(self, master_list):
		""" Extracts the coordinates from the bounds and creates a list of all them."""
		# print master_list
		
		temp = [i.split('), (') for i in master_list if i != None]
		
		for i in temp:
			x1y1 = i[0].split(',') # list
			x2y2 = i[1].split(',') # list

			x1 = x1y1[0].split('(')[2] 
			y1 = x1y1[1].strip()
			x2 = x2y2[0]
			y2 = x2y2[1].split(')')[0].strip()

			self.bounds.append(list((x1, x2, y1, y2)))

def main():
	UIDump().get_ui_dump()

if __name__ == '__main__':
	main()