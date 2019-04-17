import tkinter as tk
from tkinter import *

class Cmd_New_2(object):
	app=tk.Tk()
	app.resizable(width=0,height=0)
	log_line=[]
	class_text=[]
	text = []
	text_value=[]
	frames = []
	widgets = []
	entry=[] 

	def __init__(self):		
		file_content = open("log_file.txt", "r")
		for line in file_content:
			if 'LOG' in line:
				# self.log_line.append(x)
				string_1=line.split(':')
				
				text_value_=string_1[2].strip()
				self.text_value.append(text_value_)
				
				text_=string_1[1].strip()
				self.text.append(text_)
				
				string_2=string_1[0].split('(')[1].split(')')
				self.class_text.append(string_2[0].split('.')[2].strip())

	def header(self):
		frame = tk.Frame(self.app, borderwidth=2, relief="groove")
		frame.pack(side="top", fill="x")
		widget = tk.Label(frame,width=20, text = "Field Type",font='times 10 bold')
		widget.pack(side="left")
		widget = tk.Label(frame,width=20,text = "Existing Data" ,font='times 10 bold')
	    # self.widgets.append(widget)
		widget.pack(side="left")
		widget = tk.Label(frame,width=25,text="Desired Data",font='times 10 bold')
		self.widgets.append(widget)
		widget.pack(side="right")
		# widget = tk.Entry(frame,width=20)
		# self.entry.append(widget)
		# widget.pack(side="right")


	def footer(self):
		frame = tk.Frame(self.app, borderwidth=2, relief="groove")
		# self.frames.append(frame)
		frame.pack(side="top", fill="x")
		widget = tk.Label(frame)
		# self.widgets.append(widget)
		# widget.place(x=5,y=5)
		widget.pack(side="bottom", fill="x")
		self.app.mainloop()



	def clear(self):
		for y in self.entry:
			y.delete(0, 'end')

	def generate_Script(self):
		global e1_script
		global window_
		window_ = tk.Tk()
		window_.resizable(width=False,height=False);
		w=300
		h=60
		ws=window_.winfo_screenwidth()
		hs=window_.winfo_screenheight()
		x=(ws/2)-(w/2)
		y=(hs/2)-(h/2)
		window_.geometry('%dx%d+%d+%d'%(w,h,x,y)) 		
		window_.bind('<Return>', self.ok_button)								
		l1_script = Label(window_, text="Give Script Name: ")
		l1_script.place(x=5,y=5)
		e1_script = Entry(window_, width=25)
		e1_script.place(x=130,y=5)
		b1_script=Button(window_,width=10,text="OK",command=self.ok_button)
		b1_script.place(x=100,y=30)

	def ok_button(self,args=None):
		script_name=e1_script.get()
		print(script_name)
		window_.destroy()


	def Typed(self,text_, textval , class_text):
		label_txt = text_ + " " + textval

		frame = tk.Frame(self.app, borderwidth=2, relief="groove")
		self.frames.append(frame)
		frame.pack(side="top", fill="x")

		widget = tk.Label(frame,width=20, text = class_text)
		self.widgets.append(widget)
		widget.config(height = 2)
		widget.pack(side="left")

		widget = tk.Label(frame,text = label_txt )
		self.widgets.append(widget)
		widget.pack(side="left")

		widget = tk.Label(frame,width=1)
		self.widgets.append(widget)
		widget.pack(side="right")

		widget = tk.Label(frame,width=1)
		self.widgets.append(widget)
		widget.pack(side="left")

		widget = tk.Entry(frame,width=25)
		self.entry.append(widget)
		widget.pack(side="right")


	def clicked(self,text_,textval,class_text):
		label_txt = text_ + " " + textval
		frame = tk.Frame(self.app, borderwidth=2, relief="groove")
		self.frames.append(frame)
		frame.pack(side="top", fill="x")

		widget = tk.Label(frame,width=20, text = class_text)
		self.widgets.append(widget)
		widget.config(height = 2)
		widget.pack(side="left")

		widget = tk.Label(frame,text = label_txt )
		self.widgets.append(widget)
		widget.pack(side="left")

		widget = tk.Label(frame,width=1)
		self.widgets.append(widget)
		widget.pack(side="right")

		widget = tk.Label(frame,width=1)
		self.widgets.append(widget)
		widget.pack(side="left")

		widget = tk.Entry(frame,width=25)
		self.entry.append(widget)
		widget.pack(side="right")



	def Picked(self,text_,textval,class_text):
		label_txt = text_ + " " + textval
		frame = tk.Frame(self.app, borderwidth=2, relief="groove")
		self.frames.append(frame)
		frame.pack(side="top", fill="x")
		widget = tk.Label(frame,width=20, text = class_text)
		self.widgets.append(widget)
		widget.config(height = 2)
		# widget.place(x=5,y=5)
		widget.pack(side="left")
		widget=tk.Label(frame, text = label_txt)

		self.widgets.append(widget)
		widget.pack(side="left")
		widget = tk.Label(frame,width=1)
		self.widgets.append(widget)
		widget.pack(side="right")
		widget = tk.Label(frame,width=1)
		self.widgets.append(widget)
		widget.pack(side="left")
		widget = tk.Entry(frame,width=25)
		self.entry.append(widget)
		widget.pack(side="right") 



	def spinner(self):
		frame = tk.Frame(self.app, borderwidth=2, relief="groove")
		self.frames.append(frame)
		frame.pack(side="top", fill="x")
		widget = tk.Label(frame)
		self.widgets.append(widget)
		widget.pack(side="left")
		widget_ = tk.Spinbox(frame, from_=0, to=10)
		self.widgets.append(widget_)
		widget_.pack(side="right",text=" ")
	
	def GUI_Maker(self):
		temp=0
		for x in self.class_text:
			if 'EditText' in x : 
				self.Typed(self.text[temp],self.text_value[temp],self.class_text[temp])
				temp+=1
			elif 'View' in x : 
				self.clicked(self.text[temp],self.text_value[temp],self.class_text[temp])
				temp+=1
			elif 'Button' in x : 
				self.Picked(self.text[temp],self.text_value[temp],self.class_text[temp])
				temp+=1
			else:
				pass
				temp+=1
		widget = tk.Label(self.app,width=5)
		# self.widgets.append(widget)
		widget.pack(side="left")
		createWidgetButton_ = tk.Button(self.app, width=20,text="Reset",command=self.clear)
			# createWidgetButton_.place(x=30,y=self.hs-20)
		createWidgetButton_.pack(side="left")
		widget = tk.Label(self.app,width=5)
		# self.widgets.append(widget)
		widget.pack(side="right")
		createWidgetButton_ = tk.Button(self.app, width=20,text="Generate Script",command=self.generate_Script)
		# createWidgetButton_.place(x=300,y=self.hs-20)
		widget.config(height = 2)

		createWidgetButton_.pack(side="right")
		self.app.mainloop()


obj=Cmd_New_2()
obj.header()
obj.GUI_Maker()