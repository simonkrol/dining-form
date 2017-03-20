import tkinter as tk
from gui_calendar import Calendar
from other_gui import InfoGUI, MealsGUI
from lunch_methods import open_data
import calendar
import requests
import tkinter.font
import sys
import os


class MainApplication(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		#self.keyorder=['input_1.3', 'input_1.6', 'input_2', 'input_3', 'input_4']
		self.parent = parent

		self.radioFrame=tk.Frame(self)
		self.buttonFrame=tk.Frame(self)
		self.calendarFrame=tk.Frame(self)
		self.labelFrame=tk.Frame(self)

		self.parent.title("Calendar GUI")

		self.data_set_button = tk.Button(self.buttonFrame, text="Set Information", command= lambda: self.create_window('InfoGUI'))
		self.data_set_button.grid(row=1, column=1, padx=8, pady=2)

		self.meal_set_button = tk.Button(self.buttonFrame, text="Set Meals", command= lambda: self.create_window('MealsGUI'))
		self.meal_set_button.grid(row=1, column=3, padx=8, pady=2)

		self.submit_button = tk.Button(self.buttonFrame, text="Send Requests", command=self.send_request)
		self.submit_button.grid(row=1, column=2, padx=8, pady=2)

		self.warning_text=tk.StringVar(self.labelFrame)
		self.warning=tk.Label(self.labelFrame, textvariable=self.warning_text)
		self.warning.grid(row=1, column=1, padx=8, pady=2)

		self.radioFrame.grid(row=1)
		self.calendarFrame.grid(row=2)
		self.buttonFrame.grid(row=3)
		self.labelFrame.grid(row=4)

		MODES = [
			("Breakfast", 1),
			("Lunch", 2),
			("Dinner", 3),
		]

		self.v = tk.StringVar()
		self.v.set(1) # initialize

		for text, mode in MODES:
			b = tk.Radiobutton(self.radioFrame, text=text, variable=self.v, value=mode, indicatoron=0, command=self.reset_blocks)
			b.grid(row=0, sticky='S', column=mode, padx=8, pady=2)

		self.calendar=Calendar( self.v, self.calendarFrame, firstweekday=calendar.SUNDAY, )
		self.calendar.grid(sticky='S', column=0, padx=8, pady=2)#I have no idea what either of these do, they work the same without them, leaving them in for now

		if 'win' not in sys.platform:	#Checks for the windows operating system, changes style if not
			style = ttk.Style()
			style.theme_use('clam')
	def create_window(self, classval):
		self.warning_text.set("")
		command=('%s(self, self.parent)' %classval)
		self.parent.withdraw()
		self.window=eval(command)


	def readInfo(self):
		infile=open_data('data', 'info.dat', 'r')
		self.info={}
		for line in infile:
			split=line.split()
			self.info[split[0]]=split[1]
		infile.close()
		if(self.v.get()=='1'):
			self.mealType="Breakfast"
		elif(self.v.get()=='2'):
			self.mealType="Lunch"
		else:
			self.mealType="Dinner"
		mealfile=("%s.dat" %self.mealType)

		infile=open_data('data', mealfile, 'r')
		self.meal={}
		for line in infile:
			split=line.split()
			self.meal[split[0]]=(' '.join(split[1:len(split)]))
		infile.close()


	def send_request(self):
		self.warning_text.set("Yo")
		dates=(self.calendar.selection())
		print(dates)
		if(dates==[]):
			self.warning_text.set("No dates selected")
			return
		self.readInfo()
		if(self.info=={} or self.meal=={}):
			self.warning_text.set("Please make sure your info and meals are filled out")
			return
		self.warning_text.set("")
		key=self.get_keys()
		date={'input_5': "", 'input_6': self.mealType} #Generate dictionary representing the data and the type of meal being ordered
		payload={**self.info, **self.meal, **key, **date}
		infile=open_data('data', 'dates.dat', 'a')
		url = 'http://dining.carleton.ca/locations/fresh-food-company/'
		for date in dates:
			payload['input_5']= date
			writetext=('%s %s %s\n' %(self.v.get(), date, self.info['input_2']))
			infile.write(writetext)
			print(date)
			#r=requests.post(url, data=payload) #Commented out so as not to send a ton of requests while testing
		infile.close()
		self.reset_blocks()


	def get_keys(self):
		return {'is_submit_3':'1', 'gform_submit':'3', 'state_3':'WyJbXSIsImQ0NjBmMzhkZDZiMGJmYmI3NDI2NDA0YTZkNTIxNzhkIl0='}
	
	def reset_blocks(self):
		self.calendar._blocks()



if __name__ == "__main__":
	root = tk.Tk()
	MainApplication(root).grid(row=5, sticky='N', padx=8, pady=2)#pack(side="top", fill="both", expand=True)
	root.mainloop()


