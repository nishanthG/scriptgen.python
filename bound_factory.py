from layout import UIDump
import Tkinter 
from Tkinter import *
from ScriptGen import ScriptGen

#from UIDump import elements

class Divide_and_Conquer():

	def __init__(self, XY):
		self.XY = XY
		self.user_val = 'None'
		self.flag = 'green'

		print self.XY
	
	def bounds_Compare(self, bounds):
		""" Compares the bounds with Master XY and generates the Script fro given Element. """

		# removed "android.widget.Spinner", "android.widget.ExpandableListView" from reqlist, it's interfering with the view.
 		
 		reqlist = ["android.widget.EditText",
 		"android.widget.Button", "android.widget.CheckBox", "android.widget.RadioButton", "android.widget.TextView", "android.widget.RelativeLayout",
 		"android.widget.ImageView", "android.app.Dialogue", "android.view.View"]

 		ignore_list = [None,'','None']
		
		collection = []
		logs = []

		count = 0
		len_bounds = len(bounds)
		
		for i in bounds:
			print '\n ---------------------------------------------- \n'
			# print "for every bound block" ----> DEBUG < -----
			if int(bounds[count][2]) <= self.XY[1] <= int(bounds[count][3]):
				if int(bounds[count][0]) <= self.XY[0] <= int(bounds[count][1]):
					
					# print "current X_Y : ", str(self.XY)
					# print "current bounds : ", str(UIDump.bounds[count])
					# print "unique id : ", str(UIDump.check_unique_id[count])
					# print "resource id : ", str(UIDump.check_resource_id[count])
					# print "current text : ", str(UIDump.check_text[count])

					# print "in range block" ----> DEBUG < -----
						
					if UIDump.elements[count] in reqlist:
						# print "in reqlist block" ----> DEBUG < -----
						
						if  UIDump.elements[count] == reqlist[0]:
							# print "EditText block" ----> DEBUG < -----

							window = Tkinter.Tk()
							
							window.resizable(width=False,height=False);
							window.geometry("200x80")
							
							l1=Label(window,width=30,text="Enter Text to Type: ")
							l1.pack()

							self.entry_id = StringVar() 
							e1 = Entry(window, width=30,textvariable=self.entry_id)
							e1.pack()
							
							def input(args= None):
								self.user_val = e1.get()
								window.destroy()		
									
								if self.resource_id not in ignore_list:
									ScriptGen().script("vc.findViewByIdOrRaise('{id}').setText('{text}')\n".format(id=self.resource_id, text=self.user_val))
									ScriptGen().log("#LOG({classname}): Cleared and Typed : '{text}' on id : '{id}'\n".format(classname =self.classname,text=self.user_val, id=self.resource_id))
									

								elif self.unique_id not in ignore_list:
									ScriptGen().script("vc.findViewByIdOrRaise('{id}').setText('{text}')\n".format(id=self.unique_id, text=self.user_val))
									ScriptGen().log("#LOG({classname}): Cleared and Typed : '{text}'\n".format(classname =self.classname,text=self.user_val))
											

								elif UIDump.check_text[count] not in ignore_list:
									ScriptGen().script("vc.findViewWithTextOrRaise('{id_text}').setText('{text}')\n".format(id_text=UIDump.check_text[count], text=self.user_val))
									ScriptGen().log("#LOG({classname}): Cleared and Typed : '{text}' on Element with text : '{id_text}'\n".format(classname =self.classname,id_text=UIDump.check_text[count], text=self.user_val))
								

								else :
									ScriptGen().script("device.touchDip({X},{Y},0)\n".format(X=int(self.XY[0]), Y=int(self.XY[1])))
									ScriptGen().log("#LOG({classname}): Vulnerable/Unstable field on co-ordinates ({X},{Y})\n".format(classname ="Vulnerable",X=int(self.XY[0]), Y=int(self.XY[1])))

							def framedestroy():
								window.destroy()

							self.unique_id = UIDump.check_unique_id[count]
							self.resource_id = UIDump.check_resource_id[count]
							self.classname = UIDump.check_className[count]

							b1=Button(window,text="Ok",width=10, command = input)
							b1.pack(side=LEFT)
							b1.place(x=10,y=50)
							
							b2=Button(window, text = "Cancel", width=10, command = framedestroy)
							b2.pack(side=RIGHT)
							b2.place(x=110,y=50)

							window.bind('<Return>', input)
							
							window.mainloop()
							
							self.flag = 'red'
							break
					
						elif UIDump.elements[count] in reqlist[1:4]:
							# print "Button block" ----> DEBUG < -----

							self.unique_id = UIDump.check_unique_id[count]
							self.resource_id = UIDump.check_resource_id[count]
							self.classname = UIDump.check_className[count]

							if UIDump.check_text[count] not in ignore_list:
								log_ = "#LOG({classname}): Clicked on element with text : '{id}'\n".format(classname =self.classname,id=UIDump.check_text[count])
								line = "vc.findViewWithTextOrRaise('{id}').touch()\n\tvc.sleep(3)\n".format(id=UIDump.check_text[count])
								if line not in collection: 
									collection.append(line)
									logs.append(log_)
								break

							elif self.resource_id not in ignore_list:
								log_ = "#LOG({classname}): Clicked on : '{id}'\n".format(classname =self.classname,id=self.resource_id)
								line = "vc.findViewByIdOrRaise('{id}').touch()\n\tvc.sleep(3)\n".format(id=self.resource_id)
								if line not in collection: 
									collection.append(line)
									logs.append(log_)
								break

							elif self.unique_id not in ignore_list:
								log_ = "#LOG({classname}): Clicked on : '{id}'\n".format(classname =self.classname,id=self.unique_id)
								line = "vc.findViewByIdOrRaise('{id_text}').touch()\n\tvc.sleep(3)\n".format(id_text=self.unique_id)
								if line not in collection: 
									collection.append(line)
									logs.append(log_)
								break
							
							else :
								log_ = "#LOG({classname}): Vulnerable/Unstable field on co-ordinates ({X},{Y})\n".format(classname =self.classname,X=int(self.XY[0]), Y=int(self.XY[1]))
								line = "device.touchDip({X},{Y},0)\n\tvc.sleep(3)\n".format(X=int(self.XY[0]), Y=int(self.XY[1]))
								if line not in collection: 
									collection.append(line)
									logs.append(log_)
								break

						elif UIDump.elements[count] in reqlist[4:]:
							# print "remaining views block" ----> DEBUG < -----

							self.unique_id = UIDump.check_unique_id[count]
							self.resource_id = UIDump.check_resource_id[count]
							self.classname = UIDump.check_className[count]

							if UIDump.check_text[count] not in ignore_list:
								log_ = "#LOG({classname}): Clicked on element with Text : '{id}'\n".format(classname =self.classname,id=UIDump.check_text[count])
								line = "vc.findViewWithTextOrRaise('{id}').touch()\n".format(id=UIDump.check_text[count])
								if line not in collection: 
									collection.append(line)
									logs.append(log_)

							elif self.resource_id not in ignore_list:
								log_ = "#LOG({classname}): Clicked on : '{id}'\n".format(classname =self.classname,id=self.resource_id)
								line = "vc.findViewByIdOrRaise('{id}').touch()\n".format(id=self.resource_id)
								if line not in collection: 
									collection.append(line)
									logs.append(log_)

							elif self.unique_id not in ignore_list:
								log_ = "#LOG({classname}): Clicked on : '{id}'\n".format(classname =self.classname,id=self.unique_id)
								line = "vc.findViewByIdOrRaise('{id_text}').touch()\n".format(id_text=self.unique_id)
								if line not in collection: 
									collection.append(line)
									logs.append(log_)
							
							else :
								log_ = "#LOG({classname}): Vulnerable/Unstable field on co-ordinates ({X},{Y})\n".format(classname ='Vulnerable',X=int(self.XY[0]), Y=int(self.XY[1]))
								line = "device.touchDip({X},{Y},0)\n\tvc.sleep(3)\n".format(X=int(self.XY[0]), Y=int(self.XY[1]))
								if line not in collection: 
									collection.append(line)
									logs.append(log_)

						else:
							# print "not in imp view block" ----> DEBUG < -----
							log_ = "#LOG({classname}): Vulnerable/Unstable field on co-ordinates ({X},{Y})\n".format(classname ='Vulnerable',X=int(self.XY[0]), Y=int(self.XY[1]))
							line = "device.touchDip({X},{Y},0)\n\tvc.sleep(3)\n".format(X=int(self.XY[0]), Y=int(self.XY[1]))
							if line not in collection: 
								collection.append(line)
								logs.append(log_)
							break
										
					elif UIDump.elements[count] in ["android.widget.FrameLayout"]:
						# print "FrameLayout block" ----> DEBUG < -----
						log_ = "#LOG({classname}): Vulnerable/Unstable field on co-ordinates ({X},{Y})\n".format(classname ='Vulnerable',X=int(self.XY[0]), Y=int(self.XY[1]))
						line = "device.touchDip({X},{Y},0)\n\tvc.sleep(3)\n".format(X=int(self.XY[0]), Y=int(self.XY[1]))
						if line not in collection: 
							collection.append(line)
							logs.append(log_)
				
			count += 1

		else :
			# print "nothing matches block" ----> DEBUG < -----
			log_ = "#LOG({classname}): Vulnerable/Unstable field on co-ordinates ({X},{Y})\n".format(classname ='Vulnerable',X=int(self.XY[0]), Y=int(self.XY[1]))
			line = "device.touchDip({X},{Y},0)\n\tvc.sleep(3)\n".format(X=int(self.XY[0]), Y=int(self.XY[1]))
			if line not in collection: 
				collection.append(line)
				logs.append(log_)

		print collection
		print logs
		# ----> DEBUG < -----
		
		if self.flag == 'green':
			ScriptGen().script(collection[-1])
			ScriptGen().log(logs[-1])
		else:
			pass

def main():
	Divide_and_Conquer().bounds_Compare(bounds)

if __name__ == '__main__':
	main()