import Tkinter
from Tkinter import *
import sys
from ScreenShot import Screenshot
from ScreenShot import main
from AQMdroid import AQMdroid
from ScriptGen import ScriptGen


class startGUI(object):
	"""docstring for Screen_Shot_Button"""
	log_handler = """\nend = int(time.time())\n
try:\n\ttotal = end - start\n\ttime_result.append(total)\n
except NameError as e:\n\tpass\n
if flag==0:\n\tpass\n
elif len(exception) > 0:\n\tstep_results.append("Failed")\n\texception_result.append(exception)\n\texception = []\n
else:\n\tstep_results.append("Passed")\n\texception_result.append("None")\nstart = int(time.time())\nflag=1\n"""

	generate_log_file = """logger().generate_log()\n
logger().add_test_info(Passed=step_results.count("Passed"), Failed=step_results.count("Failed"))\n
logger().final_sequence(start_time,step_results,exception_result,time_result)\n"""
	
	def __init__(self):
		super(startGUI, self).__init__()

		resolution_list = self.get_device_resolution()
		self.width = resolution_list[0]
		self.height = resolution_list[1]
	
	def screeninfo(self):
		"""Captures the Screenshot and displays it """
		Screenshot().capture_screenshot()
		resolution = (self.width, self.height)
		droid = AQMdroid('image.png', resolution)
		
		try:
			droid.getorigin()
		except Exception as e:
			ScriptGen().log_checker(self.log_handler)
			ScriptGen().log_checker(self.generate_log_file)
			print "\nExit Point Triggered."
			sys.exit()
	
	def scenario_name(self):
		global window_
		global e1_scenario
		window_ = Tkinter.Tk()
		window_.resizable(width=False,height=False);
		w=300
		h=60	
		ws=window_.winfo_screenwidth()
		hs=window_.winfo_screenheight()
		x=(ws/2)-(w/2)
		y=(hs/2)-(h/2)
		window_.geometry('%dx%d+%d+%d'%(w,h,x,y)) 
		window_.bind('<Return>', self.scenraio_fun)								
		l1_scenario = Label(window_, text="Enter a Scenario Name: ")
		l1_scenario.place(x=5,y=5)
		e1_scenario = Entry(window_, width=25)
		e1_scenario.place(x=130,y=5)
		b1_scenario=Button(window_,width=10,text="OK", command = self.scenraio_fun)
		b1_scenario.place(x=100,y=30)

	def execution_name(self):
		global window_1
		global e1_execution
		window_1 = Tkinter.Tk()
		w=300
		h=60
		window_1.resizable(width=False,height=False);	
		ws=window_1.winfo_screenwidth()
		hs=window_1.winfo_screenheight()
		x=(ws/2)-(w/2)
		y=(hs/2)-(h/2)
		window_1.geometry('%dx%d+%d+%d'%(w,h,x,y)) 
		window_1.bind('<Return>', self.execution_fun)
		window_1.bind('<Return>', self.execution_fun)								
		l1_execution = Label(window_1, text="Enter a Step Name: ")
		l1_execution.place(x=5,y=5)
		e1_execution = Entry(window_1, width=25)
		e1_execution.place(x=130,y=5)
		b1_execution=Button(window_1,width=10,text="OK", command = self.execution_fun)
		b1_execution.place(x=100,y=30)

	def scenraio_fun(self, args = None ):
		scenario_value=e1_scenario.get()
		ScriptGen().log("#SCENARIO: {name}\n".format(name=scenario_value))
		b1['state'] = 'disabled'
		window_.destroy()

	def execution_fun(self, args = None):
		execution_value=e1_execution.get()
		ScriptGen().log_checker(self.log_handler)
		ScriptGen().log("#STEP: {name}\n".format(name=execution_value))
		window_1.destroy()
	
	def run(self):
		"""GUI customizations"""
		global b1
		window= Tkinter.Tk()
		window.resizable(width=False,height=False);
		w=325
		h=90
		window.resizable(width=False,height=False);	
		ws=window.winfo_screenwidth()
		hs=window.winfo_screenheight()
		x=(ws/2)-(w/2)
		y=(hs/2)-(h/2)
		window.geometry('%dx%d+%d+%d'%(w,h,x,y)) 
		window.bind('<Return>', self.execution_fun)
		l1= Label(window, text="  Enter a Scenario Name :")
		l1.place(x=0,y=0)
		b1=Button(window, width = 15, text="Enter", command=self.scenario_name)
		b1.place(x=200,y=0)
		l2= Label(window, text="  Enter an execution step Name :")
		l2.place(x=0,y=30)
		b2=Button(window,width = 15, text="Enter", command=self.execution_name)
		b2.place(x=200,y=30)
		l3= Label(window, text="  Take Snapshot of the Device :")
		l3.place(x=0,y=60)
		b3=Button(window, width = 15,text="ScreenShot", command=self.screeninfo)
		b3.place(x=200,y=60)
		window.mainloop()

	def get_device_resolution(self):
		""" reads and saves the device resolution. """
		instance = Screenshot()
		width, height = instance.get_screen_resolution() 
		
		return list((width, height))