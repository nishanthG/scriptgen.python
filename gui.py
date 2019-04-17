import Tkinter 
import Tkconstants, tkFileDialog
import tkMessageBox
# from Tkinter import messagebox
from Tkinter import *


class Cmd_New_2(object):
	app=Tkinter.Tk()
	app.resizable(width=0,height=0)
	
	GUI_List = []
	
	class_text=[]
	text = []
	text_value=[]
	
	values = []
	files = []
	
	entry_list = []
	imp_line_count=0	
	
	width=300
	height=60

	def __init__(self):
		self.Log_Reader()		
		# file_content = open("log_file.txt", "r")
		# for index, line in enumerate(file_content):
		# 	if 'LOG' in line:
		# 		string_1=line.split(':')
		# 		text_value_=string_1[2].strip()
		# 		self.text_value.append(text_value_.replace("'",''))
				
		# 		text_=string_1[1].strip()
		# 		self.text.append(text_)
				
		# 		string_2=string_1[0].split('(')[1].split(')')
		# 		self.class_text.append(string_2[0].split('.')[2].strip())
				
		# 		self.imp_line_count+=1
		# 		self.values.append(None)
		# 		self.files.append(None)

		# print(self.values)
		# print(self.files)

	def pickFile(self,r):
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
			# filename.encode('ascii','ignore')
			# filename_1=filename.split("/")[4].strip()
			filename_=self.copy_file(filename)

			if not filename:
				pass
			else:
				window_= Tkinter.Tk()
				window_.resizable(width=
					False,height=False);
				window_.geometry("350x120")
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

				# l5=Label(window_,width=10)
				# l5.place(x=275,y=60)
				b1=Button(window_,text="OK",width=8,command=self.file_info)
				b1.place(x=150,y=90)
				window_.mainloop()
		else:
			tkMessageBox.showinfo("Warning", "Provide only one value")

	def Log_Reader(self):
		file_content = open("log_file.txt", "r")
		for index, line in enumerate(file_content):
			if 'LOG' in line:
				string_1=line.split(':')
				text_value_=string_1[2].strip()
				self.text_value.append(text_value_.replace("'",''))
				
				text_=string_1[1].strip()
				self.text.append(text_)
				
				string_2=string_1[0].split('(')[1].split(')')
				self.class_text.append(string_2[0].split('.')[2].strip())
				
				self.imp_line_count+=1
				# self.values.append(None)
				self.files.append(None)


	def file_info(self):
		rangelist=[int(range_from.get()),int(range_to.get())]
		info_list=[filename_.encode('ascii','ignore'),sheet_name.get(),column_name.get(),rangelist]
		self.files[row]=info_list
		print self.files
		window_.destroy()

	def show(self):
		for i in info_list:
			print i

	def GUI_Maker(self):
		self.header()
		for i in range(self.imp_line_count): #Rows
			frame = Frame(self.app, width=100, borderwidth=2, relief="groove")
			frame.pack(side="top", fill="x")

			label=Label(frame,width=20,text=self.class_text[i])
			label.grid(row=i,column=0,padx=5)
			
			label_=Label(frame,width=50,  text=self.text[i]+"  : '"+self.text_value[i]+"'",anchor='w',justify=LEFT)
			label_.grid(row=i,column=1,sticky="e")
			
			entry = Entry(frame, width=20,text="")
			entry.grid(row=i, column=2)
			self.entry_list.append(entry)

			button = Button(frame,width=10, text="Pick",command=lambda row=i: self.pickFile(row))
			button.grid(row=i, column=3,padx=10)
		widget_ = Label(self.app,width=5)
		widget_.pack(side="left")
  		createWidgetButton_ = Button(self.app, width=20,text="Reset",command=self.Clear)
		createWidgetButton_.pack(side="left",)
		widget = Label(self.app,width=5)
		widget.pack(side="right")
	  	createWidgetButton_ = Button(self.app, width=20,text="Generate Script", command=self.Generate_Script)
	  	widget.config(height = 2)

		createWidgetButton_.pack(side="right")
		mainloop()
	def header(self):
		frame = Frame(self.app, borderwidth=2, relief="groove")
		frame.pack(side="top", fill="x")
		frame.config(height=3)
		widget = Label(frame,width=22, text = "Field Type",font='times 10 bold')
		widget.pack(side="left")

		widget = Label(frame,width=25,text = "Existing Data" ,font='times 10 bold',anchor='w',justify=LEFT)
	    # self.widgets.append(widget)
		widget.pack(side="left")
		widget = Label(frame,width=25,text="Desired Data",font='times 10 bold')
		# self.widgets.append(widget)
		widget.pack(side="right")

	def copy_file(self, file_path):
		import shutil, os
		cudir=os.getcwd()
		file=file_path.split("/")[-1]
		# file, extension = os.path.splitext(file_path)
		destination = cudir+"/"+file+'.bak'
		shutil.copy2(file_path, destination)
		return file+'.bak'

	def Generate_Script(self):
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

	def Clear(self):
		for entry in self.entry_list:
			entry.delete(0, 'end')
		self.files=[]
		self.Log_Reader()


Cmd_New_2().GUI_Maker()