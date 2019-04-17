""" requiers a Scenario passed to the constructor of the class
1. create_file()
2. initialize_logs()

To add data to the table [First Column], the class should call add_step_data() with count of step, name of step and a list with all the steps as parameters.
To add result(pass/fail) [Second Column], call result() passing a list of all the results and the len of list containing the lines in it.

Similarly, add exceptions and time [third and fourth columns] passing the lists of values and lenthgs.

Finally, add footers and execution result.   
"""

class logger(object):
	"""docstring for logger"""
	Final_Result = "Passed"
	
	spacing = []
	log_steps = []
	step_name = []

	from collections import OrderedDict
	ZIPPED_STEPS = OrderedDict()
	
	LOG_TABLE = []

	def __init__(self):
		super(logger, self).__init__()
		self.table_end = "<br></td>"
		self.title = ""
	
	def create_file(self):
		with open('log.html', 'w+') as log_file:
			log_file.close()

	def initialize_log_file(self, title):

		self.create_file()
		
		header = """<html>
<head>"""
		header_ ="""<link href="../testng.css" rel="stylesheet" type="text/css" />
<link href="../my-testng.css" rel="stylesheet" type="text/css" />
<style type="text/css">
.log { display: none;}
.stack-trace { display: none;} 
</style>
<script type="text/javascript">
</script>
</head>
<body>"""

		table_body = """<table width='100%' border='1' class='invocation-passed'>
<tr align='center'><td colspan='4' align='center'><b >TEST LOGS</b></td></tr>
<tr align='center'><td width="30%" align='center'><b>Scenario Steps</b></td>
<td width="10%" align='center'><b>Result (pass/fail)</b></td>
<td width="25%" align='center'><b>Exception (if any)</b></td>
<td width="10%" align='center'><b>Time per Execution(seconds)</b></td>
</tr>\n"""

		table_header = "<td title='com.AQM.testscripts.AutomationDriverScript.scriptGenerator()' align='center'><br>"

		self.LOG_TABLE.extend([header,header_,table_body,table_header])
		self.add_title_bar(title)

	def add_title_bar(self, title):
		title_bar = "<title>Scenario Name : {title}</title>".format(title=title)
		heading = "<h2 align='center'>&nbsp;{title}&nbsp;</h2><table border='1' align='center'>\n<tr>".format(title=title)
		self.LOG_TABLE.insert(1,title_bar)
		self.LOG_TABLE.insert(3,heading)
		self.log_creation_time()

	def add_test_info(self, Passed=0, Failed=0, Skipped=0):
		test_info = "<td align='center'>&nbsp;Tests : Passed/ Failed/ Skipped:&nbsp;</td><td align='center'>&nbsp;{Passed}/{Failed}/{Skipped}&nbsp;</td>\n</tr><tr>".format(Passed= Passed,Failed= Failed,Skipped= Skipped)
		self.LOG_TABLE.insert(4,test_info)	

	def log_creation_time(self):
		import datetime
		StartedOn = "<td align='center'>&nbsp;Started on:&nbsp;</td><td>&nbsp;{time}&nbsp;</td>\n</tr>".format(time=datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))
		self.LOG_TABLE.insert(4,StartedOn)

	def log_total_time(self, start_time):
		import time
		total_time = "<tr><td align='center'>&nbsp;Total time (in seconds):&nbsp;</td><td align='center'>{total_time}</td>\n</tr><tr>\n</table>".format(total_time = (int(time.time()) - start_time))
		self.LOG_TABLE.insert(6,total_time)

	def add_step_data(self, step_number, step_name, step_lines):
		step_name = "<B><u>Step Number - {number}</u>&nbsp;&nbsp;<i><Font Color = /'#00008B/'> Executing : {step_name} <br></Font></i></B><br/>\n".format(number=step_number,step_name=step_name)

		with open('log.html', 'a') as log_file:
			log_file.write(step_name)
			log_file.write("".join(step_lines))
			log_file.write("<br><br>")
			log_file.close()

	def add_result(self, result):
		execution_result = []
		
		failed_cases = result.count("Failed")
		if failed_cases > (len(result) - failed_cases):
			self.Final_Result = "Failed"
		else:
			self.Final_Result = result[-1]	
		
		for index,value in enumerate(result):
			execution_result.append("<br>"*(self.spacing[index]/2)+str(value)+"<br>"*(self.spacing[index]/2 + 1))

		execution_result = "<td align='center'>{time}</td>\n".format(time="".join(execution_result))
		with open('log.html', 'a') as log_file:
			log_file.write(execution_result)
			log_file.close()

	def add_exception(self, exception):
		exception_ = []
		
		for index,value in enumerate(exception):
			if type(value)==str:
				exception_.append("<br>"*(self.spacing[index]/2)+str(value) +"<br>"*(self.spacing[index]/2 + 1))
			elif type(value)==list:
				st = [i.split('in tree')[0] for i in value]
				exception_.append("<br>"*(self.spacing[index]/2)+ str(st) +"<br>"*(self.spacing[index]/2 - len(st)/2 +1))

		exception_result = "<td align='center'>{exception}</td>\n".format(exception="".join(exception_))
		with open('log.html', 'a') as log_file:
			log_file.write("</td>")
			log_file.write(exception_result)
			log_file.close()		

	def add_Execution_time(self, execution_time):
		execution_times = []
		
		for index,time in enumerate(execution_time):
			execution_times.append("<br>"*(self.spacing[index]/2)+str(time) +"<br>"*(self.spacing[index]/2 + 1))

		exception_time = "<td align='center'>{time}</td>\n".format(time="".join(execution_times))
		with open('log.html', 'a') as log_file:
			log_file.write(self.table_end)
			log_file.write(exception_time)
			log_file.close()

	def write_to_LOG(self):
		with open('log.html', 'a') as log_file:
			for element in self.LOG_TABLE:
				log_file.write(element)
			log_file.close()

	def final_sequence(self, start_time, step_results, exception_results, time_result):
		step_number = 1
		self.log_total_time(start_time)
		self.write_to_LOG()
		
		for step_name in self.ZIPPED_STEPS:
			self.add_step_data(step_number, step_name, self.ZIPPED_STEPS[step_name])
			step_number+=1
		
		self.add_result(step_results)
		self.add_exception(exception_results)
		self.add_Execution_time(time_result)
		self.Scenario_description(start_time)

	def logs(self):
		for index, log in enumerate(self.LOG_TABLE):
			print(str(index) + ":" + log)

	def Scenario_description(self,start_time):
		import time
		footer_time = "<h3><B>Scenario Description: Execution Completed in '{total_time}' seconds.</h3></B>\n".format(total_time=int(time.time()) - start_time)
		Scenario_result = "<h2><B>[ Scenario :::: '{result}' ]</h2></B></Br>\n".format(title=self.title, result=self.Final_Result)
		
		with open('log.html','a') as log_file:
			log_file.write(footer_time)
			log_file.write(Scenario_result)
			log_file.close()
		print("Log Generated.")

	def generate_log(self):
		log_instance = logger()
		
		with open('new_log_file.txt','r') as log_file:
			for log in log_file:
				if "SCENARIO" in log:
					log_instance.initialize_log_file(log.split(':', 1)[1].strip())

				elif "STEP" in log:
					if len(self.log_steps) == 0:
						self.step_name.append(log.split(':', 1)[1].strip())
					else:
						self.ZIPPED_STEPS[self.step_name[0]] = self.log_steps
						self.spacing.append(len(self.log_steps) + 4)
						self.step_name = []
						self.log_steps = []
						self.step_name.append(log.split(':', 1)[1].strip())

				elif "LOG" in log:
				 	self.log_steps.append(log.split(':', 1)[1].strip() +'<br>')

		self.ZIPPED_STEPS[self.step_name[0]] = self.log_steps
		self.spacing.append(len(self.log_steps) + 4)

if __name__ == '__main__':
	log = logger()
	log.generate_log()