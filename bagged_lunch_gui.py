import tkinter as tk
from gui_calendar import Calendar
from other_gui import InfoGUI, MealsGUI
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

		self.parent.title("Calendar GUI")

		self.data_set_button = tk.Button(self.buttonFrame, text="Set Information", command= lambda: self.create_window('InfoGUI'))
		self.data_set_button.grid(row=1, column=1, padx=8, pady=2)

		self.meal_set_button = tk.Button(self.buttonFrame, text="Set Meals", command= lambda: self.create_window('MealsGUI'))
		self.meal_set_button.grid(row=1, column=3, padx=8, pady=2)

		self.submit_button = tk.Button(self.buttonFrame, text="Send Requests", command=self.send_request)
		self.submit_button.grid(row=1, column=2, padx=8, pady=2)

		self.radioFrame.grid(row=1)
		self.calendarFrame.grid(row=2)
		self.buttonFrame.grid(row=3)

		MODES = [
			("Breakfast", "1"),
			("Lunch", "2"),
			("Dinner", "3"),
		]

		v = tk.StringVar()
		v.set("1") # initialize

		for text, mode in MODES:
			b = tk.Radiobutton(self.radioFrame, text=text, variable=v, value=mode, indicatoron=0)
			b.grid(row=0, sticky='S', column=mode, padx=8, pady=2)

		self.calendar=Calendar(self.calendarFrame, firstweekday=calendar.SUNDAY)
		self.calendar.grid(sticky='S', column=0, padx=8, pady=2)#I have no idea what either of these do, they work the same without them, leaving them in for now

		if 'win' not in sys.platform:	#Checks for the windows operating system, changes style if not
			style = ttk.Style()
			style.theme_use('clam')
	def create_window(self, classval):
		
		command=('%s(None, self.parent)' %classval)
		self.parent.withdraw()
		self.window=eval(command)
		#self.window=InfoGUI(None, self.parent)

	def readInfo(self):
		infile=open_data('data', 'info.dat', 'r')
		self.info={}
		for line in infile:
			split=line.split()
			self.info[split[0]]=split[1]
		infile.close()
		
		self.curMeal="Breakfast"
		mealFile=("%s.dat" %self.curMeal)
		infile=open_data('data', mealFile, 'r')
		self.meal={}
		for line in infile:
			split=line.split()
			self.meal[split[0]]=(' '.join(split[1:len(split)]))
		infile.close()


	def send_request(self):	
		dates=(self.calendar.selection)
		if(dates==None):
			return
		self.readInfo()
		key=self.get_keys()
		date={'input_5': ""}
		payload={**self.info, **self.meal, **key, **date}

		infile=open_data('data', 'dates.dat', 'a')

		for date in dates:
			payload['input_5']= date
			infile.write(date)
			infile.write("\n")
			#r=requests.post(url, data=payload) #Commented out so as not to send a ton of requests while testing
		infile.close()


	def get_keys(self):
		return {'is_submit_3':'1', 'gform_submit':'3', 'state_3':'WyJbXSIsImQ0NjBmMzhkZDZiMGJmYmI3NDI2NDA0YTZkNTIxNzhkIl0='}

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


if __name__ == "__main__":
	root = tk.Tk()
	MainApplication(root).grid(row=5, sticky='N', padx=8, pady=2)#pack(side="top", fill="both", expand=True)
	root.mainloop()


