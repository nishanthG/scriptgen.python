from Tkinter import *
import Tkinter
from Vysor import UI
from File_Generator import File_Generator

def S_initialize():
	script_name_popup()

def script_name_popup():
	global window, e1
	window=Tkinter.Tk()
	
	adjust_window_position(200,80,window)
	window.bind('<Return>', user_input_value)

	l1=Label(window,width=30,text="Save the Script with : ")
	l1.pack()

	entry_id = StringVar() 
	e1 = Entry(window, width=30,textvariable = entry_id)
	e1.pack()
	
	b1=Button(window,text="Save",width=10, command = user_input_value)
	b1.pack(side=LEFT)
	b1.place(x=10,y=50)

	b2=Button(window, text = "Discard", width=10,command = destroy)
	b2.pack(side=RIGHT)
	b2.place(x=110,y=50)
	
	window.mainloop()

def user_input_value(args=None):
	script_name = e1.get()
	window.destroy()

	File_Generator(script_name).generate_files()
	UI(script_name).popup()

def destroy():
	window.destroy()

def adjust_window_position(width, height, window_name):
	window_name.resizable(width=False,height=False);	
	width_size=window_name.winfo_screenwidth()
	heigth_size=window_name.winfo_screenheight()
	X=(width_size/2)-(width/2)
	Y=(heigth_size/2)-(height/2)
	window_name.geometry('%dx%d+%d+%d'%(width,height,X,Y))