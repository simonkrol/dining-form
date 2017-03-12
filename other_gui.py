import tkinter as tk
import os
import sys

class InfoGUI(tk.Tk):
	"""docstring for Values"""
	def __init__(self, parent, upperparent):
		tk.Tk.__init__(self, parent)
		self.bind('<Return>', self.submit)
		self.initialize()
		self.upperparent=upperparent
		self.keyorder=['input_1.3', 'input_1.6', 'input_2', 'input_3', 'input_4']

	def initialize(self):
		self.grid()
		stepOne = tk.LabelFrame(self)
		stepOne.grid(row=0, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)

		labels=["First Name", "Last Name", "Student #", "Telephone #", "Email"]
		self.vallbl=[]
		self.valtxt=[]
		self.val=[]
		self.readInfo()
		for i in range(len(labels)):
			self.vallbl.append(tk.Label(stepOne, text=labels[i]))
			self.vallbl[i].grid(row=i, column=0, sticky='E', padx=5, pady=2)

		
			self.valtxt.append(tk.Entry(stepOne))
			self.valtxt[i].grid(row=i, column=1, columnspan=3, pady=2, sticky='WE')
			try:
				self.valtxt[i].insert(0, self.val[i])
			except:
				pass

		ClearBtn = tk.Button(stepOne, text="Clear", command=self.clear)
		ClearBtn.grid(row=len(labels), column=2, sticky='W', padx=5, pady=2)
		SubmitBtn = tk.Button(stepOne, text="Submit",command=self.submit)
		SubmitBtn.grid(row=len(labels), column=3, sticky='W', padx=5, pady=2)

	def submit(self, event=None):
		
		for i in range(len(self.valtxt)):
			
			if(self.valtxt[i].get()!=""):
				self.val[i]=(self.valtxt[i]).get()
			else:
				return
		self.upperparent.deiconify()
		self.writeInfo()
		self.destroy()


	def clear(self):
		for i in range(len(self.valtxt)):
			self.valtxt[i].delete(0, 100)
	
	def writeInfo(self):
		infile=open_data('data', 'info.dat', 'w')
		for i in range(len(self.val)):
			infile.write(self.keyorder[i])
			infile.write(' ')
			infile.write(self.val[i])
			infile.write("\n")
		infile.close()

	def readInfo(self):
		infile=open_data('data', 'info.dat', 'r')
		self.val=[]
		for line in infile:
			split=line.split()
			self.val.append(split[1])
		infile.close()

def open_data(dir_loc, file, opentype):
	directory = ('%s\%s\%s' %(os.path.realpath('..'), 'dining form', dir_loc))
	if not os.path.exists(directory):
		print(directory)
		os.makedirs(directory)
	
	else:
		print(directory)
		print (os.path.exists(directory))
	location=('%s/%s' %(dir_loc, file))
	try:
		open(location, 'x')
	except OSError as e:
		pass
	infile=open(location, opentype)
	return infile
