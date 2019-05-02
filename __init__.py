import Tkinter,tkFileDialog
from Tkinter import * 
import UI
from UI import GUI
from S__init__ import S_initialize

window = Tkinter.Tk()

def file_picker():
	filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.txt"),("all files","*.*")))
	filename = copy_file(filename)

	obj = GUI(filename)
	obj.initialize()
	obj.launch()

def generate_script():
	S_initialize()

def copy_file(file_path):
	import shutil, os
	cudir=os.getcwd()
	file=file_path.split("/")[-1].split('.')[0]
	destination = cudir+"/"+file+'_copy.txt'
	shutil.copy2(file_path, destination)
	return file+'_copy.txt'

def adjust_window_position(width, height, window_name):
	window_name.resizable(width=False,height=False);	
	width_size=window_name.winfo_screenwidth()
	heigth_size=window_name.winfo_screenheight()
	X=(width_size/2)-(width/2)
	Y=(heigth_size/2)-(height/2)
	window_name.geometry('%dx%d+%d+%d'%(width,height,X,Y))

def initialize_process():
	adjust_window_position(240, 80, window)

	b1=Button(window, width = 30, text="Generate Script",command = generate_script)
	b1.place(x=10,y=10)

	b2=Button(window,width = 30, text="Edit Script", command = file_picker)
	b2.place(x=10,y=50)
	window.mainloop()

if __name__ == '__main__':
 	initialize_process()