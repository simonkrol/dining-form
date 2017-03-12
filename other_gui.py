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
class MealsGUI(tk.Tk):
	def __init__(self, parent, upperparent):
		tk.Tk.__init__(self, parent)
		self.upperparent=upperparent
		self.parent=parent
		self.bind('<Return>', self.submit)
		self.initialize()


	def initialize(self):
		self.grid()
		stepOne = tk.LabelFrame(self)
		stepOne.grid(row=0, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)


		Breakfast = tk.Button(stepOne, text="Breakfast", command= lambda: self.create_window('Breakfast'))
		Breakfast.config( height = 2, width = 11 )
		Breakfast.grid(row=1, column=1, sticky='W', padx=8, pady=2)
		Lunch = tk.Button(stepOne, text="Lunch", command= lambda: self.create_window('Lunch'))
		Lunch.config( height = 2, width = 11 )
		Lunch.grid(row=2, column=1, sticky='W', padx=8, pady=2)
		Dinner = tk.Button(stepOne, text="Dinner", command= lambda: self.create_window('Dinner'))
		Dinner.config( height = 2, width = 11 )
		Dinner.grid(row=3, column=1, sticky='W', padx=8, pady=2)
		SubmitBtn = tk.Button(stepOne, text="Submit",command=self.submit)
		SubmitBtn.config( height = 2, width = 11 )
		SubmitBtn.grid(row=4, column=1, sticky='W', padx=8, pady=2)

	def submit(self, event=None):
		
		self.upperparent.deiconify()

		self.destroy()

	def create_window(self, classval):
		self.withdraw()
		self.window=MealGUI(None, self, classval)

class MealGUI(tk.Tk):
	def __init__(self, parent, upperparent, mealtype):
		tk.Tk.__init__(self, parent)
		self.upperparent=upperparent
		self.parent=parent
		self.bind('<Return>', self.submit)
		self.mealtype=mealtype
		self.BreakfastKey=['input_6', 'input_14', 'input_16']
		self.LunchDinnerKey=['input_6', 'input_15', 'input_16', 'input_17', 'input_18', 'input_19']
		self.initialize()

	def initialize(self):
		self.grid()
		self.numOptions=0
		self.options
		self.stepOne = tk.LabelFrame(self)
		self.stepOne.grid(row=0, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
		vegchoice= ['Carrot and celery sticks', 'Piece of fruit (based on seasonal availability)', 'Fruit cup']
		drinkchoice=['Coke', 'Diet Coke', 'Sprite', 'Ginger ale', 'Apple Juice', 'Orange Juice', 'Water']
		breakfastchoice=['Bagel with cream cheese', 'Piece of fruit (based on seasonal availability)', 'Pastry item', 'Yogurt']
		saladchoice=['Caesar', 'Ranch', 'French', 'Italian']
		sandwichchoice=['Beef', 'Corn Beef', 'Turkey', 'Ham', 'Vegetarian']
		dessertchoice=['Granola Bar', 'Pastry Item']
		self.var=[]
		self.readInfo()
		if(self.mealtype=='Breakfast'):
			self.options(breakfastchoice, "Breakfast")
		else:
			self.options(vegchoice, "Veggie")
		self.options(drinkchoice, "Drink")
		if(self.mealtype!="Breakfast"):
			self.options(saladchoice, "Dressing")
			self.options(sandwichchoice, "Sandwich Filling")
			self.options(dessertchoice, "Dessert")
		SubmitBtn = tk.Button(self.stepOne, text="Submit",command=self.submit)
		SubmitBtn.config( height = 2, width = 11 )
		SubmitBtn.grid(row=self.numOptions, column=1, sticky='W', padx=8, pady=2)

	def submit(self, event=None):
		self.val=[]
		for i in range(self.numOptions):
			self.val.append(self.var[i].get())
		self.writeInfo()
		self.upperparent.deiconify()
		self.destroy()

	def options(self, choices, title):
		optionNum=self.numOptions
		self.grid()	
		self.optionFrame = tk.LabelFrame(self.stepOne)
		self.optionFrame.grid(row=optionNum, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
		self.var.append(tk.StringVar(self.optionFrame))
		try:
			self.var[optionNum].set(self.val[optionNum])
		except:

			self.var[optionNum].set(choices[0])
		optionLabel=tk.Label(self.optionFrame, text=title)
		optionLabel.pack(side='left', padx=10, pady=10)
		option = tk.OptionMenu(self.optionFrame, self.var[optionNum], *choices)
		option.pack(side='left', padx=10, pady=10)
		self.numOptions+=1

	def writeInfo(self):
		mealfile=("%s.dat" %self.mealtype)
		if(self.mealtype=="Breakfast"):
			keyorder=self.BreakfastKey
		else:
			keyorder=self.LunchDinnerKey
		infile=open_data('data', mealfile, 'w')
		for i in range(len(self.val)):
			infile.write(keyorder[i])
			infile.write(' ')
			infile.write(self.val[i])
			infile.write("\n")
		infile.close()

	def readInfo(self):
		mealfile=("%s.dat" %self.mealtype)
		infile=open_data('data', mealfile, 'r')
		self.val=[]
		for line in infile:
			split=line.split()
			self.val.append(' '.join(split[1:len(split)]))
		infile.close()



def open_data(dir_loc, file, opentype):
	directory = ('%s\%s\%s' %(os.path.realpath('..'), 'dining form', dir_loc))
	if not os.path.exists(directory):
		os.makedirs(directory)
	location=('%s/%s' %(dir_loc, file))
	try:
		open(location, 'x')
	except OSError as e:
		pass
	infile=open(location, opentype)
	return infile
