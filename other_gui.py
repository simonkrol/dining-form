import tkinter as tk

class InfoGUI(tk.Tk):
	"""docstring for Values"""
	def __init__(self, parent, upperparent):
		tk.Tk.__init__(self, parent)
		self.parent=parent
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
			
			if(self.values[i]!=None):
				self.valtxt[i].insert(0, self.values[i])
			self.val.append(None)

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

		self.val
		try:
			open('data/info.dat', 'x')
		except OSError as e:
			pass
		infile=open('data/info.dat', 'w')
		for i in range(len(self.val)):
			infile.write(self.keyorder[i])
			infile.write(' ')
			infile.write(self.val[i])
			infile.write("\n")
		infile.close()

	def readInfo(self):
		try:
			open('data/info.dat', 'x')
		except OSError as e:
			pass
		infile=open('data/info.dat', 'r')
		self.values=[]
		for line in infile:
			split=line.split()
			self.values.append(split[1])
		infile.close()