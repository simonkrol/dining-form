import tkinter as tk

class InfoGUI(tk.Tk):
	"""docstring for Values"""
	def __init__(self, parent, values):
		tk.Tk.__init__(self, parent)
		self.parent = parent
		self.values=values
		self.initialize()

	def initialize(self):
		self.grid()
		stepOne = tk.LabelFrame(self)
		stepOne.grid(row=0, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)

		labels=["First Name", "Last Name", "Student #", "Telephone #", "Email"]
		self.vallbl=[]
		self.valtxt=[]
		self.val=[]

		for i in range(len(labels)):
			self.vallbl.append(tk.Label(stepOne, text=labels[i]))
			self.vallbl[i].grid(row=i, column=0, sticky='E', padx=5, pady=2)

		
			self.valtxt.append(tk.Entry(stepOne))
			self.valtxt[i].grid(row=i, column=1, columnspan=3, pady=2, sticky='WE')
			
			self.valtxt[i].insert(0, self.values[i])
			self.val.append(None)

		ClearBtn = tk.Button(stepOne, text="Clear", command=self.clear)
		ClearBtn.grid(row=len(labels), column=2, sticky='W', padx=5, pady=2)
		SubmitBtn = tk.Button(stepOne, text="Submit",command=self.submit)
		SubmitBtn.grid(row=len(labels), column=3, sticky='W', padx=5, pady=2)

	def submit(self):
		
		for i in range(len(self.valtxt)):
			
			if(self.valtxt[i].get()!=""):
				self.val[i]=(self.valtxt[i]).get()
		self.destroy()

	def clear(self):
		for i in range(len(self.valtxt)):
			self.valtxt[i].delete(0, 100)


