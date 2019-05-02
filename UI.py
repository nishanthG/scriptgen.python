import Tkinter 
import Tkconstants, tkFileDialog
import tkMessageBox
from Tkinter import *
import Tix as tk

class GUI():
	GUI_List, widgets, class_text, text, text_value, values, files, steps, entry_list, log_line = ([] for _ in range(10))
	
	imp_line_count=0
	width=300
	height=60

	def __init__(self, filename):
		self.filename = filename
		print('Working on  file :'+ self.filename)

	def adjust_window_position(self, width, height, window_name):
		window_name.resizable(width=False,height=False);	
		width_size=window_name.winfo_screenwidth()
		heigth_size=window_name.winfo_screenheight()
		X=(width_size/2)-(width/2)
		Y=(heigth_size/2)-(height/2)
		window_name.geometry('%dx%d+%d+%d'%(width,height,X,Y))
	
	def initialize(self):
		global app
		global sw
		app=tk.Tk()

		self.adjust_window_position(850,500,app)
		
		sw= tk.ScrolledWindow(app, scrollbar=tk.Y)
		sw.pack(fill=tk.BOTH, expand=1)
		self.parse_logs()

	def file_picker(self,r):
		print r
		global row
		row = r
		global window_
		global column_name
		global sheet_name
		global range_from
		global range_to
		global filename_

		if self.entry_list[row].get() == '':

			filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.txt"),("all files","*.*")))
			
			if not filename:
				pass
			else:
				window_= Tkinter.Tk()
			
				self.adjust_window_position(350,120,window_)

				l1= Label(window_, text="Column Name :")
				l1.place(x=20,y=0)
				column_name=Entry(window_, width = 30)
				column_name.place(x=150,y=0)
				l2= Label(window_, text="Sheet Name:")
				l2.place(x=20,y=30)
				sheet_name=Entry(window_,width = 30)
				sheet_name.place(x=150,y=30)
				l3= Label(window_, text="Range of data:")
				l3.place(x=20,y=60)
				range_from=Entry(window_,width=12)
				range_from.place(x=150,y=60)
				l4 = Label(window_, text="to",width=6)
				l4.place(x=220,y=60)

				range_to = Entry(window_,width=12)
				range_to.place(x=260,y=60)

				b1=Button(window_,text="OK",width=8,command=self.file_info)
				b1.place(x=150,y=90)
				window_.mainloop()
		else:
			tkMessageBox.showinfo("Warning", "Provide only one value")

	def parse_logs(self):
		file_content = open(self.filename, "r")
		for line in file_content:
			if 'LOG' in line:
				string_1=line.split(':')
				text_value_=string_1[2].strip()
				self.text_value.append(text_value_.replace("'",''))
				
				text_=string_1[1].strip()
				self.text.append(text_)
				
				string_2=string_1[0].split('(')[1].split(')')[0].split('.')[2]
				self.class_text.append(string_2.strip())
				
				self.imp_line_count+=1
				self.files.append(None)
			
			elif 'STEP' in line:
				line = line.replace("#",'')
				self.steps.append(line)

	def file_info(self):
		rangelist=[int(range_from.get()),int(range_to.get())]
		info_list=[filename_.encode('ascii','ignore'),sheet_name.get(),column_name.get(),rangelist]
		self.files[row]=info_list
		window_.destroy()

	def launch(self):
		self.header()
		new_file_content = open(self.filename,'r').read().splitlines()
		
		global log_count
		i=0
		log_count = 0
		for v in new_file_content:
			if 'LOG' in v:
				log_count+=1
				frame = Frame(sw.window, width=100, borderwidth=2, relief="groove")
				frame.pack(side="top", fill="x")
				self.widgets.append(frame)

				label=Label(frame,width=2,text=str(i+1))
				label.grid(row=i,column=0,padx=5)

				label=Label(frame,width=20,text=self.class_text[i])
				label.grid(row=i,column=1,padx=5)
				
				label_=Label(frame,width=60,  text=self.text[i]+"  : '"+self.text_value[i]+"'",anchor='w',justify=LEFT)
				label_.grid(row=i,column=2,sticky="e")
				
				entry = Entry(frame, width=20,text="")
				entry.grid(row=i, column=3)
				self.entry_list.append(entry)

				button = Button(frame,width=10, text="Pick",command=lambda row=i: self.file_picker(row))
				button.grid(row=i, column=4,padx=10)
				i+=1
			elif 'STEP' in v:
					v = v.replace('#','')
					self.step_data(v)
		
		widget_ = Label(sw.window,width=5)
		widget_.pack(side="left")
  		
  		createWidgetButton_ = Button(sw.window, width=20,text="Reset",command=self.reset_feilds)
		createWidgetButton_.pack(side="left",)
		widget_ = Label(sw.window,width=5)
		widget_.pack(side="left")

		createWidgetButton_1 = Button(sw.window, width=20,text="+",font='times 10 bold',command=self.add_element)

		createWidgetButton_1.pack(side="left")
		widget_ = Label(sw.window,width=5)
		widget_.pack(side="left")

		createWidgetButton_2 = Button(sw.window, width=20,text="-",font='times 10 bold',command=self.delete_element)
 
		createWidgetButton_2.pack(side="left") 
		widget_ = Label(sw.window,width=5)
		widget_.pack(side="left")

	  	createWidgetButton_3 = Button(sw.window, width=20,text="Generate Script", command=self.script_name_popup)

		createWidgetButton_3.pack(side="left")
		widget_ = Label(sw.window,width=5)
		widget_.pack(side="right")
		mainloop()

	def append_window(self):
		global show_Data
		import Tix as tk
		
		root_1=tk.Tk()
		root_1.geometry("800x50")
		
		swn= tk.ScrolledWindow(root_1, scrollbar=tk.Y)
		swn.pack(fill=tk.BOTH, expand=1)
		
		def show_Data(classname_,identifier,textva,pos):
				frame1 = Frame(swn.window, width=100, borderwidth=2, relief="groove")
				frame1.pack(side="top", fill="x")

				label=Label(frame1,width=20,text=classname_)
				label.grid(row=0,column=0,padx=5)
				
				label1=Label(frame1,width=20,text=identifier)
				label1.grid(row=0,column=1,padx=5)
				
				label2=Label(frame1,width=20,text=textva)
				label2.grid(row=0,column=2,padx=5)
				
				label3=Label(frame1,width=20,text=pos)
				label3.grid(row=0,column=3,padx=5)

		b1=Button(swn,text="OK")
		b1.pack(side="left")

		b2=Button(swn,text="Add Field",command=self.add_Element)
		b2.pack(side="right")

		root_1.mainloop()

	def add_element(self):
		global clname, identifier, Element_value, Element_Position, root
		root = Tkinter.Tk()
	
		self.adjust_window_position(750,57,root) 
		
		frame = Frame(root, width=100, borderwidth=2, relief="groove")
		frame.pack(side="top", fill="x")
		
		clname = StringVar()
		clname.set('Select')
		choices = ['EditText','Button','RadioButton','View','Spinner']
		popupMenu = OptionMenu(frame, clname, *choices)
		
		Label(frame, text="Type of Field").grid(row = 1, column = 1, padx=15)
		popupMenu.grid(row = 2, column =1,padx=15)
		popupMenu.config(width=10)
		# popupMenu.pack()

		identifier = StringVar()
		identifier.set('Select')
		choices_ = ['Text','Id']
		popupMenu_ = OptionMenu(frame, identifier, *choices_)

		Label(frame, text="Identifier").grid(row = 1, column = 2, padx=15)
		popupMenu_.grid(row = 2, column =2,padx=15)
		popupMenu_.config(width=10)
		# popupMenu_.pack()

		Element_value = Entry(frame, width=25,text="")
		Label(frame, text="Give Value:").grid(row = 1, column = 3, padx=15)
		Element_value.grid(row=2, column=3,padx=15)

		Element_Position = Entry(frame, width=25,text="")
		Label(frame, text="Give Position").grid(row = 1, column = 4, padx=15)
		Element_Position.grid(row=2, column=4,padx=15)

		Button(frame,width=10,text="Submit",command=self.new_element_info).grid(row=2,column=5,padx=10)
		root.mainloop()
	
	def new_element_info(self):
		file1_content = open(self.filename,'r').read().splitlines()
		global log_count
		log_count=-1

		for new_line in file1_content:
			self.log_line.append(new_line)
			if 'LOG' in new_line:
				log_count+=1

		file1_content_w = open(self.filename,'r').read().splitlines()
		temp = int(Element_Position.get()) - 1
		tempry = clname.get()
		j=-1
		i=-1
		
		for x in file1_content_w:
			j+=1
			if 'LOG' in x:
				i+=1
				if i == temp :
					if tempry == 'Button':
						aline="#" + "LOG(android.widget.Button): Clicked on element with text : '"+Element_value.get()+"'"
						self.log_line.insert(j,aline)

					elif tempry == 'EditText':
						aline="#" +"LOG(android.widget.EditText): Cleared and Typed : '"+Element_value.get()+"'"
						self.log_line.insert(j,aline)
					
					elif tempry == 'Spinner':
						aline="#" + "LOG(android.widget.Spinner): Selected with value : '"+Element_value.get()+"'"
						self.log_line.insert(j,aline)
				
				elif temp>log_count:
					if tempry == 'Button':
						aline="#" + "LOG(android.widget.Button): Clicked on element with text : '"+Element_value.get()+"'"
						self.log_line.insert(len(self.log_line),aline)

					elif tempry == 'EditText':
						aline="#" +"LOG(android.widget.EditText): Cleared and Typed : '"+Element_value.get()+"'"
						self.log_line.insert(len(self.log_line),aline)
					
					elif tempry == 'Spinner':
						aline="#" + "LOG(android.widget.Spinner): Selected with value : '"+Element_value.get()+"'"
						self.log_line.insert(len(self.log_line),aline)
					break
					
		self.rearange_data()
		
		root.destroy()
		app.destroy()

		self.re_launch()

	def delete_element(self):
		global dl_var,root_

		root_=Tkinter.Tk()
		
		self.adjust_window_position(250,80,root_) 

		l1=Label(root_,width=20,text="Which Row to Delete :")
		l1.place(x=5,y=10)

		dl_var = StringVar()
		choices = set()
		for i in range(log_count):
			choices.add(i+1)
		
		popupMenu = OptionMenu(root_, dl_var, *choices)
		popupMenu.place(x=20,y=35)
		popupMenu.config(width=10)
		
		button=Button(root_,width=10,text="Delete",command=self.deleted_element_info)
		button.place(x=160,y=35)
		root_.mainloop()

	
	def deleted_element_info(self):
		file1_content = open(self.filename,'r').read().splitlines()

		for new_line in file1_content:
			self.log_line.append(new_line)

		file1_content_w = open(self.filename,'r').read().splitlines()
		temp = int(dl_var.get()) -1

		j=-1
		i=-1
		for x in file1_content_w:
			j+=1
			if 'LOG' in x:
				i+=1
				if i == temp :
					self.log_line.pop(j)
					
		self.rearange_data()
		
		root_.destroy()
		app.destroy()

		self.re_launch()
	
	def step_data(self, value):
		frame = Frame(sw.window, borderwidth=2, relief="groove")
		frame.pack(side="top", fill="x")
		frame.config(height=3)
		self.widgets.append(frame)
	
		widget = Label(frame,width=26, text = "",font='times 10 bold')
		widget.pack(side="left")
		
		widget = Label(frame,width=30,text = "Step Data Value :" ,font='times 10 bold',anchor='w',justify=LEFT)
		widget.pack(side="left")

		widget = Label(frame,width=60,text=value.split(':')[1].strip(),font='times 10 bold',anchor='w',justify=LEFT)
		widget.pack(side="right")

	def header(self):
		frame = Frame(sw.window, borderwidth=2, relief="groove")
		frame.pack(side="top", fill="x")
		frame.config(height=3)

		widget = Label(frame,width=5, text = "Index",font='times 10 bold')
		widget.pack(side="left")

		widget = Label(frame,width=20, text = "Field Type",font='times 10 bold')
		widget.pack(side="left")

		widget = Label(frame,width=30,text = "Existing Data" ,font='times 10 bold',anchor='w',justify=LEFT)
		widget.pack(side="left")

		widget = Label(frame,width=37,text="Desired Data",font='times 10 bold')
		widget.pack(side="right")

	def generate_script(self, new_filename):
		for index, value in enumerate(self.entry_list):
			text = value.get()
			if not text:
				if self.files[index] == None:	
					self.GUI_List.append(None)
				else:
					self.GUI_List.append(self.files[index])
			else:
				self.GUI_List.append(text)

		for index,value in enumerate(self.GUI_List):
			if value!=None and type(value)==str:
				self.GUI_List[index] = (self.text_value[index], value)
			elif type(value)==list:
				dictionary={}
				dictionary[self.text_value[index]] = value
				self.GUI_List[index] = dictionary
			else:
				self.GUI_List[index] = None
		
		print self.GUI_List
		
		from Script_Parameterization import Parameterise
		script_keyword = 'vc.findViewWith'
		Parameterise(self.filename, script_keyword, new_filename, self.GUI_List)

	def reset_feilds(self):
		for entry in self.entry_list:
			entry.delete(0, 'end')
		self.files=[]
		self.parse_logs()

	def re_launch(self):
		self.text_value =[]
		self.steps =[]
		self.class_text=[]
		self.text=[]
		self.log_line=[]

		self.initialize()
		self.launch()

	def rearange_data(self):
		import os
		os.remove(self.filename)
		print 'file deleated'

		print self.log_line
		print("creating file :"+ self.filename)
		
		with open(self.filename,'w') as file1_content_w: 
			for m in self.log_line:
				file1_content_w.write(m + '\n')
		file1_content_w.close()


	def script_name_popup(self):
		global window, e1
		window=Tkinter.Tk()
		
		self.adjust_window_position(200,80,window)
		window.bind('<Return>', self.user_input_value)

		l1=Label(window,width=30,text="Save the Script with : ")
		l1.pack()

		entry_id = StringVar() 
		e1 = Entry(window, width=30,textvariable = entry_id)
		e1.pack()
		
		b1=Button(window,text="Save",width=10, command = self.user_input_value)
		b1.pack(side=LEFT)
		b1.place(x=10,y=50)

		b2=Button(window, text = "Discard", width=10,command = self.destroy)
		b2.pack(side=RIGHT)
		b2.place(x=110,y=50)
		
		window.mainloop()

	def user_input_value(self,args=None):
		script_name = e1.get()+ '.py'

		window.destroy()

		self.generate_script(script_name)

	def destroy(self):
		window.destroy()

	def adjust_window_position(self,width, height, window_name):
		window_name.resizable(width=False,height=False);	
		width_size=window_name.winfo_screenwidth()
		heigth_size=window_name.winfo_screenheight()
		X=(width_size/2)-(width/2)
		Y=(heigth_size/2)-(height/2)
		window_name.geometry('%dx%d+%d+%d'%(width,height,X,Y))